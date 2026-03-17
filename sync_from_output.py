#!/usr/bin/env python3
"""
博客同步脚本 v3.0
源目录：vault/archive/公众号文章/
已发布判断：slug 或 title 已存在于 content/posts/ → 跳过
新文章：生成 slug.zh.md + 英文翻译 slug.en.md + 封面
"""

import os, re, shutil, subprocess, json, sys
from datetime import date
import yaml

VAULT = "/opt/my-obsidian-vault"
BLOG = "/opt/charlotteailab-blog"
ARCHIVE_DIR = os.path.join(VAULT, "archive", "公众号文章")
POSTS = os.path.join(BLOG, "content", "posts")
IMAGES = os.path.join(BLOG, "static", "images")

# ─────────────────────────────────────────────
# Slug 映射（关键词 → slug）
# ─────────────────────────────────────────────
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
    "龙虾经济学": "openclaw-26",
    "月入26万": "openclaw-26",
    "ChatGPT到底有什么区别": "chatgpt",
    "ChatGPT有什么区别": "chatgpt",
    "龙虾和ChatGPT": "chatgpt",
    "安全避坑": "openclaw-safety",
    "穷鬼方案": "openclaw-budget",
    "30元": "openclaw-budget",
    "不会用": "openclaw-newbie",
    "新手必做": "openclaw-newbie",
    "小红书封杀": "xiaohongshu-ban",
    "腾讯阿里字节": "bigtech-openclaw",
    "Claude升级": "claude-1m-token",
    "100万token": "claude-1m-token",
    "AI真的要攻克癌症": "ai-cancer",
    "AI翻了我一年账单": "ai-bill-analysis",
    "账单发现隐形消费": "ai-bill-analysis",
    "AI救狗": "ai-dog-vaccine",
    "AI对他说，死亡": "google-ai-death",
    "谢谢": "ai-thank-you",
    "豆包": "doubao-shopping",
    "AI简历筛选": "ai-resume-screening",
    "Meta裁员": "meta-layoffs",
}


def make_slug(title, filename):
    """从标题或文件名生成 URL slug"""
    for key, slug in SLUG_MAP.items():
        if key in title or key in filename:
            return slug
    # fallback：去掉日期前缀，非ASCII → 连字符
    base = os.path.splitext(filename)[0]
    base = re.sub(r'^\d{4}-\d{2}-\d{2}_?', '', base)
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', base).strip('-').lower()
    if not slug or len(slug) < 3:
        slug = f"post-{date.today().isoformat()}"
    return slug


def parse_front_matter(filepath):
    """提取 YAML front matter + body"""
    with open(filepath, 'r', encoding='utf-8') as f:
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
    except Exception:
        fm = {}
    return fm, parts[2].strip()


def get_published_state():
    """
    返回 (published_slugs: set, published_titles: set)
    用于判断 archive 中的文章是否已发布到博客
    """
    slugs = set()
    titles = set()
    if not os.path.exists(POSTS):
        return slugs, titles
    for fname in os.listdir(POSTS):
        if not fname.endswith('.md'):
            continue
        # slug from filename
        slug = fname.replace('.zh.md', '').replace('.en.md', '').replace('.md', '')
        slugs.add(slug)
        # title from front matter
        fm, _ = parse_front_matter(os.path.join(POSTS, fname))
        t = fm.get('title', '')
        if t:
            titles.add(t)
    return slugs, titles


def convert_images(body, src_dir):
    """
    将 Obsidian 图片语法和相对路径图片转换为 Hugo /images/ 路径
    并把图片文件复制到 blog/static/images/
    """
    copied = []

    def replace_obsidian_embed(m):
        fname = m.group(1)
        safe_fname = fname.replace(' ', '_')
        for root, dirs, files in os.walk(VAULT):
            if '.git' in root or 'node_modules' in root:
                continue
            for f in files:
                if f == fname or f.replace(' ', '_') == safe_fname:
                    src_path = os.path.join(root, f)
                    dst = os.path.join(IMAGES, safe_fname)
                    if not os.path.exists(dst):
                        shutil.copy2(src_path, dst)
                        copied.append(safe_fname)
                    return f'![](/images/{safe_fname})'
        return ''

    body = re.sub(r'!\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]', replace_obsidian_embed, body)

    def replace_md_image(m):
        alt, path = m.group(1), m.group(2)
        if path.startswith('http') or path.startswith('/images/'):
            return m.group(0)
        fname = os.path.basename(path).replace(' ', '_')
        # 先找相对路径，再全库搜索
        candidates = [os.path.join(src_dir, path), os.path.join(VAULT, path)]
        for c in candidates:
            if os.path.exists(c):
                dst = os.path.join(IMAGES, fname)
                if not os.path.exists(dst):
                    shutil.copy2(c, dst)
                    copied.append(fname)
                return f'![{alt}](/images/{fname})'
        return f'![{alt}](/images/{fname})'

    body = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_md_image, body)
    body = re.sub(r'> \[!(note|tip|warning|important)\][^\n]*\n', '> ', body)
    return body, copied


def find_cover(slug, title, fm, src_path):
    """
    按优先级查找封面图，返回 (hugo_path, local_src_path) 或 ('', '')
    """
    cover_fm = fm.get('cover', '')
    archive_img_dir = os.path.join(VAULT, "archive", "images")
    src_dir = os.path.dirname(src_path)

    # 候选路径列表
    candidates = []

    # 1. archive/images/<title>/cover.png
    for candidate_title in [title, os.path.splitext(os.path.basename(src_path))[0]]:
        d = os.path.join(archive_img_dir, candidate_title)
        candidates.append(os.path.join(d, "cover.png"))
        candidates.append(os.path.join(d, "cover.jpg"))
        if cover_fm:
            candidates.append(os.path.join(d, os.path.basename(cover_fm)))

    # 2. archive/images 子目录模糊匹配
    if os.path.exists(archive_img_dir):
        for d in sorted(os.listdir(archive_img_dir)):
            if d in title or title in d:
                candidates.append(os.path.join(archive_img_dir, d, "cover.png"))
                candidates.append(os.path.join(archive_img_dir, d, "cover.jpg"))

    # 3. front matter 指定路径
    if cover_fm:
        candidates.append(os.path.join(src_dir, cover_fm))
        candidates.append(os.path.join(VAULT, cover_fm))

    for path in candidates:
        if os.path.exists(path):
            cover_fname = f"cover_{slug}.png"
            dst = os.path.join(IMAGES, cover_fname)
            if not os.path.exists(dst):
                shutil.copy2(path, dst)
            return f"/images/{cover_fname}", path

    return '', ''


def geo_description(title, summary, body):
    """生成 AI 搜索友好的 description"""
    if summary:
        desc = summary
        if not desc.endswith(('。', '！', '？', '.', '!', '?')):
            desc += '。'
        return desc[:200]
    for line in body.split('\n'):
        line = line.strip()
        if (line and not line.startswith(('#', '!', '>', '-', '```'))
                and len(line) > 40):
            desc = line[:200]
            if not desc.endswith(('。', '！', '？', '.', '!', '?')):
                desc += '。'
            return desc
    return f"{title}。"


def generate_faq(title, body):
    """从正文标题提取 FAQ"""
    faqs = []
    for line in body.split('\n'):
        line = line.strip()
        if line.startswith('#') and ('？' in line or '?' in line):
            q = re.sub(r'^#+\s*', '', line).strip()
            idx = body.find(line)
            remaining = body[idx + len(line):]
            ans = []
            for al in remaining.split('\n'):
                al = al.strip()
                if not al or al.startswith('#'):
                    break
                if not al.startswith(('!', '>')):
                    ans.append(al)
            if ans:
                a = ' '.join(ans[:3])[:300]
                faqs.append({"q": q, "a": a})
    return faqs[:5]


def write_zh_post(slug, title, article_date, description, summary, tags,
                  cover_slug, body):
    """写中文版博客文章"""
    dest = os.path.join(POSTS, f"{slug}.zh.md")

    char_count = len(re.sub(r'\s+', '', body))
    reading_time = max(1, round(char_count / 400))
    keywords = list(tags) if tags else []
    for kw in ['AI', 'OpenClaw', '龙虾']:
        if kw.lower() in title.lower() and kw not in keywords:
            keywords.append(kw)
    og_image = cover_slug
    if not og_image:
        m = re.search(r'!\[.*?\]\((/images/[^)]+)\)', body)
        if m:
            og_image = m.group(1)
    faq_items = generate_faq(title, body)

    with open(dest, 'w', encoding='utf-8') as f:
        f.write("---\n")
        # 用双引号包裹 title，避免单引号 YAML 解析错误
        safe_title = title.replace('"', '\\"')
        f.write(f'title: "{safe_title}"\n')
        f.write(f"date: {article_date}\n")
        if description:
            safe_desc = description.replace('"', '\\"')
            f.write(f'description: "{safe_desc}"\n')
        if summary:
            safe_sum = summary.replace('"', '\\"')
            f.write(f'summary: "{safe_sum}"\n')
        f.write(f"tags: {json.dumps(tags, ensure_ascii=False)}\n")
        if keywords:
            f.write(f"keywords: {json.dumps(keywords, ensure_ascii=False)}\n")
        if cover_slug:
            f.write(f'cover: "{cover_slug}"\n')
        if og_image:
            f.write(f"images: [\"{og_image}\"]\n")
        f.write(f"readingTime: {reading_time}\n")
        f.write(f'slug: "{slug}"\n')
        if faq_items:
            f.write("faq:\n")
            for faq in faq_items:
                q = faq['q'].replace('"', '\\"')
                a = faq['a'].replace('"', '\\"')
                f.write(f'  - q: "{q}"\n')
                f.write(f'    a: "{a}"\n')
        f.write("---\n\n")
        f.write(body)
        f.write("\n")

    return dest


def translate_to_english(zh_title, zh_body, tags):
    """
    调用 Gemini Pro API 翻译中文文章为英文
    返回 (en_title, en_body, en_description)
    """
    import urllib.request
    import urllib.error

    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        return None, None, None

    # 截断正文以节省 token（最多 8000 字）
    body_to_translate = zh_body[:8000]

    prompt = f"""You are a professional translator. Translate the following Chinese blog article to natural, engaging English.

Requirements:
1. Title: translate to catchy English title (not literal), suitable for Western readers
2. Body: translate the full article naturally. Keep markdown formatting (headings, bold, lists, code blocks)
3. Description: write a 1-2 sentence English description summarizing the article for SEO
4. COVER_TITLE: write a short punchy English cover title (max 6 words, ALL CAPS for visual impact)

Return ONLY a JSON object with these keys: "title", "body", "description", "cover_title"
No extra text outside the JSON.

Chinese title: {zh_title}

Chinese body:
{body_to_translate}
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    payload = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.3, "maxOutputTokens": 8192}
    }).encode('utf-8')

    req = urllib.request.Request(url, data=payload,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode())
        text = data['candidates'][0]['content']['parts'][0]['text'].strip()
        # 去掉 markdown code fences
        text = re.sub(r'^```json\s*', '', text)
        text = re.sub(r'\s*```$', '', text)
        result = json.loads(text)
        return result.get('title', ''), result.get('body', ''), result.get('description', ''), result.get('cover_title', '')
    except Exception as e:
        print(f"  ⚠️ 翻译API失败: {e}")
        return None, None, None, None


def write_en_post(slug, en_title, article_date, en_description, tags,
                  cover_slug, en_body, cover_title=''):
    """写英文版博客文章"""
    dest = os.path.join(POSTS, f"{slug}.en.md")

    char_count = len(en_body.split())
    reading_time = max(1, round(char_count / 200))

    # 英文封面图
    en_cover_slug = ''
    en_cover_file = os.path.join(IMAGES, f"cover_{slug}_en.png")
    if os.path.exists(en_cover_file):
        en_cover_slug = f"/images/cover_{slug}_en.png"
    elif cover_slug:
        en_cover_slug = cover_slug  # 暂用中文封面

    with open(dest, 'w', encoding='utf-8') as f:
        f.write("---\n")
        safe_title = en_title.replace('"', '\\"')
        f.write(f'title: "{safe_title}"\n')
        f.write(f"date: {article_date}\n")
        if en_description:
            safe_desc = en_description.replace('"', '\\"')
            f.write(f'description: "{safe_desc}"\n')
        f.write(f"tags: {json.dumps(tags, ensure_ascii=False)}\n")
        if en_cover_slug:
            f.write(f'cover: "{en_cover_slug}"\n')
            f.write(f'images: ["{en_cover_slug}"]\n')
        f.write(f"readingTime: {reading_time}\n")
        f.write(f'slug: "{slug}"\n')
        if cover_title:
            f.write(f"<!-- COVER_TITLE: {cover_title} -->\n")
        f.write("---\n\n")
        f.write(en_body)
        f.write("\n")

    return dest


def main():
    if not os.path.exists(ARCHIVE_DIR):
        print(f"❌ 源目录不存在: {ARCHIVE_DIR}")
        sys.exit(1)

    os.makedirs(POSTS, exist_ok=True)
    os.makedirs(IMAGES, exist_ok=True)

    published_slugs, published_titles = get_published_state()

    new_count = 0
    skipped = 0
    translated = 0

    all_files = sorted(f for f in os.listdir(ARCHIVE_DIR) if f.endswith('.md'))
    print(f"📂 源目录: {ARCHIVE_DIR}")
    print(f"📊 共 {len(all_files)} 篇文章，博客已有 {len(published_slugs)//2} 篇\n")

    for fname in all_files:
        src_path = os.path.join(ARCHIVE_DIR, fname)
        fm, body = parse_front_matter(src_path)

        # 获取标题
        title = fm.get('title', '') or fm.get('标题', '')
        if not title:
            title = os.path.splitext(fname)[0]
            title = re.sub(r'^\d{4}-\d{2}-\d{2}_?', '', title)

        slug = make_slug(title, fname)

        # ─── 已发布判断 ───
        if slug in published_slugs or title in published_titles:
            skipped += 1
            continue

        print(f"🆕 新文章: {title}")
        print(f"   slug: {slug}")

        # 元数据
        summary = fm.get('summary', '') or fm.get('摘要', '') or ''
        tags = fm.get('tags', [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(',')]
        if not isinstance(tags, list):
            tags = []
        article_date = fm.get('date', date.today().isoformat())
        if hasattr(article_date, 'isoformat'):
            article_date = article_date.isoformat()

        # 处理图片
        body, copied_images = convert_images(body, os.path.dirname(src_path))
        for img in copied_images:
            print(f"   📷 图片: {img}")

        # 封面
        cover_slug, cover_src = find_cover(slug, title, fm, src_path)
        if cover_src:
            print(f"   🖼️  封面: {cover_src}")

        # description
        description = geo_description(title, summary, body)

        # ─── 写中文版 ───
        write_zh_post(slug, title, article_date, description, summary, tags,
                      cover_slug, body)
        print(f"   ✅ {slug}.zh.md")

        # ─── 英文翻译 ───
        en_title, en_body, en_description, cover_title = translate_to_english(title, body, tags)

        if en_title and en_body:
            write_en_post(slug, en_title, article_date, en_description or '',
                          tags, cover_slug, en_body, cover_title or '')
            print(f"   🌐 {slug}.en.md  ({en_title})")
            translated += 1
        else:
            print(f"   ⚠️ 英文翻译失败，请手动翻译: {slug}")

        new_count += 1
        print()

    # ─── 检查现有文章缺少英文版 ───
    zh_posts = {f.replace('.zh.md', '') for f in os.listdir(POSTS) if f.endswith('.zh.md')}
    en_posts = {f.replace('.en.md', '') for f in os.listdir(POSTS) if f.endswith('.en.md')}
    missing_en = zh_posts - en_posts
    if missing_en:
        print(f"⚠️  {len(missing_en)} 篇中文文章缺少英文版: {', '.join(sorted(missing_en))}")

    print(f"\n📊 同步完成: 新增 {new_count} 篇（{translated} 篇已翻译），跳过已发布 {skipped} 篇")

    if new_count == 0:
        print("✅ 源目录无新文章，博客已是最新状态")
        return

    # ─── 构建验证 ───
    print("\n🔨 验证 Hugo 构建...")
    result = subprocess.run(
        ["hugo", "--minify"],
        capture_output=True, text=True, cwd=BLOG
    )
    if result.returncode != 0:
        print(f"❌ Hugo 构建失败，不推送！\n{result.stderr[-2000:]}")
        sys.exit(1)
    print("✅ Hugo 构建通过")

    # ─── Git push ───
    os.chdir(BLOG)
    subprocess.run(["git", "add", "-A"], check=True)
    commit_result = subprocess.run(
        ["git", "commit", "-m", f"sync: 从archive新增{new_count}篇文章（{translated}篇含英文版）"],
        capture_output=True, text=True
    )
    if commit_result.returncode == 0:
        push_result = subprocess.run(
            ["git", "push", "origin", "main"],
            capture_output=True, text=True
        )
        if push_result.returncode == 0:
            print("🚀 已推送，等待 Cloudflare Pages 构建")
        else:
            print(f"⚠️  push 失败: {push_result.stderr}")
    else:
        print("ℹ️  无变更需要 commit")


if __name__ == "__main__":
    main()
