# Fact-Check Report: Công thức lãi kép

## 1. Verified Claims

### Công thức toán học (Python-verified)
- Công thức cơ bản A = P x (1 + r/n)^(n x t) → Verified ✅
- Ví dụ 100M, 7%, 10 năm lãi đơn = 170M → Verified ✅
- Ví dụ 100M, 7%, 10 năm lãi kép = 196.715.136 VND → Verified ✅
- Ví dụ 200M, 6.5%, 3 năm nhập lãi theo ngày = 243.057.978 → Verified ✅
- Ví dụ 200M, 6.5%, 3 năm nhập lãi theo tháng = 242.934.325 → Verified ✅
- Ví dụ 200M, 6.5%, 3 năm nhập lãi theo quý = 242.681.516 → Verified ✅
- Ví dụ 200M, 6.5%, 3 năm nhập lãi theo năm = 241.589.925 → Verified ✅
- DCA 5M/tháng, 7%/năm, 30 năm = ~6.1 tỷ → Verified ✅ (6.099.854.979)
- DCA 5M/tháng, 7%/năm, 20 năm = ~2.6 tỷ → Verified ✅ (2.604.633.299)

### Lãi suất tiết kiệm tháng 3/2026
- "4,7% đến 7,5%/năm" → Source: vneconomy.vn, laodong.vn, vnexpress.net (tháng 3/2026) ✅
- "Gửi online cao hơn 0,3 đến 0,7 điểm %" → Source: vneconomy.vn ✅

### Khái niệm tài chính
- "Lãi kép = Compound Interest, lãi mẹ đẻ lãi con" → Wikipedia, Prudential, HDBank ✅
- "Kỳ quan thứ 8 của thế giới" → Trích dẫn phổ biến, xuất hiện trên nhiều nguồn ✅
- Lãi suất không kỳ hạn "0,1% đến 0,5%/năm" → Phổ biến tại các NHTM Việt Nam ✅

## 2. Corrections Made (đã sửa trong article.md)

| # | Original | Corrected To | Reason |
|---|---|---|---|
| 1 | Daily: 243.155.522 | 243.057.978 | Python calculation mismatch |
| 2 | Monthly: 243.021.348 | 242.934.325 | Python calculation mismatch |
| 3 | Quarterly: 242.686.254 | 242.681.516 | Python calculation mismatch |
| 4 | Annual: 241.589.845 | 241.589.925 | Python calculation mismatch |
| 5 | DCA 20yr: "2,8 tỷ" | "2,6 tỷ" | Python: 2.604.633.299 |
| 6 | DCA diff: "3 tỷ" | "3,5 tỷ" | Corrected to match verified numbers |
| 7 | Chênh 1,57 triệu | 1,47 triệu | Corrected based on new calculations |

## 3. Removed Claims
- Không có claim nào bị xóa. Tất cả claims đã được verify hoặc sửa chính xác.
