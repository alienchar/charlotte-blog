#!/usr/bin/env python3
"""博客同步脚本：03_Output → charlotteailab-blog"""

import os, re, shutil, subprocess, yaml, json
from datetime import date

VAULT = "/opt/my-obsidian-vault"
BLOG = "/opt/charlotteailab-blog"
OUTPUT = os.path.join(VAULT, "03_Output")
POSTS = os.path.join(BLOG, "content", "posts")
IMAGES = os.path.join(BLOG, "static", "images")

# Slug mapping for Chinese titles
SLUG_MAP = {
    "Anthropic": "anthropic-ai-jobs",
    "Karpathy": "karpathy-ai-researcher",
    "3分钟看懂": "openclaw-3min",
    "20件事": "openclaw-20-things",
    "Obsidian": "openclaw-obsidian",
    "3类Skill": "openclaw-skills",
    "部署指南": "openclaw-deploy-guide",
    "龙虾部署": "openclaw-deploy-guide",
    "花多少钱": "openclaw-cost",
    "Dan Koe": "dan-koe-future-of-work",
    "杨立昆": "lecun-llm-doomed",
    "融资10亿": "lecun-llm-doomed",
    "谷歌被告": "google-ai-death",
    "马斯克": "musk-7-years",
}

def make_slug(title, filename):
    """Generate URL-safe slug from title or filename"""
    # Try mapping first
    for key, slug in SLUG_MAP.items():
        if key in title or key in filename:
            return slug
    # Fallback: use filename, strip date prefix, transliterate
    base = os.path.splitext(filename)[0]
    base = re.sub(r'^\d{4}-\d{2}-\d{2}_?', '', base)
    # Simple transliteration: keep ascii, replace rest with hyphens
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', base).strip('-').lower()
    if not slug:
        slug = f"post-{date.today().isoformat()}"
    return slug

def parse_front_matter(filepath):
    """Extract front matter from markdown file"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    if not content.startswith('---'):
        return {}, content
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content
    
    try:
        fm = yaml.safe_load(parts[1])
        if not isinstance(fm, dict):
            fm = {}
    except:
        fm = {}
    
    body = parts[2].strip()
    return fm, body

def convert_images(body, src_dir):
    """Convert Obsidian image syntax to Hugo and copy files"""
    copied = []
    
    # ![[filename.png]] or ![[filename.png|alt]]
    def replace_obsidian_embed(m):
        fname = m.group(1)
        safe_fname = fname.replace(' ', '_')
        # Search for file in vault
        for root, dirs, files in os.walk(VAULT):
            # Skip .git and node_modules
            if '.git' in root or 'node_modules' in root:
                continue
            for f in files:
                if f == fname or f.replace(' ', '_') == safe_fname:
                    src_path = os.path.join(root, f)
                    dst_path = os.path.join(IMAGES, safe_fname)
                    if not os.path.exists(dst_path):
                        shutil.copy2(src_path, dst_path)
                        copied.append(safe_fname)
                    return f'![](/images/{safe_fname})'
        return ''  # Image not found, remove embed
    
    body = re.sub(r'!\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]', replace_obsidian_embed, body)
    
    # ![alt](relative/path) → ![alt](/images/filename)
    def replace_md_image(m):
        alt, path = m.group(1), m.group(2)
        if path.startswith('http') or path.startswith('/images/'):
            return m.group(0)
        fname = os.path.basename(path).replace(' ', '_')
        # Try to find the image
        for base in [src_dir, VAULT]:
            full = os.path.join(base, path)
            if os.path.exists(full):
                dst = os.path.join(IMAGES, fname)
                if not os.path.exists(dst):
                    shutil.copy2(full, dst)
                    copied.append(fname)
                return f'![{alt}](/images/{fname})'
        return f'![{alt}](/images/{fname})'
    
    body = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_md_image, body)
    
    # Clean up Obsidian callouts > [!note] → blockquote
    body = re.sub(r'> \[!(note|tip|warning|important)\][^\n]*\n', '> ', body)
    
    return body, copied

def get_existing_titles():
    """Get titles of existing blog posts"""
    titles = set()
    if not os.path.exists(POSTS):
        return titles
    for f in os.listdir(POSTS):
        if not f.endswith('.md'):
            continue
        filepath = os.path.join(POSTS, f)
        fm, _ = parse_front_matter(filepath)
        title = fm.get('title', '')
        if title:
            titles.add(title)
    return titles

def main():
    existing_titles = get_existing_titles()
    existing_slugs = {os.path.splitext(f)[0] for f in os.listdir(POSTS) if f.endswith('.md')}
    new_count = 0
    
    for fname in sorted(os.listdir(OUTPUT)):
        if not fname.endswith('.md'):
            continue
        
        src_path = os.path.join(OUTPUT, fname)
        fm, body = parse_front_matter(src_path)
        
        title = fm.get('title', '') or fm.get('标题', '')
        if not title:
            title = os.path.splitext(fname)[0]
        
        # Check if already exists
        if title in existing_titles:
            continue
        
        slug = make_slug(title, fname)
        if slug in existing_slugs:
            continue
        
        print(f"📝 新文章: {title}")
        
        # Extract metadata
        summary = fm.get('summary', '') or fm.get('摘要', '') or ''
        tags = fm.get('tags', [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(',')]
        article_date = fm.get('date', date.today().isoformat())
        if hasattr(article_date, 'isoformat'):
            article_date = article_date.isoformat()
        
        # Convert body
        src_dir = os.path.dirname(src_path)
        body, copied_images = convert_images(body, src_dir)
        for img in copied_images:
            print(f"  📷 {img}")
        
        # Handle cover image
        cover = fm.get('cover', '')
        cover_slug = ''
        if cover and not cover.startswith('http'):
            # Search multiple locations for cover image
            search_paths = [
                os.path.join(src_dir, cover),
                os.path.join(VAULT, cover),
            ]
            # Also search archive/images/ subdirectories
            archive_dir = os.path.join(VAULT, "archive", "images")
            if os.path.exists(archive_dir):
                for d in os.listdir(archive_dir):
                    search_paths.append(os.path.join(archive_dir, d, cover))
            
            for cover_path in search_paths:
                if os.path.exists(cover_path):
                    cover_fname = f"cover_{slug}.png"
                    shutil.copy2(cover_path, os.path.join(IMAGES, cover_fname))
                    cover_slug = f"/images/{cover_fname}"
                    print(f"  📷 封面: {cover_fname}")
                    break
        
        # SEO: generate description from summary or first paragraph
        description = summary
        if not description:
            # Take first meaningful paragraph (skip images, headers)
            for line in body.split('\n'):
                line = line.strip()
                if line and not line.startswith('#') and not line.startswith('!') and not line.startswith('>') and len(line) > 30:
                    description = line[:160]
                    break
        
        # SEO: generate keywords from tags + title
        keywords = list(tags) if tags else []
        for kw in ['AI', 'OpenClaw', '龙虾']:
            if kw.lower() in title.lower() and kw not in keywords:
                keywords.append(kw)
        
        # SEO: estimate reading time (Chinese ~400 chars/min)
        char_count = len(re.sub(r'\s+', '', body))
        reading_time = max(1, round(char_count / 400))
        
        # SEO: extract first image for og:image fallback
        og_image = cover_slug
        if not og_image:
            img_match = re.search(r'!\[.*?\]\((/images/[^)]+)\)', body)
            if img_match:
                og_image = img_match.group(1)
        
        # Write blog post (Chinese version)
        dest = os.path.join(POSTS, f"{slug}.zh.md")
        with open(dest, 'w') as f:
            f.write("---\n")
            f.write(f"title: '{title.replace(chr(39), chr(39)+chr(39))}'\n")
            f.write(f"date: {article_date}\n")
            if description:
                f.write(f"description: '{description.replace(chr(39), chr(39)+chr(39))}'\n")
            if summary:
                f.write(f"summary: '{summary.replace(chr(39), chr(39)+chr(39))}'\n")
            f.write(f"tags: {json.dumps(tags, ensure_ascii=False)}\n")
            if keywords:
                f.write(f"keywords: {json.dumps(keywords, ensure_ascii=False)}\n")
            if cover_slug:
                f.write(f"cover: '{cover_slug}'\n")
            if og_image:
                f.write(f"images: ['{og_image}']\n")
            f.write(f"readingTime: {reading_time}\n")
            f.write(f"slug: '{slug}'\n")
            f.write("---\n\n")
            f.write(body)
            f.write("\n")
        
        print(f"  ✅ {slug}.md")
        new_count += 1
    
    # Check for Chinese posts without English translations
    zh_posts = {f.replace('.zh.md', '') for f in os.listdir(POSTS) if f.endswith('.zh.md')}
    en_posts = {f.replace('.en.md', '') for f in os.listdir(POSTS) if f.endswith('.en.md')}
    missing_en = zh_posts - en_posts
    if missing_en:
        print(f"\n⚠️ {len(missing_en)}篇文章缺少英文版: {', '.join(sorted(missing_en))}")
        print("  请运行翻译子agent生成英文版")

    if new_count == 0:
        print("✅ 无新文章需要同步")
        return
    
    print(f"\n📊 共同步 {new_count} 篇新文章")
    
    # Git push
    os.chdir(BLOG)
    subprocess.run(["git", "add", "-A"], check=True)
    result = subprocess.run(["git", "commit", "-m", f"sync: 新增{new_count}篇文章"], capture_output=True, text=True)
    if result.returncode == 0:
        push_result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
        if push_result.returncode == 0:
            print("🚀 已推送，等待Cloudflare Pages构建")
        else:
            print(f"⚠️ push失败: {push_result.stderr}")
    else:
        print("ℹ️ 无变更需要commit")

if __name__ == "__main__":
    main()
