# Semantic Research: ứng tiền mobi

## Entity Map

| Entity | Type | Vai trò trong bài |
|---|---|---|
| MobiFone | Organization | Nhà mạng cung cấp dịch vụ ứng tiền |
| Tổng đài 988 | Service | Kênh ứng tiền chính, cú pháp SMS UT10/UT15/UT20 |
| Tổng đài 900 | Service | Kênh ứng tiền 20k vào TK KM3 |
| Fast Credit | Service | Dịch vụ ứng tiền tự động qua 9015/9025/9779 |
| Airtime Plus | Service | Dịch vụ ứng tiền miễn phí qua 9913/1255 |
| My MobiFone | App | Ứng dụng quản lý thuê bao MobiFone |
| Tài khoản chính | Concept | Tài khoản dùng cho mọi dịch vụ (gọi, nhắn, data) |
| Tài khoản KM3 | Concept | Tài khoản khuyến mãi 3, giới hạn sử dụng |
| Tài khoản AP2 | Concept | Tài khoản Airtime Plus, giới hạn thời gian |
| Thuê bao trả trước | Concept | Loại thuê bao được hỗ trợ ứng tiền |
| Thuê bao trả sau | Concept | Không hỗ trợ ứng tiền |
| Phí dịch vụ | Concept | 10% đến 30% tùy dịch vụ |
| Home Credit | Organization | Nền tảng tài chính, hỗ trợ nạp tiền/thanh toán trên ứng dụng |

## Query Clusters

### What (Định nghĩa)
- ứng tiền mobi là gì
- ứng tiền của mobifone
- ứng tiền sim mobi
→ Map: H2 "Ứng tiền Mobi là gì"

### How (Quy trình)
- cách ứng tiền mobi
- cách ứng tiền mobifone
- cách ứng tiền mobi 20k vào tài khoản chính
- cách ứng tiền mobi 5k vào tài khoản chính
- cách ứng tiền mobifone vào tài khoản chính
- cách ứng tiền vào tài khoản chính mobifone
- cú pháp ứng tiền mobi
- ứng tiền mobi 9779
→ Map: H2 "Các cách ứng tiền Mobifone vào tài khoản chính" (H3 cho từng cách)

### Condition (Điều kiện)
- điều kiện ứng tiền Mobifone
- cách ứng tiền sim mobi khi chưa đủ điều kiện
→ Map: H2 "Điều kiện ứng tiền Mobifone"

### Object (Đối tượng)
- ứng tiền sim mobi
- cách ứng tiền sim mobi
→ Gom vào phần điều kiện/hướng dẫn

### Fee/Repayment (Phí)
- phí dịch vụ ứng tiền
- cách hoàn trả tiền ứng
→ Map: H2 "Phí dịch vụ và cách hoàn trả"

## Content Hierarchy

- **Loại bài**: Cluster Page (topic cụ thể về ứng tiền MobiFone)
- **Pillar liên quan**: Bài tổng hợp viễn thông/nạp tiền điện thoại
- **Internal linking**:
  - Link ngang: cách ứng tiền Viettel, cách ứng tiền Vinaphone, cách ứng tiền Vietnamobile
  - Link liên quan: nạp thẻ MobiFone, kiểm tra tiền điện thoại, thuê bao trả trước/trả sau
  - Link HC: ứng dụng Home Credit (nạp tiền trên app)

## Dữ liệu chính (đã verify qua search)

### Cách 1: Tổng đài 988
- Mức ứng: 10k, 15k, 20k
- Cú pháp: UT10/UT15/UT20 gửi 988 hoặc bấm *988#
- Tiền cộng vào: tài khoản chính
- Phí: khoảng 15% (VD: ứng 10k → phí 1.500đ)
- ĐK: thuê bao trả trước, hoạt động 2 chiều, tối thiểu 45 ngày, TK dưới 5.000đ

### Cách 2: Tổng đài 900
- Mức ứng: 20k
- Cú pháp: Soạn UT gửi 900, sau đó CO gửi 900 xác nhận (trong 10 phút)
- Tiền cộng vào: tài khoản KM3
- Phí: 2.000đ/lần
- ĐK: tương tự 988

### Cách 3: Fast Credit (9779, 9015, 9025)
- Mức ứng: lên đến 50k (hệ thống quyết định)
- Cú pháp: Y gửi 9015/9025/9779 khi nhận SMS mời
- Ứng tự động: UTD gửi 9015/9025/9779
- Hủy: TC hoặc HUY gửi đầu số
- Phí: 10% đến 30%
- ĐK: hoạt động 3 tháng, tiêu 15k/3 tháng, nạp ít nhất 1 lần/tháng

### Cách 4: Airtime Plus (9913, 1255)
- Mức ứng: 5k đến 50k
- Cú pháp: Y gửi 9913 hoặc 1255 khi nhận SMS mời
- Tiền cộng vào: tài khoản AP2
- Thời hạn sử dụng: 1 đến 24 giờ
- Phí: miễn phí
- Hoàn trả: tối đa 90 ngày
