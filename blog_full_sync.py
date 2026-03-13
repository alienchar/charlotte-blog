#!/usr/bin/env python3
"""
博客全流程同步脚本 v1.0
1. 同步中文文章（sync_from_output.py）
2. 检测缺失英文翻译 → 调用Opus翻译
3. 从译文提取COVER_TITLE → 生成英文封面
4. 检查所有英文文章封面状态
5. Git push

用于cron每日自动运行。
"""

import os, re, subprocess, json, sys
from pathlib import Path

BLOG = "/opt/charlotteailab-blog"
POSTS = os.path.join(BLOG, "content", "posts")
IMAGES = os.path.join(BLOG, "static", "images")
MAKE_COVER_EN = "/root/.openclaw/workspace/obsidian-bridge/make_cover_en.py"
SYNC_SCRIPT = os.path.join(BLOG, "sync_from_output.py")
WRITING_SKILL = "/opt/my-obsidian-vault/04_System/Skills/夏洛特写作Skill.md"
STYLE_CORPUS = "/opt/my-obsidian-vault/04_System/Skills/夏洛特风格语料库.md"
BLOG_SKILL = "/opt/my-obsidian-vault/04_System/Skills/博客同步与英文版Skill.md"

# Translation rules (from 博客同步与英文版Skill.md)
TRANSLATION_SYSTEM_PROMPT = """你是Charlotte的博客翻译助手。将中文博客文章翻译为英文版。

翻译规范：
1. 风格：口语化博客英文，像一个真人blogger在写英文博客
2. 语气：保持Charlotte的直接、有观点、偶尔幽默的语气
3. 中国特有概念：保留拼音+英文解释（搜一搜→"Sou Yi Sou (WeChat Search)"，小红书→Xiaohongshu）
4. 皮皮虾：首次出场"my AI assistant (a lobster named PiPiXia)"，后续直接用PiPiXia
5. 产品名：OpenClaw/Obsidian/Claude/Meta等保持英文
6. 不逐句翻译，意译，英文读起来自然流畅
7. 标题：重新拟定适合英文读者的标题，不必直译
8. YAML值用双引号包裹（避免撇号破坏YAML）
9. blockquote里不加引号（主题自动加装饰引号）
10. 正文开头不放封面图

在译文末尾必须输出英文封面标题（不是翻译中文标题，而是通读全文后提炼有冲击力的英文短句）：
<!-- COVER_TITLE: Line 1 / Line 2 / Line 3 -->
每行3-4个英文单词，2-4行，要有情绪张力。"""


def run_sync():
    """Step 1: Run sync_from_output.py"""
    print("=" * 50)
    print("📝 Step 1: 同步中文文章")
    print("=" * 50)
    result = subprocess.run(
        ["python3", SYNC_SCRIPT],
        capture_output=True, text=True, cwd=BLOG
    )
    print(result.stdout)
    if result.stderr:
        print(f"STDERR: {result.stderr}")
    return result.returncode == 0


def find_missing_translations():
    """Step 2: Find Chinese posts without English translations"""
    zh_posts = {}
    en_slugs = set()

    for f in os.listdir(POSTS):
        if f.endswith('.zh.md'):
            slug = f.replace('.zh.md', '')
            zh_posts[slug] = os.path.join(POSTS, f)
        elif f.endswith('.en.md'):
            slug = f.replace('.en.md', '')
            en_slugs.add(slug)

    missing = {slug: path for slug, path in zh_posts.items() if slug not in en_slugs}
    return missing


def translate_article(slug, zh_path):
    """Translate a single article using Anthropic Opus API directly"""
    import anthropic

    print(f"\n  🔄 翻译: {slug}")

    with open(zh_path, 'r') as f:
        zh_content = f.read()

    # Extract frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---\n(.*)$', zh_content, re.DOTALL)
    if not fm_match:
        print(f"  ❌ 无法解析frontmatter: {slug}")
        return None

    fm_text = fm_match.group(1)
    body = fm_match.group(2)

    # Extract date and tags from Chinese version
    date_match = re.search(r'date:\s*(\S+)', fm_text)
    article_date = date_match.group(1) if date_match else ""
    
    cover_match = re.search(r"cover:\s*'([^']*)'", fm_text)
    cn_cover = cover_match.group(1) if cover_match else ""

    # Prepare EN cover path
    en_cover = cn_cover.replace(f'cover_{slug}.png', f'cover_{slug}_en.png') if cn_cover else ""

    prompt = f"""请翻译以下中文博客文章为英文版。

输出格式要求：
1. 以 --- 开头的YAML front matter（包含title, date, description, summary, tags, keywords, cover, images, readingTime, slug）
2. date保持: {article_date}
3. cover设为: '{en_cover}'（如果有的话）
4. images设为: ['{en_cover}']（如果有的话）
5. slug保持: '{slug}'
6. 然后是翻译后的正文
7. 最后一行必须是 <!-- COVER_TITLE: Line1 / Line2 --> 格式

中文原文：
{zh_content}"""

    try:
        # Read API key from OpenClaw auth profiles
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            auth_file = os.path.expanduser("~/.openclaw/agents/main/agent/auth-profiles.json")
            if os.path.exists(auth_file):
                with open(auth_file) as af:
                    auth = json.load(af)
                profile = auth.get("profiles", {}).get("anthropic:manual", {})
                api_key = profile.get("token") or profile.get("key")
        
        if not api_key:
            print("  ❌ 未找到Anthropic API key")
            return None

        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=8000,
            system=TRANSLATION_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}]
        )

        en_content = response.content[0].text
        
        # Save English version
        en_path = os.path.join(POSTS, f"{slug}.en.md")
        with open(en_path, 'w') as f:
            f.write(en_content)

        print(f"  ✅ 已保存: {slug}.en.md")

        # Extract COVER_TITLE
        cover_match = re.search(r'<!-- COVER_TITLE:\s*(.+?)\s*-->', en_content)
        if cover_match:
            cover_lines = [line.strip() for line in cover_match.group(1).split('/')]
            print(f"  📝 封面标题: {' | '.join(cover_lines)}")
            return cover_lines
        else:
            print(f"  ⚠️ 未找到COVER_TITLE注释")
            return None

    except Exception as e:
        print(f"  ❌ 翻译失败: {e}")
        return None


def generate_en_cover(slug, title_lines):
    """Generate English cover image"""
    cn_cover = os.path.join(IMAGES, f"cover_{slug}.png")
    en_cover = os.path.join(IMAGES, f"cover_{slug}_en.png")

    if not os.path.exists(cn_cover):
        print(f"  ⚠️ 中文封面不存在: {cn_cover}")
        return False

    # Build command - use single quotes for lines with $
    cmd = ["python3", MAKE_COVER_EN, "--illus", cn_cover, "--title"] + title_lines + ["--output", en_cover]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"  ✅ 英文封面: cover_{slug}_en.png")
        return True
    else:
        print(f"  ❌ 封面生成失败: {result.stderr}")
        return False


def check_en_cover_references():
    """Step 4: Check all EN posts have correct cover references"""
    print("\n" + "=" * 50)
    print("🔍 Step 4: 检查英文封面状态")
    print("=" * 50)
    
    fixes = 0
    missing = 0
    
    for f in sorted(os.listdir(POSTS)):
        if not f.endswith('.en.md'):
            continue
        slug = f.replace('.en.md', '')
        en_path = os.path.join(POSTS, f)
        en_cover_file = os.path.join(IMAGES, f"cover_{slug}_en.png")
        cn_cover_file = os.path.join(IMAGES, f"cover_{slug}.png")

        with open(en_path, 'r') as fh:
            content = fh.read()

        if os.path.exists(en_cover_file):
            expected = f"/images/cover_{slug}_en.png"
            if expected not in content:
                # Fix reference
                # Replace cover line
                content = re.sub(
                    r"cover:\s*'[^']*'",
                    f"cover: '{expected}'",
                    content
                )
                content = re.sub(
                    r'cover:\s*"[^"]*"',
                    f"cover: '{expected}'",
                    content
                )
                content = re.sub(
                    r"images:\s*\['[^']*'\]",
                    f"images: ['{expected}']",
                    content
                )
                content = re.sub(
                    r'images:\s*\["[^"]*"\]',
                    f"images: ['{expected}']",
                    content
                )
                with open(en_path, 'w') as fh:
                    fh.write(content)
                print(f"  🔗 {slug} → 更新封面引用为_en版本")
                fixes += 1
        elif os.path.exists(cn_cover_file):
            print(f"  ⚠️ {slug}: 缺少英文封面")
            missing += 1

    if fixes:
        print(f"\n  📷 修复了 {fixes} 篇封面引用")
    if missing:
        print(f"  ⚠️ {missing} 篇缺少英文封面")
    if not fixes and not missing:
        print("  ✅ 所有英文文章封面状态正常")


def git_push(msg):
    """Git add, commit, push"""
    os.chdir(BLOG)
    subprocess.run(["git", "add", "-A"], check=True)
    result = subprocess.run(
        ["git", "commit", "-m", msg],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        push = subprocess.run(
            ["git", "push", "origin", "main"],
            capture_output=True, text=True
        )
        if push.returncode == 0:
            print("🚀 已推送，等待Cloudflare Pages构建")
        else:
            print(f"⚠️ push失败: {push.stderr}")
    else:
        print("ℹ️ 无变更需要commit")


def main():
    print("🔄 博客全流程同步开始\n")

    # Step 1: Sync Chinese articles
    run_sync()

    # Step 2: Find & translate missing English versions
    missing = find_missing_translations()
    translated = 0
    covers_generated = 0

    if missing:
        print("\n" + "=" * 50)
        print(f"🌐 Step 2: 翻译 {len(missing)} 篇缺失英文版")
        print("=" * 50)

        for slug, zh_path in sorted(missing.items()):
            cover_lines = translate_article(slug, zh_path)
            if cover_lines:
                translated += 1
                # Step 3: Generate EN cover
                if generate_en_cover(slug, cover_lines):
                    covers_generated += 1
    else:
        print("\n✅ Step 2: 所有文章已有英文版")

    # Step 4: Check all EN cover references
    check_en_cover_references()

    # Step 5: Git push if changes
    changes = []
    if translated:
        changes.append(f"翻译{translated}篇")
    if covers_generated:
        changes.append(f"生成{covers_generated}张英文封面")
    
    if changes:
        print("\n" + "=" * 50)
        print("📦 Step 5: 提交推送")
        print("=" * 50)
        git_push(f"sync: {', '.join(changes)}")
    else:
        # Still push in case sync or cover fixes made changes
        print("\n" + "=" * 50)
        print("📦 Step 5: 检查变更")
        print("=" * 50)
        git_push("sync: 日常检查")

    # Summary
    print("\n" + "=" * 50)
    print("📊 同步完成")
    if translated:
        print(f"  🌐 新翻译: {translated} 篇")
    if covers_generated:
        print(f"  🎨 新封面: {covers_generated} 张")
    print("=" * 50)


if __name__ == "__main__":
    main()
