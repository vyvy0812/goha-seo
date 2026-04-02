# Research: Ứng tiền VinaPhone

## Entity Map

| Entity | Type | Relevance |
|---|---|---|
| VinaPhone / VNPT | Organization | Nhà mạng cung cấp dịch vụ ứng tiền |
| Tổng đài 1576 | Service | Đầu số chính cho ứng tiền chủ động + tự động |
| Airtime Plus / 1357 | Service | Dịch vụ ứng tiền miễn phí |
| *911# | Service | Ứng tiền khẩn cấp 3.000đ |
| My VNPT | Application | Ứng dụng ứng tiền online |
| Thuê bao trả trước | Concept | Đối tượng sử dụng dịch vụ |
| Phí dịch vụ | Concept | 10% đến 30% tùy hình thức |
| Home Credit | Organization | Ứng dụng nạp tiền ĐT thay thế |

## Query Clusters

| Nhóm | Queries | Heading tương ứng |
|---|---|---|
| What | ứng tiền vina là gì | H2: Ứng tiền VinaPhone là gì |
| How | cách ứng tiền vina, cú pháp, cách ứng tiền vina 10k | H2: Cách ứng tiền VinaPhone qua nhà cung cấp mạng |
| How (specific) | cách ứng tiền vinaphone 100k, 20k | H3: Mệnh giá và phí dịch vụ |
| Condition | điều kiện ứng tiền, chưa đủ điều kiện | H2: Điều kiện + H2: Ứng liên tiếp |
| Table | bảng mệnh giá, phí | H2: Bảng tổng hợp |
| Alternative | ứng tiền trả sau | H2: Ứng dụng Home Credit |

## Content Hierarchy
- **Cluster Page**: Bài chi tiết về ứng tiền VinaPhone
- **Liên kết pillar**: Cách nạp tiền điện thoại, cách kiểm tra tiền điện thoại
- **Liên kết cluster ngang**: Ứng tiền Viettel, ứng tiền MobiFone, ứng tiền Vietnamobile

## Dữ liệu xác thực (2026)

### Ứng tiền chủ động qua 1576
- Cú pháp: Soạn UT gửi 1576 hoặc bấm *1576#
- Mệnh giá: 10.000đ/lần
- Phí: Khoảng 10% đến 15%
- Điều kiện: Trả trước, 2 chiều, 3 tháng+, tiêu 15.000đ/tháng, nạp 10.000đ/tháng (2 tháng), hoàn trả nợ cũ

### Ứng tiền tự động từ tổng đài
- Cú pháp: Soạn Y gửi 1576 (khi nhận SMS mời)
- Mệnh giá: 5.000đ đến 50.000đ (tùy lịch sử tiêu dùng)
- Kích hoạt: Tài khoản dưới 5.000đ
- Thời hạn xác nhận: 24 giờ

### Airtime Plus qua 1357
- Cú pháp: Soạn A gửi 1357 (hoặc UA gửi 1357)
- Mệnh giá: 5.000đ đến 50.000đ
- Phí: Miễn phí (có thời hạn sử dụng)
- Kích hoạt: Tài khoản còn 0đ, tổng đài gửi SMS mời
- Thời hạn chấp nhận: 48 giờ
- Hủy DV: TC A gửi 1357

### Ứng tiền khẩn cấp *911#
- Cú pháp: Bấm *911# nhấn Gọi
- Mệnh giá: 3.000đ
- Điều kiện: Thuê bao hoạt động 12 tháng+, TK dưới 300đ

### My VNPT
- Mở app → Nạp tiền điện thoại → Ứng tiền → Nhận ứng

### Dịch vụ GTGT khác
- Gọi trước trả sau: 1094 + SĐT cần gọi
- Ứng phút gọi: UDV THOAI gửi 9345
- Người nghe trả tiền: DK gửi 1569, gọi 1569+SĐT

### Cơ chế hoàn trả
- Tự động trừ khi nạp thẻ lần tiếp theo
- Trừ tiền ứng + phí dịch vụ

### Ứng liên tiếp
- Có thể ứng tối đa 5 lần trước khi phải hoàn trả
- Tùy thuộc lịch sử sử dụng và loại thuê bao
