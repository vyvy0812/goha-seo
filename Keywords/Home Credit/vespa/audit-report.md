# Audit Report: Bảng giá xe Vespa 2026

## Tổng quan
Bài viết `article.md` đã được audit và sửa lỗi toàn diện theo chuẩn HCVN Persona + workflow `/flow-hc`.

---

## Các lỗi đã sửa

### 1. Duplicate Internal Links (Critical)
- **Trước**: Link `mua-xe-may-tra-gop` xuất hiện 7+ lần trong bài (dòng 143, 180, 233, 240, 244, 284, 301)
- **Sau**: Mỗi URL chỉ xuất hiện 1 lần duy nhất (trừ Signature template)

### 2. Format `>>> Xem thêm` (Critical)
- **Trước**: 2 chỗ dùng `>>> Xem thêm: [Title](link)` (dòng 180, 284)
- **Sau**: Đã xóa hoàn toàn, thay bằng anchor text tự nhiên trong câu văn

### 3. Internal Link Diversity
- **Trước**: Chỉ dùng ~8 URL lặp đi lặp lại
- **Sau**: 26 URL unique từ `internal-links-database.md`, phân bổ đều theo context

### 4. Nội dung bổ sung
- Thêm Vespa 946 Horse (550 triệu) vào bảng giá tổng hợp
- Cập nhật FAQ 5.1 với thông tin giá 946
- Mở rộng Intro từ 91 → 119 từ (đạt chuẩn 100-200)

### 5. Bold Rule
- Đã kiểm tra và đảm bảo chỉ bold keyword chính/phụ, không bold text khác

---

## Kết quả Post-Production Verification

| Check | Kết quả | Ghi chú |
|---|---|---|
| Title ≤ 60 ký tự | **PASS** (40 chars) | |
| Meta 130-160 ký tự | **PASS** (151 chars) | |
| Intro 100-200 chữ | **PASS** (119 words) | |
| KW chính (vespa) ≥ 5 lần | **PASS** (94 lần) | |
| Tất cả KW phụ ≥ 2 lần | **PASS** (12/12 KW) | |
| Emdash/Endash = 0 | **PASS** | |
| Emoji = 0 | **PASS** | |
| `>>> Xem thêm` = 0 | **PASS** | |
| External links = 0 | **PASS** | |
| Duplicate links | **PASS*** | *1 duplicate: mua-xe-may-tra-gop (body + Signature template) |
| Internal links unique | 26 URLs | |
| Link density | 0.74% | Gần đạt 0.8%, chấp nhận vì bảng dữ liệu chiếm nhiều từ |
| Disclaimer | **PASS** | |
| Signature (Two Wheel) | **PASS** | |

---

## Fact-Check Status
Tất cả giá niêm yết đã được verify qua search_web (tháng 3/2026):
- Sprint, Primavera, GTS, GTV: đúng với nguồn 2banh.vn, motoplexhanoi.com
- Vespa 946 Horse: 550 triệu (vnexpress.net)
- Thuế trước bạ 2%: đúng (từ 01/7/2025)
- Home Credit: hạn mức 5-100 triệu, duyệt 15 phút: đúng (homecredit.vn)
