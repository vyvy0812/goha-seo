# Semantic Research: Quẹt thẻ tín dụng

## Entity Map

### Concept (Khái niệm)
- **Quẹt thẻ tín dụng**: Hành động sử dụng thẻ tín dụng thanh toán qua máy POS hoặc thiết bị đọc thẻ
- **Máy POS (Point of Sale)**: Thiết bị điện tử chấp nhận thanh toán bằng thẻ ngân hàng
- **Contactless / NFC**: Công nghệ thanh toán không tiếp xúc, chạm thẻ hoặc điện thoại
- **Thẻ từ (Magnetic Stripe)**: Công nghệ thẻ cũ sử dụng dải từ
- **Thẻ chip (EMV Chip)**: Công nghệ thẻ hiện đại có gắn chip bảo mật
- **Hạn mức tín dụng**: Số tiền tối đa ngân hàng cho phép chi tiêu
- **Kỳ sao kê**: Chu kỳ thanh toán hàng tháng của thẻ tín dụng
- **Thời gian miễn lãi**: 45-55 ngày
- **CVV/CVC**: Mã bảo mật 3 số mặt sau thẻ
- **Mã PIN**: Mật khẩu 4-6 số xác thực giao dịch
- **SmartPOS / SoftPOS**: Các loại máy POS thế hệ mới

### Organization (Tổ chức)
- **Home Credit**: Công ty tài chính phát hành thẻ tín dụng
- **VISA**: Tổ chức thẻ quốc tế
- **Mastercard**: Tổ chức thẻ quốc tế
- **NAPAS**: Tổ chức thẻ nội địa Việt Nam
- **Ngân hàng Nhà nước Việt Nam**: Cơ quan quản lý

### Person
- Chủ thẻ (Cardholder)
- Đơn vị chấp nhận thẻ (Merchant)
- Ngân hàng phát hành (Issuing Bank)
- Ngân hàng thanh toán (Acquiring Bank)

---

## Query Clusters & Facts

### What: Định nghĩa
- Quẹt thẻ tín dụng = sử dụng thẻ thanh toán hàng hóa/dịch vụ qua máy POS
- Bản chất: "tiêu trước, trả sau" trong hạn mức tín dụng được cấp
- Quy trình: Thẻ → Máy POS → Ngân hàng thanh toán → Tổ chức thẻ (VISA/MC) → Ngân hàng phát hành → Phê duyệt

### How: Cách thực hiện
1. **Thẻ từ**: Quẹt dải từ qua khe đọc
2. **Thẻ chip**: Cắm thẻ vào khe đọc chip
3. **Contactless**: Chạm thẻ vào biểu tượng sóng trên máy POS
4. **Điện thoại (NFC)**: Apple Pay, Samsung Pay, Google Pay → chạm điện thoại vào máy POS

### Where: Quẹt ở đâu
- Siêu thị, cửa hàng, nhà hàng có máy POS
- Trung tâm thương mại
- Sân bay, khách sạn
- Cửa hàng online (nhập số thẻ, CVV, ngày hết hạn)
- Bất kỳ điểm chấp nhận VISA/Mastercard

### Fee: Chi phí
- **Thanh toán mua sắm**: Chủ thẻ KHÔNG mất phí
- **Phí merchant**: 1-2.5% (do cửa hàng trả cho NH)
- **Rút tiền mặt**: Phí 1-4% + lãi suất 20-40%/năm, tính lãi ngay lập tức
- **Chuyển đổi ngoại tệ**: 1-3% (khi quẹt ở nước ngoài)
- **Home Credit**: Phí rút tiền mặt 3% (tối thiểu 30.000 VNĐ), phí chuyển đổi ngoại tệ 4%

### Warning: Cảnh báo
- Dịch vụ "cà thẻ lấy tiền mặt" qua POS: Trái quy định, rủi ro lộ thông tin
- Rút tiền mặt từ ATM: Phí cao, lãi tính ngay
- Thanh toán chậm: Lãi suất 45-49.5%/năm (Home Credit)

---

## Thông tin Home Credit Card

| Mục | Chi tiết |
|---|---|
| Hạn mức tối đa | 100 triệu đồng |
| Phí phát hành/thường niên | Miễn phí |
| Phí quản lý thẻ | 39.000 VNĐ/tháng (miễn nếu chi tiêu từ 3 triệu hoặc 5 giao dịch/kỳ) |
| Phí rút tiền mặt | 3% (tối thiểu 30.000 VNĐ) |
| Phí chuyển đổi ngoại tệ | 4% (tối thiểu 10.000 VNĐ) |
| Lãi suất | 45-49.5%/năm |
| Miễn lãi | Lên đến 45 ngày |
| Điều kiện | CCCD, từ 18 tuổi, đăng ký 100% online |
| Duyệt | Nhanh 3 phút |
| Trả góp | 0% lãi suất tại đối tác liên kết |
| Hoàn tiền | 10% cho nhóm chi tiêu |
