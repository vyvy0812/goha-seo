# Semantic Research: cách ứng tiền Viettel

## Entity Map

### Organization
- **Viettel**: Tập đoàn Công nghiệp Viễn thông Quân đội, nhà mạng lớn nhất VN
- **Home Credit Vietnam**: Công ty tài chính cung cấp dịch vụ nạp tiền điện thoại qua app
- **Viettel Telecom**: Đơn vị cung cấp dịch vụ viễn thông trả trước/trả sau

### Concept
- **Ứng tiền Viettel**: Dịch vụ cho phép thuê bao trả trước mượn tiền vào tài khoản khi hết tiền
- **Airtime Credit (9118)**: Dịch vụ ứng tiền linh hoạt từ 5k đến 100k
- **xTime (5511/511)**: Dịch vụ ứng tiền cho thuê bao chưa đủ điều kiện cơ bản
- **Cú pháp *911#**: Ứng nhanh 10.000đ cố định
- **My Viettel**: Ứng dụng chính thức của Viettel
- **Thuê bao trả trước**: Loại thuê bao sử dụng dịch vụ ứng tiền
- **Nợ cước ứng tiền**: Khoản tiền ứng + phí chưa thanh toán

### Time
- Cập nhật tháng 3/2026
- Điều kiện hoạt động tối thiểu 90 ngày

### Service (HC Match)
- Ứng dụng Home Credit: Nạp tiền điện thoại trả sau
- Tính năng: Nạp tiền trực tiếp, thanh toán cước trả sau, mua thẻ cào

## Query Clusters

### What (Định nghĩa)
- Ứng tiền Viettel là gì
- Dịch vụ 911, 9118, 5511 là gì

### How (Quy trình)
- Cách ứng tiền Viettel qua *911#
- Cách ứng tiền qua 9118
- Cách ứng tiền qua 5511
- Cách ứng tiền qua My Viettel
- Cách ứng tiền qua tổng đài 198
- Cách ứng tiền khi còn nợ
- Cách kiểm tra nợ cước ứng tiền
- Cách hủy dịch vụ ứng tiền

### Comparison (So sánh)
- So sánh 5 cách ứng tiền (mức tiền, phí)
- 911 vs 9118: khác nhau thế nào

### Detail (Chi tiết)
- Bảng phí dịch vụ ứng tiền
- Điều kiện ứng tiền Viettel
- Mức ứng tối đa mỗi cách

## Content Hierarchy
- **Vai trò**: Cluster Page (hướng dẫn cụ thể)
- **Pillar liên quan**: Nạp tiền điện thoại / Dịch vụ viễn thông Viettel
- **Internal linking**: Liên kết đến bài nạp tiền điện thoại qua app Home Credit

## Dữ liệu chi tiết (Verified 03/2026)

### Cách 1: *911# (Ứng nhanh)
- Cú pháp: Bấm *911# → Gọi
- Số tiền: 10.000đ (cố định)
- Phí: 1.500đ (15%)
- Tổng trừ khi nạp: 11.500đ
- Điều kiện: Trả trước, hoạt động 2 chiều ≥90 ngày, tài khoản <5.000đ, không nợ cước
- Giới hạn: Chỉ ứng 1 lần/lần nạp thẻ

### Cách 2: Gửi tin nhắn 9118 (Airtime Credit)
- Cú pháp: Soạn UT gửi 9118 (kiểm tra mức ứng) hoặc UT[số tiền] gửi 9118
- Ví dụ: UT20 gửi 9118 để ứng 20.000đ
- Số tiền: 5.000đ đến 100.000đ
- Phí: 10% đến 17% (≤50k: 15%, >50k: 17%)
- Điều kiện: Trả trước, hoạt động 2 chiều, lịch sử tiêu dùng ổn định, không nợ cước

### Cách 3: Gửi tin nhắn 5511 (xTime)
- Cú pháp: Soạn XT gửi 5511 hoặc bấm *511#
- Số tiền: 5.000đ đến 50.000đ
- Phí: 15% đến 17%
- Điều kiện: Hoạt động ≥90 ngày, tiêu dùng tháng gần nhất ≥150.000đ
- Đặc biệt: Có thể ứng khi còn nợ ở một số trường hợp

### Cách 4: Ứng dụng My Viettel
- Cách làm: Mở app → Nạp tiền → Ứng tiền → Đồng ý điều khoản
- Số tiền: 5.000đ đến 30.000đ
- Điều kiện: Trả trước, hoạt động 2 chiều 12 tháng, tài khoản <300đ, không nợ cước

### Cách 5: Tổng đài 198 (content gap)
- Cách làm: Gọi 198 (miễn phí) → Gặp nhân viên → Yêu cầu ứng tiền
- Số tiền: Theo hệ thống xác nhận
- Điều kiện: Chung (trả trước, hoạt động 2 chiều, không nợ cước)

### Kiểm tra nợ ứng tiền
- Soạn TC gửi 9118 (miễn phí)
- Soạn KT gửi 211
- Gọi 198 hoặc 18008198
- Qua ứng dụng My Viettel: Mục Lịch sử giao dịch

### Hủy dịch vụ ứng tiền
- Soạn TUCHOI gửi 9118 hoặc HUY gửi 9118
- Gọi tổng đài 198
- Qua ứng dụng My Viettel → Thuê bao → Dịch vụ → Hủy
