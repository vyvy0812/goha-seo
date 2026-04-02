import re
import sys

file_path = r'c:\Users\MSI\Documents\Antigravity-SEO\Keywords\Heritage\top-dia-diem-du-lich-da-lat\article.md'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Pattern matches the exact 4-line structure of each location
    pattern = re.compile(r"^Địa chỉ: (.*?)\nGiá vé tham quan: (.*?)\nThời gian hoạt động: (.*?)\n(.*)$", re.MULTILINE)

    def repl(m):
        return f"* **Địa chỉ:** {m.group(1)}\n* **Giá vé tham quan:** {m.group(2)}\n* **Thời gian hoạt động:** {m.group(3)}\n\n{m.group(4)}"

    new_text = pattern.sub(repl, text)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_text)

    print("Successfully reformatted article.md")
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
