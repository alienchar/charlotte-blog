#!/bin/bash
# 博客同步脚本：03_Output → charlotteailab-blog
# 扫描新文章，转换格式，复制图片，push到GitHub
set -e

VAULT="/opt/my-obsidian-vault"
BLOG="/opt/charlotteailab-blog"
OUTPUT="$VAULT/03_Output"
POSTS="$BLOG/content/posts"
IMAGES="$BLOG/static/images"

# Mapping: 03_Output filename → blog slug
# We match by comparing titles in existing blog posts
get_existing_titles() {
  for f in "$POSTS"/*.md; do
    [ -f "$f" ] || continue
    grep -m1 "^title:" "$f" | sed "s/^title: *['\"]*//" | sed "s/['\"]$//"
  done
}

EXISTING_TITLES=$(get_existing_titles)
NEW_COUNT=0

for src in "$OUTPUT"/*.md; do
  [ -f "$src" ] || continue
  
  # Extract title from source
  SRC_TITLE=$(grep -m1 "^title:" "$src" | sed "s/^title: *['\"]*//" | sed "s/['\"]$//" || basename "$src" .md)
  
  # Check if already exists (fuzzy match on title)
  FOUND=0
  while IFS= read -r existing; do
    if [ "$existing" = "$SRC_TITLE" ]; then
      FOUND=1
      break
    fi
  done <<< "$EXISTING_TITLES"
  
  if [ "$FOUND" = "1" ]; then
    continue
  fi
  
  echo "📝 新文章发现: $SRC_TITLE"
  
  # Generate slug from filename
  BASENAME=$(basename "$src" .md)
  # Remove date prefix if exists
  SLUG=$(echo "$BASENAME" | sed 's/^[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}_//')
  # Transliterate to safe slug (keep as-is for Chinese, will work with Hugo)
  SLUG_SAFE=$(echo "$SLUG" | tr ' ' '-' | tr '[:upper:]' '[:lower:]' | sed 's/[^a-zA-Z0-9\u4e00-\u9fff_-]/-/g' | sed 's/--*/-/g' | sed 's/^-//' | sed 's/-$//')
  
  # Extract front matter fields
  SUMMARY=$(grep -m1 "^summary:" "$src" | sed "s/^summary: *['\"]*//" | sed "s/['\"]$//" || echo "")
  [ -z "$SUMMARY" ] && SUMMARY=$(grep -m1 "^摘要:" "$src" | sed "s/^摘要: *['\"]*//" | sed "s/['\"]$//" || echo "")
  
  TAGS=$(python3 -c "
import yaml, sys, json
with open('$src') as f:
    content = f.read()
if '---' in content:
    fm = content.split('---')[1]
    data = yaml.safe_load(fm)
    tags = data.get('tags', [])
    if isinstance(tags, list):
        print(json.dumps(tags))
    else:
        print('[]')
else:
    print('[]')
" 2>/dev/null || echo '[]')
  
  DATE=$(python3 -c "
import yaml
with open('$src') as f:
    content = f.read()
if '---' in content:
    fm = content.split('---')[1]
    data = yaml.safe_load(fm)
    print(data.get('date', '$(date +%Y-%m-%d)'))
else:
    print('$(date +%Y-%m-%d)')
" 2>/dev/null || date +%Y-%m-%d)
  
  # Extract body (after front matter)
  BODY=$(python3 -c "
import sys
with open('$src') as f:
    content = f.read()
parts = content.split('---', 2)
if len(parts) >= 3:
    body = parts[2].strip()
else:
    body = content
# Remove Obsidian image embeds and convert to Hugo format
import re
# Convert ![[filename.png]] to ![](/images/filename.png)
body = re.sub(r'!\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]', lambda m: '![](' + '/images/' + m.group(1).replace(' ', '_') + ')', body)
# Convert ![alt](relative/path) to ![alt](/images/filename)
def fix_img(m):
    alt = m.group(1)
    path = m.group(2)
    if path.startswith('http') or path.startswith('/images/'):
        return m.group(0)
    import os
    fname = os.path.basename(path).replace(' ', '_')
    return f'![{alt}](/images/{fname})'
body = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', fix_img, body)
# Remove Obsidian note blocks > [!note]
body = re.sub(r'> \[!note\][^\n]*\n', '', body)
print(body)
" 2>/dev/null)
  
  # Copy images
  # Find all image references in source
  python3 -c "
import re, os, shutil
with open('$src') as f:
    content = f.read()
# Find Obsidian embeds ![[file.png]]
for m in re.findall(r'!\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]', content):
    fname = m.replace(' ', '_')
    # Search in vault
    for root, dirs, files in os.walk('$VAULT'):
        for f in files:
            if f.replace(' ', '_') == fname or f == m:
                src_path = os.path.join(root, f)
                dst_path = os.path.join('$IMAGES', fname)
                if not os.path.exists(dst_path):
                    shutil.copy2(src_path, dst_path)
                    print(f'  📷 复制图片: {fname}')
                break

# Find markdown images ![](path)
for m in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', content):
    if m.startswith('http') or m.startswith('/images/'):
        continue
    full_path = os.path.join(os.path.dirname('$src'), m) if not os.path.isabs(m) else m
    if not os.path.isabs(full_path):
        full_path = os.path.join('$VAULT', m)
    fname = os.path.basename(m).replace(' ', '_')
    dst_path = os.path.join('$IMAGES', fname)
    if os.path.exists(full_path) and not os.path.exists(dst_path):
        shutil.copy2(full_path, dst_path)
        print(f'  📷 复制图片: {fname}')
" 2>/dev/null
  
  # Copy cover image if exists
  COVER_SRC=$(python3 -c "
import yaml, os
with open('$src') as f:
    content = f.read()
if '---' in content:
    fm = content.split('---')[1]
    data = yaml.safe_load(fm)
    cover = data.get('cover', '')
    if cover and not cover.startswith('http'):
        # Resolve relative to article location or vault
        for base in [os.path.dirname('$src'), '$VAULT']:
            full = os.path.join(base, cover)
            if os.path.exists(full):
                print(full)
                break
" 2>/dev/null)
  
  COVER_SLUG=""
  if [ -n "$COVER_SRC" ] && [ -f "$COVER_SRC" ]; then
    COVER_FNAME="cover_${SLUG_SAFE}.png"
    cp "$COVER_SRC" "$IMAGES/$COVER_FNAME" 2>/dev/null && COVER_SLUG="/images/$COVER_FNAME"
    echo "  📷 封面: $COVER_FNAME"
  fi
  
  # Write blog post
  DEST="$POSTS/${SLUG_SAFE}.md"
  {
    echo "---"
    echo "title: '$(echo "$SRC_TITLE" | sed "s/'/\\\\'/g")'"
    echo "date: $DATE"
    [ -n "$SUMMARY" ] && echo "summary: '$(echo "$SUMMARY" | sed "s/'/\\\\'/g")'"
    echo "tags: $TAGS"
    [ -n "$COVER_SLUG" ] && echo "cover: '$COVER_SLUG'"
    echo "---"
    echo ""
    echo "$BODY"
  } > "$DEST"
  
  echo "  ✅ 写入: $DEST"
  NEW_COUNT=$((NEW_COUNT + 1))
done

if [ "$NEW_COUNT" -eq 0 ]; then
  echo "✅ 无新文章需要同步"
  exit 0
fi

echo ""
echo "📊 共同步 $NEW_COUNT 篇新文章"

# Git push
cd "$BLOG"
git add -A
git commit -m "sync: 新增${NEW_COUNT}篇文章 from 03_Output" || true
git push origin main 2>&1 || echo "⚠️ push失败，请检查"

echo "🚀 已推送到GitHub，等待Cloudflare Pages构建"
