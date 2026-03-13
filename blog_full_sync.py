#!/usr/bin/env python3
"""
博客全流程同步脚本 v2.0
1. 同步中文文章（sync_from_output.py）
2. 检测缺失英文翻译 → 输出待翻译列表（由cron agent自己翻译）
3. 从已有译文提取COVER_TITLE → 生成英文封面
4. 检查所有英文文章封面状态
5. Git push

翻译由运行此脚本的LLM agent直接完成（Opus），不调用外部API。
脚本只负责机械操作（文件检测、封面合成、git）。
"""

import os, re, subprocess, json, sys
from pathlib import Path

BLOG = "/opt/charlotteailab-blog"
POSTS = os.path.join(BLOG, "content", "posts")
IMAGES = os.path.join(BLOG, "static", "images")
MAKE_COVER_EN = "/root/.openclaw/workspace/obsidian-bridge/make_cover_en.py"
SYNC_SCRIPT = os.path.join(BLOG, "sync_from_output.py")


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
    """Find Chinese posts without English translations"""
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


def find_en_without_cover_title():
    """Find EN posts that exist but don't have covers generated yet"""
    needs_cover = []
    for f in sorted(os.listdir(POSTS)):
        if not f.endswith('.en.md'):
            continue
        slug = f.replace('.en.md', '')
        en_cover = os.path.join(IMAGES, f"cover_{slug}_en.png")
        cn_cover = os.path.join(IMAGES, f"cover_{slug}.png")
        if not os.path.exists(en_cover) and os.path.exists(cn_cover):
            en_path = os.path.join(POSTS, f)
            with open(en_path) as fh:
                content = fh.read()
            cover_match = re.search(r'<!-- COVER_TITLE:\s*(.+?)\s*-->', content)
            if cover_match:
                lines = [l.strip() for l in cover_match.group(1).split('/')]
                needs_cover.append((slug, lines))
    return needs_cover


def generate_en_cover(slug, title_lines):
    """Generate English cover image"""
    cn_cover = os.path.join(IMAGES, f"cover_{slug}.png")
    en_cover = os.path.join(IMAGES, f"cover_{slug}_en.png")

    if not os.path.exists(cn_cover):
        print(f"  ⚠️ 中文封面不存在: {cn_cover}")
        return False

    cmd = ["python3", MAKE_COVER_EN, "--illus", cn_cover, "--title"] + title_lines + ["--output", en_cover]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"  ✅ 英文封面: cover_{slug}_en.png")
        return True
    else:
        print(f"  ❌ 封面生成失败: {result.stderr}")
        return False


def check_en_cover_references():
    """Check all EN posts have correct cover references"""
    print("\n" + "=" * 50)
    print("🔍 检查英文封面引用状态")
    print("=" * 50)
    
    fixes = 0
    for f in sorted(os.listdir(POSTS)):
        if not f.endswith('.en.md'):
            continue
        slug = f.replace('.en.md', '')
        en_path = os.path.join(POSTS, f)
        en_cover_file = os.path.join(IMAGES, f"cover_{slug}_en.png")

        if not os.path.exists(en_cover_file):
            continue

        with open(en_path, 'r') as fh:
            content = fh.read()

        expected = f"/images/cover_{slug}_en.png"
        if expected not in content:
            content = re.sub(r"cover:\s*'[^']*'", f"cover: '{expected}'", content)
            content = re.sub(r'cover:\s*"[^"]*"', f"cover: '{expected}'", content)
            content = re.sub(r"images:\s*\['[^']*'\]", f"images: ['{expected}']", content)
            content = re.sub(r'images:\s*\["[^"]*"\]', f"images: ['{expected}']", content)
            with open(en_path, 'w') as fh:
                fh.write(content)
            print(f"  🔗 {slug} → 更新封面引用")
            fixes += 1

    if not fixes:
        print("  ✅ 所有封面引用正常")


def git_push(msg):
    """Git add, commit, push"""
    os.chdir(BLOG)
    subprocess.run(["git", "add", "-A"], check=True)
    result = subprocess.run(["git", "commit", "-m", msg], capture_output=True, text=True)
    if result.returncode == 0:
        push = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
        if push.returncode == 0:
            print("🚀 已推送，等待Cloudflare Pages构建")
        else:
            print(f"⚠️ push失败: {push.stderr}")
    else:
        print("ℹ️ 无变更需要commit")


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "full"
    
    if mode == "sync-only":
        # Step 1 only: sync + detect missing
        run_sync()
        missing = find_missing_translations()
        if missing:
            print(f"\n⚠️ {len(missing)}篇缺英文版:")
            for slug, path in sorted(missing.items()):
                print(f"  - {slug}: {path}")
            print("\nTRANSLATION_NEEDED")
        else:
            print("\n✅ 所有文章已有英文版")
            print("NO_TRANSLATION_NEEDED")
        return

    elif mode == "post-translate":
        # After agent finishes translation: generate covers + fix refs + push
        covers = 0
        needs_cover = find_en_without_cover_title()
        if needs_cover:
            print("🎨 生成英文封面:")
            for slug, lines in needs_cover:
                if generate_en_cover(slug, lines):
                    covers += 1

        check_en_cover_references()

        changes = []
        if covers:
            changes.append(f"生成{covers}张英文封面")
        git_push(f"sync: {', '.join(changes)}" if changes else "sync: 日常检查")
        
        print(f"\n📊 完成: {covers}张新封面")
        return

    else:  # "full" mode — for backward compat, but translation is now agent's job
        print("🔄 博客全流程同步开始\n")
        run_sync()
        
        missing = find_missing_translations()
        if missing:
            print(f"\n⚠️ {len(missing)}篇缺英文版:")
            for slug, path in sorted(missing.items()):
                print(f"  - {slug}: {path}")
            print("\n⏳ 请cron agent翻译后运行: python3 blog_full_sync.py post-translate")
        else:
            print("\n✅ 所有文章已有英文版")

        # Still do covers for any EN posts missing them
        needs_cover = find_en_without_cover_title()
        if needs_cover:
            print("\n🎨 生成缺失的英文封面:")
            for slug, lines in needs_cover:
                generate_en_cover(slug, lines)

        check_en_cover_references()
        git_push("sync: 日常检查")
        print("\n📊 同步完成")


if __name__ == "__main__":
    main()
