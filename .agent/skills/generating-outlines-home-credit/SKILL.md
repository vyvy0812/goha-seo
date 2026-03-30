---
name: generating-outlines-home-credit
description: >
  Generates SEO outlines specifically for Home Credit Vietnam blog articles.
  Follows HCVN persona rules: title ≤60 chars, meta 130–160 chars, numbered H2/H3,
  3 FAQs, disclaimer, signature, keyword density 1–1.5%, internal links 0.8–1.2%.
  Triggers: home credit outline, hcvn outline, /generate-outline-hc
---

# Generating Outlines — Home Credit Vietnam

## Purpose
Generates article outlines for the **Home Credit Vietnam Blog** (homecredit.vn/blog), strictly following the HCVN persona rules and writing style patterns extracted from live articles.

## Mandatory References
Before generating, load these files:
1. `Persona Brand/Home Credit/persona-home-credit-skill.md` — Rules & constraints
2. `Persona Brand/Home Credit/writing-style-analysis.md` — Style patterns from live articles
3. `Persona Brand/Home Credit/dich-vu-hcvn.md` — Danh mục dịch vụ Home Credit (service matching)

## Process

### Phase 1: Input Validation

```
REQUIRED:
  → Primary Keyword (từ khóa chính)
  → 4–5 Secondary Keywords (từ khóa phụ)

OPTIONAL (if available):
  → search-intent.md
  → research.md
  → competitor-insights.md
```

### Phase 2: Strategy Definition

Define before outlining:
- **Primary Keyword**: [KW chính]
- **Secondary Keywords**: [4–5 KW phụ]
- **Search Intent**: [Informational / Commercial / Transactional]
- **Content Format**: [Listicle / Guide / Comparison / 101 Primer]
- **Target Audience**: Người tiêu dùng phổ thông, quan tâm đến tài chính cá nhân
- **Signature to use**: [Chọn 1 trong 8 signatures — xem bảng tra cứu Mục 12 persona]

### Phase 2.5: So sánh Outline đối thủ (nội bộ — KHÔNG xuất ra output)

Trước khi tạo outline, research heading structure của **top 3 kết quả Google** cho KW chính:

1. Search Google cho KW chính
2. Lấy top 3 bài organic (không tính ads, featured snippet)
3. Trích xuất toàn bộ H2/H3 của từng đối thủ
4. So sánh → xác định topic đối thủ có mà mình chưa cover
5. **Gom nhóm & Tối ưu Heading (Bắt buộc)**:
    - **Chỉ tối đa 5 H2** (không tính FAQ và Kết bài).
    - Phải **merge (tổng hợp) các nội dung tương tự** thành các khối lớn. Tránh tình trạng nhiều H2 làm bài bị rối rắm.
    - Tiêu chí lên Heading: Nội dung lớn xứng đáng làm H2 thì cho làm H2. Nội dung nhỏ chỉ xứng đáng làm 1 H3, 1 câu, hay 1 đoạn văn thì **phải để chính xác như vậy**, không được cố rặn ra thành H2.
    - Cập nhật đủ ý của đối thủ bằng cách gom vào H2 lớn hoặc làm H3/bullet point.

> **Lưu ý**: Bảng so sánh đối thủ chỉ dùng trong quá trình research, KHÔNG đưa vào outline output. Tuy nhiên, danh sách **brand + URL** của các đối thủ đã phân tích **PHẢI đưa vào** outline output trong section `## Đang so với các đối thủ`.

### Phase 2.7: Service Matching — Tự động promote dịch vụ Home Credit

Đọc `Persona Brand/Home Credit/dich-vu-hcvn.md` và **think** xem keyword chính + keyword phụ + chủ đề bài viết có liên quan đến dịch vụ/sản phẩm nào của Home Credit không.

**Bảng mapping dịch vụ:**

| Nhóm keyword/chủ đề | Dịch vụ HC | Link |
|---|---|---|
| Vay, lãi suất, tiền mặt, tín chấp, khoản vay | Vay tiền mặt | https://www.homecredit.vn/vay-tien-online-nhanh |
| Thẻ tín dụng, credit card, hạn mức | Thẻ tín dụng | https://www.homecredit.vn/the-tin-dung-online |
| Trả sau, mua trước trả sau, BNPL | Tài khoản trả sau | https://www.homepaylater.vn/?utm_source=homeweb |
| Điện thoại, laptop, tablet, điện máy, phụ kiện | Vay trả góp điện máy | https://www.homecredit.vn/vay-tra-gop-thiet-bi-dien-tu |
| Xe máy, Honda, Yamaha, Suzuki, SYM, Yadea, VinFast, Piaggio | Vay trả góp xe máy | https://www.homecredit.vn/mua-xe-may-tra-gop |
| Thẩm mỹ, thể thao, giáo dục, nội thất, nha khoa, xây dựng | Trả góp DV/SP khác | https://www.homecredit.vn/vay-tra-gop-online-san-pham-dich-vu-khac |
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

**Nguyên tắc:**
- Match → **BẮT BUỘC** thêm **1 H2** promote dịch vụ, đặt **trước Kết bài**
- Heading dạng: `## [Số]. [Hành động] cùng Home Credit` — ví dụ: `## 5. Mua xe máy trả góp cùng Home Credit`
- Nội dung: giới thiệu ngắn gọn + gắn **internal link** từ bảng mapping
- Nhiều dịch vụ match → chọn **1 dịch vụ liên quan nhất**
- Không match → **bỏ qua**, không thêm heading promote
- Heading promote phải **tự nhiên**, không gượng ép

### Phase 3: Outline Generation

#### Template bắt buộc

> **Nguyên tắc**: Outline chỉ chứa **heading structure + metadata + disclaimer + signature (viết ra đầy đủ)**. Có thể research nội dung để heading chính xác, nhưng KHÔNG ghi hướng dẫn nội dung bên trong mỗi section. Constraint checklist và bảng so sánh đối thủ là bước nội bộ, KHÔNG xuất ra trong outline.

```markdown
---
# SEO METADATA TABLE
| Field | Value |
|---|---|
| Title | [KW chính + hook — ĐẾM ≤ 60 KÝ TỰ] |
| Meta Description | [130–160 ký tự, chứa KW chính] |
| KW chính | [từ khóa chính] |
| KW phụ | [KW phụ 1] |
| | [KW phụ 2] |
| | [KW phụ 3] |
| | [KW phụ 4] |
| | [KW phụ 5] |
| KW Density Target | 1% – 1.5% |
| Internal Link Density | 0.8% – 1.2% |
| Word Count Target | Tự điều chỉnh: 1000–1500 |
---

## Intro (70–150 chữ)
## 1. [KW chính] là gì?
## 2. [Phân loại / Đặc điểm / Cách hoạt động]
## 3. [Lợi ích / Hướng dẫn / Phương pháp]
### 3.1. [Sub-topic]
### 3.2. [Sub-topic]
### 3.3. [Sub-topic]
## 4. [Sai lầm / Rủi ro / Lưu ý]
## [Số]. [Heading promote dịch vụ HC — nếu keyword match, xem Phase 2.7]
## Kết bài
## FAQ (3–5 câu)
### [Câu hỏi 1]?
### [Câu hỏi 2]?
### [Câu hỏi 3]?
## Disclaimer

---
[Disclaimer viết ra đầy đủ]
## Đang so với các đối thủ
- **[Brand 1]**: [URL]
- **[Brand 2]**: [URL]
- **[Brand 3]**: [URL]
---
[Signature viết ra đầy đủ, in nghiêng — chọn đúng mẫu theo chủ đề từ persona Mục 11]
```

### Phase 4: Internal Constraint Checklist (KHÔNG xuất ra output)

Sau khi tạo outline, tự kiểm tra trước khi gửi. Đây là bước nội bộ:

#### Title
- [ ] Chứa KW chính
- [ ] ≤ 60 ký tự (đếm chính xác)
- [ ] Dạng "[KW] là gì? + [hook]"

#### Meta Description
- [ ] Chứa KW chính
- [ ] 130–160 ký tự (đếm chính xác)

#### Headings
- [ ] H2 đánh số: `1.`, `2.`, `3.`...
- [ ] H3 phân cấp: `3.1`, `3.2`...
- [ ] Từ 3 đến **tối đa 5 H2** (không đếm FAQs và Kết bài). Không lạm dụng H2.
- [ ] Ý nhỏ đã được merge vào H3 hoặc văn bản, bài không bị rối.
- [ ] 1–2 H2 chứa KW chính
- [ ] H2 KHÔNG dạng câu hỏi (trừ FAQs)

#### Internal Links
- [ ] Chỉ domain `homecredit.vn`
- [ ] Phân bổ tự nhiên qua anchor text (KHÔNG gom cụm)
- [ ] Mỗi link chỉ xuất hiện 1 lần

#### FAQs
- [ ] Đúng 3 câu hỏi
- [ ] Dựa trên KW chính/phụ

#### Service Promote
- [ ] Nếu keyword match dịch vụ HC → có 1 H2 promote trước Kết bài
- [ ] Link đúng từ bảng mapping `dich-vu-hcvn.md`
- [ ] Heading tự nhiên, không gượng ép

#### Nội dung
- [ ] Target 1000–1500 từ
- [ ] Mỗi đoạn ≤ 4 dòng, câu ≤ 25 chữ
- [ ] Giọng văn xưng "bạn", thân thiện
- [ ] Bullet: **đậm** + `:` + giải thích

#### Kết bài
- [ ] Chứa KW chính
- [ ] CTA dẫn về blog HC
- [ ] Disclaimer viết đầy đủ
- [ ] Chữ ký viết đầy đủ, in nghiêng, sau `---`

