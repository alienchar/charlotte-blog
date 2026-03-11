#!/usr/bin/env python3
"""批量补SEO+GEO字段到已有博客文章"""

import os, re, json, yaml

POSTS = "/opt/charlotteailab-blog/content/posts"

def parse_post(filepath):
    """Parse front matter and body"""
    with open(filepath, 'r') as f:
        content = f.read()
    if not content.startswith('---'):
        return None, content
    end = content.index('---', 3)
    fm_text = content[3:end].strip()
    body = content[end+3:].strip()
    fm = yaml.safe_load(fm_text) or {}
    return fm, body

def make_description(title, summary, body):
    """Generate AI-friendly description (complete answer sentence, not marketing)"""
    if summary:
        desc = summary.strip()
        if len(desc) > 50:
            return desc[:155].rstrip('，。！？、') + '。' if not desc[:155].endswith(('。','！','？')) else desc[:155]
    # Extract first meaningful paragraph
    for para in body.split('\n\n'):
        clean = re.sub(r'[#*>\[\]!()]', '', para).strip()
        if len(clean) > 30 and not clean.startswith('!['):
            return clean[:155].rstrip('，。！？、') + '。' if not clean[:155].endswith(('。','！','？')) else clean[:155]
    return title

def make_keywords(title, tags, is_en=False):
    """Generate keywords from title + tags"""
    kws = list(tags) if tags else []
    # Add common keywords
    for kw in ['AI', 'OpenClaw', '龙虾', 'Claude', 'GPT']:
        if kw.lower() in title.lower() and kw not in kws:
            kws.append(kw)
    if is_en:
        for kw in ['AI', 'artificial intelligence', 'OpenClaw']:
            if kw.lower() in title.lower() and kw not in kws:
                kws.append(kw)
    return kws

def make_faq(title, body, tags, is_en=False):
    """Generate 2-3 FAQ items based on content"""
    faqs = []
    
    # Strategy: extract key questions from the article structure
    # Look for headings that are questions or can be turned into questions
    headings = re.findall(r'^#{1,3}\s+(.+)$', body, re.MULTILINE)
    
    if is_en:
        # English FAQ
        if 'openclaw' in title.lower() or '龙虾' in title.lower() or 'lobster' in title.lower():
            faqs.append({'q': 'What is OpenClaw and how does it work?', 'a': 'OpenClaw is an open-source AI agent framework that runs on your own computer, acting as a 24/7 AI assistant that can automate tasks, write content, and manage workflows.'})
        if 'cost' in title.lower() or 'free' in title.lower() or 'price' in title.lower():
            faqs.append({'q': 'How much does it cost to run OpenClaw?', 'a': 'OpenClaw itself is free and open-source. The main costs are API tokens for AI models (varies by usage) and optionally a cloud server ($5-20/month).'})
        if 'deploy' in title.lower() or 'install' in title.lower() or 'setup' in title.lower():
            faqs.append({'q': 'Can I deploy OpenClaw without coding skills?', 'a': 'Yes, OpenClaw can be deployed with zero coding using one-click installers on cloud servers or Mac computers.'})
    else:
        # Chinese FAQ
        if 'openclaw' in title.lower() or '龙虾' in title:
            faqs.append({'q': 'OpenClaw龙虾是什么？', 'a': 'OpenClaw是一个开源AI Agent框架，可以在你自己的电脑上运行，充当24小时AI助手，自动化处理任务、写作和管理工作流。'})
        if '费用' in title or '花多少钱' in title or '成本' in title:
            faqs.append({'q': 'OpenClaw养龙虾需要花多少钱？', 'a': 'OpenClaw本身免费开源，主要成本是AI模型的API调用费（按使用量计费）和可选的云服务器费用（每月5-20美元）。'})
        if '部署' in title or '安装' in title:
            faqs.append({'q': '不会写代码能部署OpenClaw吗？', 'a': '可以。OpenClaw支持零代码一键部署，在云服务器或Mac电脑上都能快速安装。'})
    
    # Generic FAQ based on content
    if not faqs:
        # Extract first heading as a question topic
        if headings:
            topic = headings[0].strip()
            if is_en:
                faqs.append({'q': f'What is the main point of this article about {topic}?', 'a': f'This article provides an in-depth analysis of {topic}, with practical insights and personal experience from an AI content creator.'})
            else:
                faqs.append({'q': f'这篇文章关于{topic}的核心观点是什么？', 'a': f'本文深度分析了{topic}，结合AI内容创作者的实际经验提供实用见解。'})
    
    return faqs[:3]

def patch_post(filepath, is_en=False):
    """Add missing SEO/GEO fields to a post"""
    fm, body = parse_post(filepath)
    if fm is None:
        return False
    
    changed = False
    title = fm.get('title', '')
    summary = fm.get('summary', '')
    tags = fm.get('tags', [])
    
    # Add description if missing
    if 'description' not in fm:
        fm['description'] = make_description(title, summary, body)
        changed = True
    
    # Add keywords if missing
    if 'keywords' not in fm:
        fm['keywords'] = make_keywords(title, tags, is_en)
        changed = True
    
    # Add readingTime if missing
    if 'readingTime' not in fm:
        char_count = len(re.sub(r'\s+', '', body))
        fm['readingTime'] = max(1, round(char_count / (250 if is_en else 400)))
        changed = True
    
    # Add FAQ if missing
    if 'faq' not in fm:
        faq_items = make_faq(title, body, tags, is_en)
        if faq_items:
            fm['faq'] = faq_items
            changed = True
    
    # Add images for OG if missing
    if 'images' not in fm:
        cover = fm.get('cover', '')
        if cover:
            fm['images'] = [cover]
            changed = True
        else:
            img_match = re.search(r'!\[.*?\]\((/images/[^)]+)\)', body)
            if img_match:
                fm['images'] = [img_match.group(1)]
                changed = True
    
    if not changed:
        return False
    
    # Rewrite file
    with open(filepath, 'w') as f:
        f.write('---\n')
        # Custom YAML dump to handle quotes properly
        for key, val in fm.items():
            if key == 'faq':
                f.write('faq:\n')
                for item in val:
                    q = str(item['q']).replace("'", "''")
                    a = str(item['a']).replace("'", "''")
                    f.write(f"  - q: '{q}'\n")
                    f.write(f"    a: '{a}'\n")
            elif isinstance(val, list):
                f.write(f'{key}: {json.dumps(val, ensure_ascii=False)}\n')
            elif isinstance(val, (int, float)):
                f.write(f'{key}: {val}\n')
            elif isinstance(val, bool):
                f.write(f'{key}: {str(val).lower()}\n')
            else:
                val_str = str(val).replace("'", "''")
                f.write(f"{key}: '{val_str}'\n")
        f.write('---\n\n')
        f.write(body)
        f.write('\n')
    
    return True

def main():
    patched = 0
    for fname in sorted(os.listdir(POSTS)):
        if not fname.endswith('.md'):
            continue
        filepath = os.path.join(POSTS, fname)
        is_en = fname.endswith('.en.md')
        if patch_post(filepath, is_en):
            print(f"✅ {fname}")
            patched += 1
        else:
            print(f"⏭️ {fname} (已有SEO字段)")
    
    print(f"\n📊 已补丁 {patched} 篇文章")

if __name__ == "__main__":
    main()
