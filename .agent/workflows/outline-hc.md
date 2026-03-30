---
description: Home Credit Vietnam - Tạo Outline bài blog theo chuẩn HCVN Persona
---

# Home Credit Outline Workflow

Workflow tạo outline cho **Blog Home Credit Vietnam** (homecredit.vn/blog).
Tuân thủ persona HCVN: title tối đa 60 ký tự, meta 130 đến 160 ký tự, H2/H3 đánh số, FAQs 5 câu, disclaimer, signature.

**Quy tắc writing style bắt buộc:**
- ❌ **KHÔNG dùng emdash (—) hoặc dash (–, -)** trong heading, title, nội dung. Thay bằng từ tiếng Việt tương đương: "đến", "và", "kèm", "với", hoặc dấu phẩy.
- ❌ **KHÔNG dùng flair words** (từ ngữ hoa mỹ, phóng đại). Viết đơn giản, trực tiếp, dễ hiểu.

**Quy tắc Lead Generation Title Priority (bắt buộc):**
- Khi keyword chính/phụ **liên quan đến dịch vụ HC** (bảo hiểm, vay, trả góp, thẻ tín dụng...) hoặc **chứa intent thương mại** (mua ở đâu, giá, bao nhiêu tiền, có nên mua, so sánh...) → **Title và heading PHẢI ưu tiên chứa các từ khóa thương mại đó**
- Mục đích: tối ưu **lead generation**, không chỉ informational
- **Ví dụ áp dụng**:
    - KW "bảo hiểm xe máy giá bao nhiêu" → Title: `Bảo hiểm xe máy giá bao nhiêu? Bảng giá cập nhật 2026` (ưu tiên "giá bao nhiêu")
    - KW "mua bảo hiểm xe máy ở đâu" → Title: `Mua bảo hiểm xe máy ở đâu uy tín, giá tốt 2026` (ưu tiên "mua ở đâu")
    - KW "vay trả góp xe máy" → Title: `Vay trả góp xe máy lãi suất thấp tại Home Credit` (ưu tiên dịch vụ HC)
- **Ví dụ KHÔNG áp dụng**: KW informational thuần túy như "lãi kép là gì", "GDP là gì" → giữ title informational bình thường
- Heading H2/H3 cũng áp dụng tương tự: nếu có sub-topic về giá, mua ở đâu, so sánh → heading **PHẢI chứa** các từ khóa đó thay vì dùng từ chung chung

**Command:** `/outline-hc [keyword chính] [keyword phụ 1] [keyword phụ 2] ...`

**Tài liệu tham chiếu bắt buộc:**
- [persona-home-credit-skill.md](file:///c:/Users/MSI/Documents/Antigravity-SEO/Persona%20Brand/Home%20Credit/persona-home-credit-skill.md)
- [writing-style-analysis.md](file:///c:/Users/MSI/Documents/Antigravity-SEO/Persona%20Brand/Home%20Credit/writing-style-analysis.md)
- [dich-vu-hcvn.md](file:///c:/Users/MSI/Documents/Antigravity-SEO/Persona%20Brand/Home%20Credit/dich-vu-hcvn.md) — Danh mục dịch vụ Home Credit (dùng cho service matching)
- [internal-links-database.md](file:///c:/Users/MSI/Documents/Antigravity-SEO/Persona%20Brand/Home%20Credit/internal-links-database.md) — Database 456 internal links + anchor text (dùng khi gợi ý link trong outline)

---

## 1. Chuẩn bị
- **Input**: Từ khóa chính + tất cả từ khóa phụ do user cung cấp (không giới hạn số lượng)
- **Action**: Tạo folder output: `Keywords/Home Credit/[keyword-slug]/outline/`
- **Load persona files**:
    - `Persona Brand/Home Credit/persona-home-credit-skill.md`
    - `Persona Brand/Home Credit/writing-style-analysis.md`
    - `Persona Brand/Home Credit/dich-vu-hcvn.md`
    - `Persona Brand/Home Credit/internal-links-database.md`

## 2. Research đối thủ (nội bộ)
**Goal**: Tổng hợp heading structure của top 3 đối thủ → dùng làm **template gốc** cho outline.

- **Action 1**: `search_web [keyword chính]`
- **Action 2**: Dùng `read_url_content` để đọc **top 3 bài organic**, trích xuất **toàn bộ H2/H3** của từng bài
- **Action 3**: Tổng hợp heading đối thủ thành bảng so sánh nội bộ:

```
| Topic | ĐT1 | ĐT2 | ĐT3 | Outline HC |
|---|---|---|---|---|
| [topic] | ✅/❌ | ✅/❌ | ✅/❌ | ✅ / ✅ (content gap) |
```

- **Nguyên tắc**:
    - Coi outline đối thủ là **template**: mọi topic đối thủ cover → outline HC **PHẢI có**
    - Topic nào ≥2 đối thủ cover → heading **bắt buộc** trong outline
    - Topic nào 0 đối thủ cover nhưng liên quan KW phụ → heading **mới** + gắn `(content gap)`
    - Heading HC phải **chi tiết hơn** đối thủ: tách H3 rõ ràng hơn, thêm sub-topic cụ thể
- **Bảng so sánh nội bộ KHÔNG đưa vào outline output**, chỉ dùng nội bộ để quyết định heading
- **Danh sách đối thủ (brand + URL) PHẢI đưa vào outline output** → section `## Đang so với các đối thủ` sau Disclaimer

## 2.5. Service Matching — Tự động promote dịch vụ Home Credit
**Goal**: Xác định keyword/chủ đề bài viết có liên quan đến dịch vụ nào của Home Credit → tạo heading promote dịch vụ đó.

- **Action**: Đọc `Persona Brand/Home Credit/dich-vu-hcvn.md` và **think** xem keyword chính + keyword phụ + chủ đề bài viết có liên quan đến dịch vụ/sản phẩm nào không.
- **Bảng mapping dịch vụ** (tham chiếu từ `dich-vu-hcvn.md`):

| Nhóm keyword/chủ đề | Dịch vụ HC liên quan | Link |
|---|---|---|
| Vay, lãi suất, tiền mặt, tín chấp, khoản vay | Vay tiền mặt | https://www.homecredit.vn/vay-tien-online-nhanh |
| Thẻ tín dụng, credit card, hạn mức | Thẻ tín dụng | https://www.homecredit.vn/the-tin-dung-online |
| Trả sau, mua trước trả sau, BNPL | Tài khoản trả sau | https://www.homepaylater.vn/?utm_source=homeweb |
| Điện thoại, laptop, tablet, điện máy, phụ kiện | Vay trả góp điện máy | https://www.homecredit.vn/vay-tra-gop-thiet-bi-dien-tu |
| Xe máy, Honda, Yamaha, Suzuki, SYM, Yadea, VinFast, Piaggio | Vay trả góp xe máy | https://www.homecredit.vn/mua-xe-may-tra-gop |
| Thẩm mỹ, thể thao, giáo dục, nội thất, nha khoa, xây dựng | Trả góp dịch vụ/sản phẩm khác | https://www.homecredit.vn/vay-tra-gop-online-san-pham-dich-vu-khac |
| Bảo hiểm (chung) | Bảo hiểm | https://www.homecredit.vn/bao-hiem |
| Tai nạn, chất lỏng, hư hỏng thiết bị | BH Thiệt hại do tai nạn và chất lỏng | https://www.homecredit.vn/bao-hiem/bao-hiem-thiet-hai-do-tai-nan-va-chat-long |
| Thẻ, bảo vệ thẻ, mất thẻ | BH Thẻ 3 trong 1 | https://www.homecredit.vn/bao-hiem/bao-hiem-the-3-trong-1 |
| Màn hình, rơi vỡ, nứt kính | BH Rơi vỡ Màn hình | https://www.homecredit.vn/bao-hiem/bao-hiem-roi-vo-man-hinh |
| An tâm tài chính, bảo vệ tài chính, rủi ro tài chính | Gói An tâm Tài chính | https://www.homecredit.vn/bao-hiem/goi-an-tam-tai-chinh |
| Xe máy, bảo vệ xe máy | BH BV Xe máy Toàn diện | https://www.homecredit.vn/bao-hiem/bao-hiem-bao-ve-xe-may-toan-dien-moi |
| Xe máy điện, xe điện | BH BV Xe máy điện Toàn diện | https://www.homecredit.vn/bao-hiem/bao-hiem-bao-ve-xe-may-dien-toan-dien |
| Thiết bị di động, điện thoại, bảo vệ điện thoại | BH BV Toàn diện Thiết bị di động | https://www.homecredit.vn/bao-hiem/bao-hiem-bao-ve-toan-dien-thiet-bi-di-dong |
| Nội thất, trang thiết bị, đồ gia dụng | BH Trang thiết bị Nội thất | https://www.homecredit.vn/bao-hiem/bao-hiem-trang-thiet-bi-noi-that |
| Tai nạn cá nhân, tai nạn | BH Tai nạn Cá nhân | https://www.homecredit.vn/bao-hiem/bao-hiem-tai-nan |
| Sức khỏe, nội trú, nằm viện | BH Sức khỏe Nội trú | https://www.homecredit.vn/bao-hiem/bao-hiem-suc-khoe-noi-tru |
| Sức khỏe toàn diện, khám chữa bệnh | BH Sức khỏe Toàn diện | https://www.homecredit.vn/bao-hiem/bao-hiem-suc-khoe-toan-dien |
| Bệnh hiểm nghèo, ung thư, bệnh nặng | BH Bệnh hiểm nghèo | https://www.homecredit.vn/bao-hiem/bao-hiem-benh-hiem-ngheo |

- **Nguyên tắc**:
    - Nếu keyword/chủ đề **match** với bất kỳ nhóm nào → **BẮT BUỘC** thêm **1 heading H2** promote dịch vụ đó, đặt **trước Kết bài**
    - Heading **PHẢI chứa USP cụ thể** của dịch vụ HC (ví dụ: "từ 0 đồng", "lãi suất 0%", "duyệt nhanh 3 phút"), KHÔNG dùng heading chung chung
    - **Pattern heading promote**: `## [Số]. [Hành động] [sản phẩm/chủ đề bài] [USP cụ thể] cùng Home Credit`
    - **Ví dụ đúng**:
        - `## 4. Mua trả góp điện thoại Samsung A37 từ 0 đồng kèm lãi suất 0% cùng Home Credit`
        - `## 5. Mua xe máy trả góp từ 0 đồng kèm lãi suất 0% cùng Home Credit`
        - `## 6. Vay tiền mặt duyệt nhanh 3 phút tại Home Credit`
    - **Ví dụ sai** (quá chung chung): `Mua xe máy trả góp cùng Home Credit`, `Vay tiền mặt nhanh tại Home Credit`
    - Nội dung heading này: giới thiệu ngắn gọn dịch vụ HC + gắn **internal link** từ bảng mapping
    - Nếu match **nhiều dịch vụ** → chọn dịch vụ **liên quan nhất** với keyword chính, chỉ tạo **1 heading promote**
    - Nếu keyword **không match** dịch vụ nào → **KHÔNG thêm heading promote**, bỏ qua bước này
    - Heading promote **KHÔNG được** cảm thấy gượng ép — phải tự nhiên, liên quan trực tiếp đến chủ đề bài viết

- **4 H3 bắt buộc trong heading promote** (áp dụng khi có H2 promote):
    - `### [Số].1. Điều kiện đăng ký [dịch vụ HC liên quan]` — Điều kiện cá nhân (tuổi, CCCD, thu nhập...)
    - `### [Số].2. Thủ tục [dịch vụ HC liên quan]` — Hồ sơ cần chuẩn bị
    - `### [Số].3. Các bước [dịch vụ HC liên quan] tại Home Credit` — Quy trình từng bước
    - `### [Số].4. Bảng thanh toán từng tháng khi [dịch vụ HC liên quan] [sản phẩm]` — Bảng tính mẫu theo giá sản phẩm, chia kỳ hạn 6/12/18/24 tháng
    - **Ví dụ đầy đủ**:
        ```
        ## 4. Mua trả góp điện thoại Samsung A57 từ 0 đồng kèm lãi suất 0% cùng Home Credit
        ### 4.1. Điều kiện đăng ký vay trả góp Samsung A57
        ### 4.2. Thủ tục vay trả góp Samsung A57
        ### 4.3. Các bước vay trả góp Samsung A57 tại Home Credit
        ### 4.4. Bảng thanh toán từng tháng khi vay trả góp Samsung A57
        ```

## 2.7. Outline Consolidation Pattern (bắt buộc)
**Goal**: Giữ outline gọn, tập trung, không dàn trải quá nhiều H2.

- **Nguyên tắc gộp heading**:
    - Các topic liên quan nhau **PHẢI gộp** thành 1 H2 chứa nhiều H3, thay vì tách riêng từng H2
    - Ví dụ: "Thiết kế" và "Pin" có thể gộp thành 1 H3 chung `Thiết kế kháng nước IP68 kèm pin 5000mAh`
    - Ưu tiên **tối đa 4 đến 5 H2 nội dung chính** (không đếm Kết bài, FAQ, Disclaimer)
- **Nguyên tắc đẩy xuống FAQ**:
    - Các topic phụ, topic chỉ cần trả lời ngắn (1 đến 3 câu) → **đẩy xuống FAQ** thay vì tạo H2 riêng
    - Ví dụ: "Ra mắt khi nào?", "Điểm AnTuTu?", "Có đáng mua không?" → chuyển thành câu hỏi FAQ
    - Topic nào đối thủ cover nhưng **không cần giải thích dài** → ưu tiên đưa vào FAQ
- **FAQ luôn 5 câu hỏi** (không ít hơn, không nhiều hơn)
    - Ưu tiên câu hỏi từ KW phụ và các topic đã đẩy xuống từ H2
    - Câu hỏi phải cụ thể, có giá trị cho người đọc
- **Nguyên tắc format bảng so sánh**:
    - Heading nào có nội dung **so sánh, phân biệt, đối chiếu** 2 khái niệm trở lên → description **PHẢI ghi rõ dùng format bảng**
    - Ví dụ: `> Bảng so sánh theo tiêu chí: tính chất, đối tượng bảo vệ, phạm vi bồi thường, mức phí.`
    - Áp dụng cho cả H2 và H3

## 3. Tạo Outline
**Goal**: Tạo outline theo đúng template HCVN.

// turbo
- **Skill**: `.agent/skills/generating-outlines-home-credit/SKILL.md`
- **Inputs**:
    - KW chính + KW phụ
    - Kết quả research đối thủ (Phase 2)
    - Persona files (Phase 1)
- **Template output**:

```
<style>
@import url('https://fonts.googleapis.com/css2?family=Libre+Franklin:ital,wght@0,400;0,700;1,400&display=swap');
* { font-family: 'Libre Franklin', sans-serif !important; font-size: 12pt !important; }
h1, h2, h3 { font-size: 12pt !important; }
</style>

# Outline: [Title]

| Field | Value |
|---|---|
| Title | [tối đa 60 ký tự] |
| Meta Description | [130 đến 160 ký tự] |
| KW chính | [keyword] |
| KW phụ | [liệt kê TẤT CẢ KW phụ user cung cấp, mỗi KW 1 hàng] |
| Mật độ KW | 1% đến 1.5% |
| Mật độ link nội bộ | 0.8% đến 1.2% |


---

## 1. [H2 heading đánh số, chứa KW chính/phụ]
> [1 dòng mô tả ngắn gọn nội dung chính của H2]

### 1.1. [H3 sub-heading]
> [1 dòng mô tả ngắn gọn nội dung H3]

### 1.2. [H3 sub-heading]
> [1 dòng mô tả ngắn gọn nội dung H3]

## 2. [H2 heading tiếp theo]
> [1 dòng mô tả ngắn gọn]

### 2.1. [H3]
> [1 dòng mô tả ngắn gọn]

...(tiếp tục cho các H2/H3 còn lại)...

## [Số]. [Heading promote dịch vụ HC — nếu có match]
> [1 dòng: giới thiệu dịch vụ HC liên quan, USP, link]

### [Số].1. Điều kiện đăng ký [dịch vụ HC]
> [1 dòng: điều kiện cá nhân (tuổi, CCCD, thu nhập...)]

### [Số].2. Thủ tục [dịch vụ HC]
> [1 dòng: hồ sơ cần chuẩn bị]

### [Số].3. Các bước [dịch vụ HC] tại Home Credit
> [1 dòng: quy trình từng bước, online hay offline]

### [Số].4. Bảng thanh toán từng tháng khi [dịch vụ HC] [sản phẩm]
> [1 dòng: bảng tính mẫu theo giá sản phẩm, chia kỳ hạn 6/12/18/24 tháng]

## Kết bài
> [1 dòng: tóm tắt, CTA mềm hướng đến dịch vụ HC]

## FAQ (5 câu)
### [Câu hỏi 1]?
> [1 dòng tóm tắt câu trả lời]

### [Câu hỏi 2]?
> [1 dòng tóm tắt câu trả lời]

### [Câu hỏi 3]?
> [1 dòng tóm tắt câu trả lời]

### [Câu hỏi 4]?
> [1 dòng tóm tắt câu trả lời]

### [Câu hỏi 5]?
> [1 dòng tóm tắt câu trả lời]

## Disclaimer

---
[Disclaimer đầy đủ]
## Đang so với các đối thủ
- **[Brand 1]**: [URL]
- **[Brand 2]**: [URL]
- **[Brand 3]**: [URL]
---
[Signature đầy đủ, chọn theo chủ đề bài]
```

- **Output**: `Keywords/Home Credit/[keyword-slug]/outline/outline.md`

## 4. Kiểm tra nội bộ (KHÔNG xuất ra)
Tự verify trước khi lưu:
- [ ] Title chứa KW chính, tối đa 60 ký tự
- [ ] Meta 130 đến 160 ký tự, chứa KW chính
- [ ] H2 đánh số, tối thiểu 3 H2, 1 đến 2 H2 chứa KW chính
- [ ] H3 phân cấp, không bold (font-weight normal)
- [ ] FAQ đúng 5 câu, sau Kết bài, trước Disclaimer
- [ ] Outline gọn: tối đa 4 đến 5 H2 nội dung chính, topic phụ đẩy xuống FAQ
- [ ] Internal links chỉ homecredit.vn, không gom cụm
- [ ] Nếu keyword match dịch vụ HC → có heading promote trước Kết bài, link đúng từ `dich-vu-hcvn.md`
- [ ] Heading promote có đủ **4 H3**: điều kiện, thủ tục, các bước, bảng thanh toán
- [ ] Disclaimer + Signature đầy đủ, đúng chủ đề
- [ ] **KHÔNG có emdash (—) hoặc dash (–, -)** trong toàn bộ outline
- [ ] **KHÔNG có flair words** (từ ngữ hoa mỹ, phóng đại)

## 5. Lưu và Thông báo
// turbo
- Lưu outline vào: `Keywords/Home Credit/[keyword-slug]/outline/outline.md`
- Thông báo user hoàn thành, kèm link file
