# Semantic Research: Công thức lãi kép

## Entity Map

| Entity | Type | Vai trò trong bài |
|---|---|---|
| Lãi kép (Compound Interest) | Concept | Core entity, chủ đề chính |
| Lãi đơn (Simple Interest) | Concept | Entity so sánh |
| Lãi suất danh nghĩa (Nominal Rate) | Concept | Thành phần công thức |
| Tần suất nhập lãi (Compounding Frequency) | Concept | Yếu tố ảnh hưởng |
| Tiền gốc (Principal - P) | Concept | Thành phần công thức |
| Giá trị tương lai (Future Value - A/FV) | Concept | Kết quả tính toán |
| Albert Einstein | Person | Trích dẫn "kỳ quan thứ 8" |
| Ngân hàng Nhà nước Việt Nam (NHNN) | Organization | Cơ quan quản lý |
| Ngân hàng thương mại (Techcombank, HDBank, SeABank, MSB) | Organization | Đơn vị cung cấp sản phẩm tiết kiệm |
| Home Credit | Organization | Brand chủ, dịch vụ tài chính |
| Chứng khoán | Concept | Kênh đầu tư lãi kép |
| Vàng | Concept | Kênh đầu tư |
| Bất động sản | Concept | Kênh đầu tư |
| Gửi tiết kiệm có kỳ hạn | Concept | Kênh đầu tư phổ biến nhất cho lãi kép |
| 2026 | Time | Thời điểm cập nhật |

## Query Clusters

### What (Định nghĩa)
- lãi kép là gì
- lãi suất kép là gì
- compound interest là gì

### How (Quy trình / Công thức)
- công thức tính lãi kép
- công thức lãi kép
- cách tính lãi suất kép
- tính lãi kép theo ngày
- tính lãi kép theo tháng
- tính lãi kép theo quý
- tính lãi kép theo năm
- tính lãi suất kép online

### Why (Giải thích)
- tại sao lãi kép quan trọng
- lãi kép phát huy hiệu quả khi nào
- lợi ích của lãi suất kép

### Comparison (So sánh)
- lãi kép và lãi đơn khác nhau thế nào
- so sánh lãi kép theo ngày tháng quý năm
- nên gửi tiết kiệm theo kỳ hạn nào

### Best/Top (Xếp hạng)
- đầu tư vào đâu để có lãi suất kép
- kênh đầu tư lãi kép hiệu quả
- công cụ tính lãi kép online miễn phí

## Content Hierarchy

- **Vai trò bài viết**: Pillar Page (topic rộng, bao quát về lãi kép)
- **Internal linking strategy**:
  - Pillar → Cluster: Link sang bài "lãi đơn là gì", "đầu tư tài chính là gì", "sổ tiết kiệm là gì"
  - Cluster → Pillar: Các bài cluster liên quan link ngược về bài này
  - Cluster ↔ Cluster: "cách tính lãi suất vay", "đòn bẩy tài chính"

## Công thức chính

### Công thức lãi kép cơ bản
```
A = P × (1 + r)^t
```
- A: Tổng tiền nhận được (gốc + lãi)
- P: Vốn gốc ban đầu
- r: Lãi suất/kỳ
- t: Số kỳ

### Công thức lãi kép tổng quát (có tần suất nhập lãi)
```
A = P × (1 + r/n)^(n×t)
```
- n: Số lần nhập lãi/năm (365 = ngày, 12 = tháng, 4 = quý, 1 = năm)

### Tiền lãi thuần
```
CI = A - P = P × [(1 + r/n)^(n×t) - 1]
```
