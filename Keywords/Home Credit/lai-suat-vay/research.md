# Semantic Research: Lãi suất vay

## Entity Map

| Entity | Type | Vai trò trong bài |
|---|---|---|
| Ngân hàng Nhà nước Việt Nam (NHNN) | Organization | Cơ quan điều hành chính sách tiền tệ, quyết định lãi suất điều hành |
| Ngân hàng thương mại (VietinBank, BIDV, Vietcombank, Agribank) | Organization | Big4, mức lãi suất cho vay thấp nhất thị trường |
| Ngân hàng TMCP (VPBank, Techcombank, MBBank, Sacombank...) | Organization | Nhóm có lãi suất cao hơn, nhiều sản phẩm vay đa dạng |
| Home Credit | Organization | Công ty tài chính, dịch vụ vay tiền mặt, promote trong bài |
| Lãi suất điều hành | Concept | Lãi suất tái cấp vốn, tái chiết khấu, cho vay qua đêm do NHNN quy định |
| Lãi suất cố định | Concept | Lãi suất không đổi trong suốt kỳ hạn vay |
| Lãi suất thả nổi | Concept | Lãi suất thay đổi theo thị trường sau thời gian ưu đãi |
| Lãi suất tiền gửi | Concept | Lãi ngân hàng trả cho người gửi tiết kiệm |
| Lãi suất cho vay | Concept | Lãi người vay phải trả cho ngân hàng |
| Dư nợ giảm dần | Concept | Phương pháp tính lãi phổ biến, lãi giảm theo gốc đã trả |
| Dư nợ gốc | Concept | Phương pháp tính lãi trên tổng gốc ban đầu |
| Lạm phát | Concept | Yếu tố vĩ mô ảnh hưởng trực tiếp đến lãi suất |
| CIC | Concept | Trung tâm Thông tin Tín dụng Quốc gia, ảnh hưởng đến lãi suất được hưởng |
| Điểm tín dụng | Concept | Chỉ số đánh giá khả năng trả nợ, quyết định lãi suất vay |
| Q1/2026 | Time | Thời điểm cập nhật dữ liệu lãi suất mới nhất |

## Dữ liệu thị trường (tháng 3/2026)

### Lãi suất cho vay
- Bình quân: 5,42% đến 7,73%/năm
- Big4: VietinBank 5,42%, BIDV 5,52%, Vietcombank 5,6%
- NHTMCP: 7% đến 7,7%/năm
- Vay thế chấp: 5,5% đến 12%/năm
- Vay tín chấp: 8,5% đến 24%/năm

### Lãi suất tiết kiệm
- Kỳ hạn ngắn (1 đến 3 tháng): 2,1% đến 4,75%/năm
- Kỳ hạn trung bình (6 đến 12 tháng): 4,0% đến 7,0%/năm
- Kỳ hạn dài (trên 12 tháng): 5,5% đến 7,5%/năm
- Trần lãi suất huy động kỳ hạn dưới 6 tháng: 4,75%/năm
- Online cao hơn tại quầy: 0,3% đến 0,7%/năm

### Vĩ mô
- Lạm phát mục tiêu 2026: 4,5% (Quốc hội)
- Dự báo CPI thực tế: 3,5% đến 3,8%
- Tăng trưởng tín dụng mục tiêu: 15%
- GDP phấn đấu: tăng trưởng 10%

## Query Clusters

### What (Định nghĩa)
- lãi suất ngân hàng là gì
- lãi suất cho vay là gì
- lãi suất cố định vs thả nổi
→ Map H2: "Lãi suất ngân hàng là gì? Phân loại"

### How (Quy trình)
- cách tính lãi suất vay
- cách tính lãi suất tiền gửi
- công thức tính lãi vay theo dư nợ giảm dần
→ Map H2/H3: "Công thức tính lãi suất cho vay", "Công thức tính lãi suất tiền gửi"

### Why (Giải thích)
- tại sao lãi suất vay cao hơn lãi suất huy động
- yếu tố ảnh hưởng lãi suất
→ Map H2: "Yếu tố ảnh hưởng đến lãi suất ngân hàng 2026"

### Comparison (So sánh)
- lãi suất cố định vs thả nổi
- so sánh lãi suất các ngân hàng
→ Map H3: trong phần "Các loại lãi suất cho vay"

### Best/Top (Xếp hạng)
- vay ngân hàng lãi suất bao nhiêu
- lãi suất ngân hàng nào thấp nhất
→ Map: bảng so sánh lãi suất trong bài

## Content Hierarchy

### Vai trò bài viết: Pillar Page
- Topic rộng "lãi suất ngân hàng" bao quát cả tiết kiệm và cho vay
- Bài dạng tổng quan, định nghĩa + hướng dẫn + so sánh

### Internal Linking Strategy
- Pillar → Cluster: link đến các bài chi tiết (lãi suất cố định, lãi suất thả nổi, cách tính lãi vay, điểm tín dụng...)
- Cluster → Pillar: các bài chi tiết link ngược về Pillar
- Cluster ↔ Cluster: link ngang giữa các bài liên quan (lãi kép, lãi đơn, vay tín chấp, vay thế chấp...)
