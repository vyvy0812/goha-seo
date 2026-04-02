# Semantic Research: trả chậm thẻ tín dụng

## Entity Map

### Organization
- CIC (Trung tâm Thông tin Tín dụng Quốc gia Việt Nam)
- Ngân hàng Nhà nước Việt Nam (NHNN)
- Home Credit Vietnam
- Các ngân hàng: Techcombank, BIDV, VIB, ACB, HDBank, VPBank, SeABank

### Concept
- Thẻ tín dụng (Credit Card)
- Dư nợ thẻ tín dụng
- Sao kê thẻ tín dụng (billing statement)
- Thanh toán tối thiểu (minimum payment): thường 5% dư nợ
- Thời gian miễn lãi (grace period): 45-55 ngày
- Phí phạt trả chậm (late payment fee): 4-6% dư nợ quá hạn
- Lãi suất quá hạn: 20-40%/năm
- Nhóm nợ CIC (1-5)
- Nợ xấu (NPL): Nhóm 3 trở lên (91 ngày+)
- Điểm tín dụng (credit score)
- Lịch sử tín dụng (credit history)
- Thanh toán tự động (auto-debit)
- Trả góp dư nợ (installment conversion)

### Legal / Regulation
- Thông tư 14/2017/TT-NHNN: phương pháp tính lãi trong hoạt động cấp tín dụng
- Quy định phân loại nợ NHNN (5 nhóm)
- Trách nhiệm pháp lý: khởi kiện dân sự nếu nợ quá lâu

### Number / Data
- Phí phạt: 4-6% dư nợ, tối thiểu 80.000-150.000 VND
- Lãi suất quá hạn: 20-40%/năm (~1.67-3.33%/tháng)
- Thời hạn thanh toán: 25-30 ngày sau ngày chốt sao kê
- Nhóm 1: < 10 ngày quá hạn
- Nhóm 2: 10-90 ngày quá hạn
- Nhóm 3: 90-180 ngày quá hạn (bắt đầu nợ xấu)
- Nhóm 4: 181-360 ngày
- Nhóm 5: > 360 ngày
- Nợ xấu lưu hồ sơ CIC: 5 năm

## Công thức tính lãi

Số tiền lãi = (Dư nợ thực tế x Lãi suất năm x Số ngày chịu lãi) / 365

## Query Clusters

| Loại | Queries |
|---|---|
| What | trả chậm thẻ tín dụng là gì, khi nào bị tính trả chậm |
| How | cách tính lãi trả chậm, cách xử lý khi trả chậm |
| Why | tại sao trả chậm bị phạt nặng, tại sao ảnh hưởng điểm tín dụng |
| Comparison | phí phạt vs lãi suất quá hạn, thanh toán toàn bộ vs thanh toán tối thiểu |
| Risk | trả chậm có bị nợ xấu không, trả chậm 1 ngày có sao không, bao nhiêu ngày bị nợ xấu |
