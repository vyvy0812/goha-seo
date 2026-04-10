# Semantic Research & Entity Discovery: Số thẻ tín dụng

## 1. Entity Map

### Person
- Chủ thẻ (Cardholder)
- Hans Peter Luhn (nhà khoa học IBM, cha đẻ thuật toán Luhn)

### Organization
- Visa, Mastercard, JCB, American Express, UnionPay, Discover
- ISO (International Organization for Standardization)
- Home Credit Vietnam
- Ngân hàng Nhà nước Việt Nam (NHNN)

### Concept
- Số thẻ tín dụng (Credit Card Number / PAN - Primary Account Number)
- BIN/IIN (Bank Identification Number / Issuer Identification Number)
- Thuật toán Luhn (Luhn Algorithm / Mod 10)
- CVV/CVC (Card Verification Value / Card Verification Code)
- Checksum digit (chữ số kiểm tra)
- Skimming (gắn thiết bị đọc lén)
- Phishing (website giả mạo)
- 3D Secure / OTP (xác thực hai lớp)
- Thẻ tín dụng ảo (Virtual Credit Card)
- ISO/IEC 7812 (tiêu chuẩn quốc tế về số thẻ)
- MII (Major Industry Identifier)
- Mã PIN
- Máy POS (Point of Sale)
- Thanh toán không tiếp xúc (Contactless Payment)

### Location
- Mặt trước thẻ (số thẻ), mặt sau thẻ (CVV/CVC)
- ATM, máy POS, website https://

### Time
- Ngày hết hạn thẻ (Expiry Date)
- 45 ngày miễn lãi (Home Credit)

## 2. Query Clusters

### What (Định nghĩa)
- Số thẻ tín dụng là gì
- Số CVV/CVC trên thẻ tín dụng là gì
- BIN/IIN là gì
- Thuật toán Luhn là gì
- Số thẻ tín dụng ảo là gì

### How (Hướng dẫn)
- Cách kiểm tra số thẻ tín dụng hợp lệ
- Cách bảo mật số thẻ tín dụng
- Cách xử lý khi bị lộ số thẻ tín dụng
- Cách đọc ý nghĩa từng cụm số trên thẻ

### Why (Nguyên nhân)
- Tại sao số thẻ tín dụng không hợp lệ
- Bị lộ số thẻ tín dụng có sao không

### Comparison (So sánh)
- Số thẻ tín dụng vs số tài khoản ngân hàng
- Thẻ tín dụng ảo vs thẻ vật lý

### Best/Top
- 9 cách bảo vệ số thẻ tín dụng an toàn

## 3. Thông tin then chốt đã xác minh

| Thông tin | Chi tiết | Nguồn |
|---|---|---|
| Số lượng chữ số | 16 số (phổ biến), 15-19 số (tùy loại) | Visa, Mastercard, ISO/IEC 7812 |
| Đầu số Visa | Bắt đầu bằng 4 | Quy chuẩn quốc tế |
| Đầu số Mastercard | Bắt đầu bằng 5 (51-55) hoặc 2 (2221-2720) | Quy chuẩn quốc tế |
| Đầu số JCB | Bắt đầu bằng 35 | Quy chuẩn quốc tế |
| Đầu số AmEx | Bắt đầu bằng 34 hoặc 37, có 15 số | Quy chuẩn quốc tế |
| 6 số đầu (BIN) | Xác định ngân hàng phát hành | ISO/IEC 7812 |
| CVV/CVC | 3 số mặt sau (Visa/MC), 4 số mặt trước (AmEx) | Các ngân hàng |
| Thuật toán Luhn | Kiểm tra checksum, mod 10 | IBM, Hans Peter Luhn |
