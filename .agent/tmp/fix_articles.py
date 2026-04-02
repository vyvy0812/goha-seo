import codecs
import re
import sys

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

file_path = r'c:\Users\MSI\Documents\Antigravity-SEO\Keywords\Heritage\top-dia-diem-du-lich-da-lat\article.md'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'### Vietnam Airlines có chuỗi tiện ích bổ trợ nào khi du khách đến sân bay Liên Khương\?\n.*?khách hạng vé cao cấp\. Hành trình chiêm ngưỡng 55 tuyệt tác Đà Lạt sẽ bắt đầu trong sự thoải mái tuyệt đối, dọn đường cho cảm xúc bay bổng ngay khi mười ngón chân chạm xuống cửa ngõ cao nguyên miền Nam\.\n\n', '', text, flags=re.DOTALL)
text = text.replace('## Lời kết trọn vẹn cho một hành trình xuyên thời gian cùng Vietnam Airlines', '## Lời kết trọn vẹn cho một hành trình xuyên thời gian cùng Heritage')
old_conclusion = r'Hành trình khám phá ngọn đồi thông lộng gió sẽ thực sự trọn vẹn khép kín hơn khi mở đầu bằng một vị thế sang trọng chuyên nghiệp\. Hãy để cánh bay mang biểu tượng Hoa Sen Vàng của \*\*Vietnam Airlines\*\* kết nối êm ái giữa bộn bề nhịp sống thường nhật với tầng tầng lớp lớp rặng mây bồng bềnh phủ trắng trời vùng di sản ngàn thông huyền thoại này\.'
new_conclusion = 'Hành trình khám phá ngọn đồi thông lộng gió sẽ thực sự trọn vẹn khép kín hơn thông qua một góc nhìn thưởng lãm vương giả. Hãy để những trang viết văn hóa tinh tế của Tạp chí **Heritage** kết nối êm ái giữa nhịp sống hối hả thường nhật với tầng tầng lớp lớp rặng mây bồng bềnh phủ trắng trời vùng di sản ngàn thông huyền thoại này, dẫn lối bạn trở về với những miền di sản nguyên bản tuyệt mỹ.'
text = re.sub(old_conclusion, new_conclusion, text)

primary_keyword = "địa điểm du lịch đà lạt"
count = text.lower().count(primary_keyword.lower())
print(f"Count initially for article 1: {count}")

replacements = [
    ('Thác Datanla ẩn mình', 'Thác Datanla ẩn mình, một địa điểm du lịch Đà Lạt '),
    ('Được ví như viên ngọc lục bảo khổng lồ phẳng lặng', 'Được ví như viên ngọc lục bảo khổng lồ phẳng lặng và cũng là một địa điểm du lịch Đà Lạt nổi tiếng bậc nhất, '),
    ('Sự hùng vĩ phô diễn tự do của Pongour', 'Sự hùng vĩ phô diễn tự do của địa điểm du lịch Đà Lạt ngoạn mục này'),
    ('Như một bến đỗ an yên lãng mạn lọt thỏm giữa rặng núi uy nghiêm', 'Như một bến đỗ an yên lãng mạn lọt thỏm giữa rặng núi uy nghiêm, địa điểm du lịch Đà Lạt này'),
    ('Dinh I (King Palace) ẩn mình giữa một đồi thông rộng lớn, tĩnh mịch.', 'Được đánh giá là địa điểm du lịch Đà Lạt quyền uy bậc nhất, Dinh I (King Palace) ẩn mình giữa một đồi thông rộng lớn, tĩnh mịch.'),
    ('Biệt điện Toàn Quyền Đông Dương ngạo nghễ sở hữu tầm nhìn panorama tuyệt đỉnh', 'Địa điểm du lịch Đà Lạt này ngạo nghễ sở hữu tầm nhìn panorama tuyệt đỉnh'),
    ('Khốc liệt và huyền bí, Thác Voi ồ ạt đổ xuống', 'Đại diện cho những địa điểm du lịch Đà Lạt nguyên sơ, khốc liệt và huyền bí, Thác Voi ồ ạt đổ xuống'),
    ('Thổi bùng vào cõi tạm thứ bồng lai ảo ảnh', 'Thổi bùng vào cõi tạm thứ bồng lai ảo ảnh, địa điểm du lịch Đà Lạt Lạc Tiên Giới'),
    ('Quy tụ tất cả mộng ảo về một miền quê thơ thẩn', 'Hình mẫu điển hình của các địa điểm du lịch Đà Lạt nên thơ, quy tụ tất cả mộng ảo về một miền quê thơ thẩn'),
    ('Từng đi vào muôn vàn thi ca bởi ráng chiều buông lơi trên dòng nước đổ', 'Từng đi vào muôn vàn thi ca bởi ráng chiều buông lơi trên dòng nước đổ, địa điểm du lịch Đà Lạt này')
]

if count < 10:
    needed = 12 - count
    injected = 0
    for old, new in replacements:
        if injected >= needed:
            break
        if old in text:
            text = text.replace(old, new)
            injected += 1
    print(f"Injected {injected} times for article 1")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

file_path2 = r'c:\Users\MSI\Documents\Antigravity-SEO\Keywords\Heritage\dia-diem-du-lich-gan-trung-tam-da-lat\article.md'
with open(file_path2, 'r', encoding='utf-8') as f2:
    text2 = f2.read()
count2 = text2.lower().count("địa điểm du lịch gần trung tâm đà lạt")
print(f"Article 2 keyword count: {count2}")
