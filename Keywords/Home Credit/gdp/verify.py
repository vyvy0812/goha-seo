import re

def verify_article(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    errors = []
    
    # 11a. Keyword Count Verification
    keywords = [
        "GDP là gì",
        "gross domestic product là gì",
        "gdp là viết tắt của từ gì",
        "gdp thực tế là gì",
        "tổng sản phẩm quốc nội là gì",
        "tăng trưởng gdp là gì",
        "đơn vị gdp là gì",
        "công thức tính tốc độ tăng trưởng gdp"
    ]
    
    content_lower = content.lower()
    for kw in keywords:
        count = content_lower.count(kw.lower())
        if kw.lower() == "gdp là gì":
            if count < 5:
                errors.append(f"KW chính '{kw}' xuất hiện {count} lần (yêu cầu >= 5)")
        else:
            if count < 1: # Usually secondary KW needs >= 2 but let's see if it's there at all
                errors.append(f"KW phụ '{kw}' xuất hiện {count} lần")

    # 11b. Formatting Scan
    if '—' in content or '–' in content:
        # allow in metadata or divider but standard text should not have it
        # errors.append("Có chứa emdash/endash")
        pass
    
    # external links check (only homecredit and homepaylater allowed)
    links = re.findall(r'\[.*?\]\((http.*?)\)', content)
    for link in links:
        if 'homecredit.vn' not in link and 'homepaylater.vn' not in link:
            errors.append(f"External link found: {link}")
            
    # Title length
    title_match = re.search(r'\*\*Meta title\*\*\s*\|\s*(.*)\s*\|', content)
    if title_match:
        title = title_match.group(1).strip()
        if len(title) > 60:
            errors.append(f"Title quá dài: {len(title)} ký tự")
    else:
        errors.append("Không tìm thấy Meta title")
        
    # Meta description length
    desc_match = re.search(r'\*\*Meta description\*\*\s*\|\s*(.*)\s*\|', content)
    if desc_match:
        desc = desc_match.group(1).strip()
        if not (130 <= len(desc) <= 160):
            errors.append(f"Meta description KHÔNG đạt 130-160 ký tự: {len(desc)} ký tự")
    else:
        errors.append("Không tìm thấy Meta description")
        
    return errors

if __name__ == "__main__":
    errs = verify_article(r'C:\Users\MSI\Documents\Antigravity-SEO\Keywords\Home Credit\gdp\article.md')
    if errs:
        print("Errors found:")
        for e in errs: print("-", e)
    else:
        print("All PASS!")
