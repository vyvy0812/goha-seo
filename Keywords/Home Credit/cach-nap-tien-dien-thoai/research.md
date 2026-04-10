# Semantic Research: cách nạp tiền điện thoại

## Entity Map

| Entity | Type | Vai trò |
|---|---|---|
| Viettel | Organization | Nhà mạng lớn nhất VN |
| MobiFone | Organization | Nhà mạng |
| VinaPhone (VNPT) | Organization | Nhà mạng |
| Home Credit | Organization | Ứng dụng tích hợp nạp tiền ĐT |
| MoMo | Organization | Ví điện tử phổ biến |
| ZaloPay | Organization | Ví điện tử |
| ShopeePay | Organization | Ví điện tử trên Shopee |
| Thẻ cào | Concept | Phương thức nạp truyền thống |
| Cú pháp USSD *100* | Concept | Mã nạp thẻ trả trước |
| *199*, *188*0* | Concept | Mã nạp thẻ trả sau |
| *101# | Concept | Kiểm tra số dư |
| Mobile Banking | Concept | Nạp qua ứng dụng ngân hàng |
| Internet Banking | Concept | Nạp qua website ngân hàng |
| ATM | Concept | Nạp qua máy rút tiền |
| SMS | Concept | Nạp qua tin nhắn |
| My Viettel, My MobiFone, My VNPT | Product | Ứng dụng nhà mạng |
| QR Code | Concept | Nạp bằng quét mã |
| Thuê bao trả trước | Concept | Loại thuê bao |
| Thuê bao trả sau | Concept | Loại thuê bao |

## Cú pháp nạp thẻ cào

### Trả trước (chung 3 nhà mạng)
- *100*Mã thẻ# → Gọi

### Trả sau
- Viettel: *199*Mã thẻ# → Gọi
- VinaPhone: *188*0*Mã thẻ# → Gọi
- MobiFone: *100*Mã thẻ# → Gọi (cần đăng ký FastPay: DKTK gửi 9233)

## Kiểm tra số dư
- Viettel: *101# (chính), *102# (khuyến mãi)
- MobiFone: *101# (trả trước), *112# (trả sau)
- VinaPhone: *101# (chính), *111# (chi tiết)

## Nạp tiền cho người khác
- Viettel: *136# → chọn 4 (Nạp thẻ hộ)
- VinaPhone: Gọi 18001094 → phím 1 → phím 2, hoặc dịch vụ 2Friends (DK gửi 999)
- MobiFone: Không có cú pháp trực tiếp, gửi mã thẻ cho người nhận

## Query Clusters
- How: cách nạp tiền điện thoại, cách nạp thẻ, cách nạp card
- What: nạp thẻ là gì, thuê bao trả trước trả sau
- Comparison: so sánh các phương thức nạp tiền
- Check: cách kiểm tra tiền điện thoại sau khi nạp

## Content Hierarchy
- Pillar Page: Bài viết bao quát tất cả phương thức nạp tiền
- Clusters: Bài riêng cho từng nhà mạng (đã có trên HC blog)
