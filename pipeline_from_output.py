#!/usr/bin/env python3
"""
一鱼多吃 Pipeline v1.0
触发：03_Output/ 有新 .md 文件
流程：
  1. 博客同步（中文 + 英文翻译 + 封面）
  2. 小红书图文版生成
  3. 移入 archive/公众号文章/
  4. Telegram 通知 Charlotte
"""

import os, re, shutil, subprocess, json, sys, requests
from datetime import date, datetime
from pathlib import Path

VAULT        = "/opt/my-obsidian-vault"
OUTPUT_DIR   = os.path.join(VAULT, "03_Output")
ARCHIVE_DIR  = os.path.join(VAULT, "archive", "公众号文章")
XIAOHONGSHU_DIR = os.path.join(VAULT, "03_Output", "小红书草稿")
BLOG_SCRIPT  = "/opt/charlotteailab-blog/sync_from_output.py"
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT  = "8343502493"
GEMINI_KEY     = os.environ.get("GEMINI_API_KEY", "")


# ──────────────────────────────────────────────────────
# Telegram 通知
# ──────────────────────────────────────────────────────
def notify(msg: str):
    if not TELEGRAM_TOKEN:
        print(f"[NOTIFY] {msg}")
        return
    try:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            json={"chat_id": TELEGRAM_CHAT, "text": msg, "parse_mode": "HTML"},
            timeout=10
        )
    except Exception as e:
        print(f"Telegram通知失败: {e}")


# ──────────────────────────────────────────────────────
# 获取新文件列表（03_Output/ 里还没有在 archive 里的 .md）
# ──────────────────────────────────────────────────────
def get_new_files():
    if not os.path.exists(OUTPUT_DIR):
        return []
    archived = {f for f in os.listdir(ARCHIVE_DIR)} if os.path.exists(ARCHIVE_DIR) else set()
    new = []
    for f in os.listdir(OUTPUT_DIR):
        if f.endswith('.md') and f not in archived:
            new.append(f)
    return sorted(new)


# ──────────────────────────────────────────────────────
# 小红书图文版生成（用 Gemini 改写）
# ──────────────────────────────────────────────────────
def generate_xiaohongshu(title: str, body: str, slug: str) -> str | None:
    if not GEMINI_KEY:
        print("  ⚠️ 无 GEMINI_API_KEY，跳过小红书生成")
        return None

    prompt = f"""你是一位小红书爆款内容专家。请将以下公众号文章改写为小红书图文笔记。

要求：
1. 标题：加emoji，20字以内，口语化，带悬念或利益点
2. 正文：500字以内，分3-5个小节，每节2-4句话，多用emoji，短句为主
3. 结尾：一句互动引导（如"你试过吗？评论区聊聊"）
4. Tags：5-8个相关话题标签，格式 #标签
5. 封面文案：一句话，15字以内，适合做封面大字

返回 JSON 格式：
{{"title": "小红书标题", "body": "正文内容", "tags": "#标签1 #标签2 ...", "cover_text": "封面文案"}}

原文标题：{title}

原文内容：
{body[:4000]}
"""

    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_KEY}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.7, "maxOutputTokens": 2048}
        }
        r = requests.post(url, json=payload, timeout=60)
        data = r.json()
        text = data['candidates'][0]['content']['parts'][0]['text'].strip()
        text = re.sub(r'^```json\s*', '', text)
        text = re.sub(r'\s*```$', '', text)
        result = json.loads(text)

        xhs_title    = result.get('title', title)
        xhs_body     = result.get('body', '')
        xhs_tags     = result.get('tags', '')
        xhs_cover    = result.get('cover_text', '')

        os.makedirs(XIAOHONGSHU_DIR, exist_ok=True)
        out_path = os.path.join(XIAOHONGSHU_DIR, f"{slug}_小红书.md")
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(f"# {xhs_title}\n\n")
            f.write(f"> 封面文案：**{xhs_cover}**\n\n")
            f.write(f"{xhs_body}\n\n")
            f.write(f"{xhs_tags}\n")

        print(f"  📱 小红书草稿: {out_path}")
        return xhs_title

    except Exception as e:
        print(f"  ⚠️ 小红书生成失败: {e}")
        return None


# ──────────────────────────────────────────────────────
# 读取文章 title 和 body（简单解析，无需完整 front matter）
# ──────────────────────────────────────────────────────
def read_article(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    title = os.path.splitext(os.path.basename(filepath))[0]
    title = re.sub(r'^\d{4}-\d{2}-\d{2}_?', '', title)
    body = content
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            import yaml
            try:
                fm = yaml.safe_load(parts[1])
                if isinstance(fm, dict):
                    title = fm.get('title', title) or fm.get('标题', title) or title
            except Exception:
                pass
            body = parts[2].strip()
    return title, body


# ──────────────────────────────────────────────────────
# 主流程
# ──────────────────────────────────────────────────────
def main():
    new_files = get_new_files()
    if not new_files:
        print("✅ 03_Output/ 无新文章，跳过")
        return

    print(f"🆕 发现 {len(new_files)} 篇新文章: {', '.join(new_files)}\n")
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    os.makedirs(XIAOHONGSHU_DIR, exist_ok=True)

    results = []

    for fname in new_files:
        src_path = os.path.join(OUTPUT_DIR, fname)
        print(f"{'='*50}")
        print(f"📄 处理: {fname}")

        title, body = read_article(src_path)
        slug = re.sub(r'[^a-zA-Z0-9\u4e00-\u9fff]+', '-', os.path.splitext(fname)[0]).strip('-')

        # ── Step 1: 先复制到 archive（让博客脚本能读到）──
        archive_path = os.path.join(ARCHIVE_DIR, fname)
        shutil.copy2(src_path, archive_path)
        print(f"  📦 已暂存到 archive/")

        # ── Step 2: 触发博客同步 ──
        print(f"  🔄 博客同步中...")
        result = subprocess.run(
            [sys.executable, BLOG_SCRIPT],
            capture_output=True, text=True
        )
        blog_ok = result.returncode == 0
        if blog_ok:
            print(f"  ✅ 博客同步完成")
        else:
            print(f"  ❌ 博客同步失败:\n{result.stdout[-1000:]}\n{result.stderr[-500:]}")
            # 同步失败时从 archive 移回，保留在 03_Output 等待重试
            os.remove(archive_path)
            results.append((fname, False, None, "博客同步失败"))
            continue

        # ── Step 3: 小红书图文生成 ──
        print(f"  📱 生成小红书版本...")
        xhs_title = generate_xiaohongshu(title, body, slug)

        # ── Step 4: 从 03_Output 删除（已在 archive 里了）──
        os.remove(src_path)
        print(f"  🗂️  已归档，03_Output/ 中已移除")

        results.append((fname, blog_ok, xhs_title, title))
        print()

    # ── Step 5: git commit vault（小红书草稿）──
    try:
        os.chdir(VAULT)
        subprocess.run(["git", "add", "-A"], check=True, capture_output=True)
        commit = subprocess.run(
            ["git", "commit", "-m", f"pipeline: {len(new_files)}篇文章已归档，小红书草稿已生成"],
            capture_output=True, text=True
        )
        if commit.returncode == 0:
            subprocess.run(["git", "push", "origin", "main"], capture_output=True)
            print("✅ Vault git push 完成")
    except Exception as e:
        print(f"⚠️ Vault git push 失败: {e}")

    # ── Step 6: Telegram 通知 ──
    success = [r for r in results if r[1]]
    failed  = [r for r in results if not r[1]]

    msg_lines = [f"🎉 <b>一鱼多吃 Pipeline 完成</b>", f"时间：{datetime.now().strftime('%H:%M')}"]
    for fname, ok, xhs_title, title in success:
        msg_lines.append(f"\n✅ <b>{title}</b>")
        msg_lines.append(f"  📝 博客已同步（中+英文）")
        if xhs_title:
            msg_lines.append(f"  📱 小红书草稿：{xhs_title}")
        msg_lines.append(f"  👉 记得去 NoteToMp 发布公众号")
    for fname, ok, _, reason in failed:
        msg_lines.append(f"\n❌ {fname}：{reason}")

    notify("\n".join(msg_lines))
    print("\n" + "\n".join(msg_lines))


if __name__ == "__main__":
    main()
