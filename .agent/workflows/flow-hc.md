---
description: Premium Home Credit Vietnam Blog SEO Workflow — Full Pipeline (Research → Outline → Article → Audit)
---

# Home Credit Vietnam — Full Writing Pipeline

Workflow viết bài hoàn chỉnh cho **Blog Home Credit Vietnam** (homecredit.vn/blog).
Kết hợp Semantic SEO + HCVN Persona + Quality Audit trong một pipeline duy nhất.

**Command:** `/flow-hc [keyword chính] [keyword phụ 1] [keyword phụ 2] ...`

**Tài liệu persona bắt buộc:**
- [persona-home-credit-skill.md](file:///c:/Users/MSI/Documents/Antigravity-SEO/Persona%20Brand/Home%20Credit/persona-home-credit-skill.md) — Rules & constraints
- [writing-style-analysis.md](file:///c:/Users/MSI/Documents/Antigravity-SEO/Persona%20Brand/Home%20Credit/writing-style-analysis.md) — Style patterns
- [dich-vu-hcvn.md](file:///c:/Users/MSI/Documents/Antigravity-SEO/Persona%20Brand/Home%20Credit/dich-vu-hcvn.md) — Danh mục dịch vụ HC (service matching)
- [internal-links-database.md](file:///c:/Users/MSI/Documents/Antigravity-SEO/Persona%20Brand/Home%20Credit/internal-links-database.md) — Database 456 internal links + anchor text

---

## Global Quality Rules (áp dụng toàn bộ pipeline)

1. **Content Freshness**: MUST dùng `search_web` verify thông tin mới nhất trước khi viết. Không dùng dữ liệu cũ.
2. **No Emoji**: KHÔNG dùng emoji (⭐, ⚠️, 🔥...). Thay bằng **(MỚI)**, **Lưu ý**, **Quan trọng**.
3. **No Emdash/Dash**: KHÔNG dùng emdash (—) hoặc dash (–, -) trong heading, title, nội dung. Thay bằng từ tiếng Việt: "đến", "và", "kèm", "với", hoặc dấu phẩy.
4. **No Flair Words**: KHÔNG dùng từ ngữ hoa mỹ, phóng đại. Viết đơn giản, trực tiếp, dễ hiểu.
5. **100% Vietnamese**: Viết hoàn toàn tiếng Việt. KHÔNG dùng từ tiếng Anh trừ thuật ngữ kỹ thuật không thể dịch.
6. **Sentence Case Headings**: Chỉ viết hoa chữ cái đầu câu + danh từ riêng. KHÔNG viết hoa mỗi từ (Title Case).
7. **Bold Only Keywords**: Chỉ in đậm (bold) các từ khóa chính và phụ trong bài. KHÔNG bold sapo, label bullet, cú pháp, tên nút UI, hay bất kỳ text nào khác. Mục đích: highlight keyword cho SEO, không phải để format nội dung.
8. **No Content Gap Indicator**: KHÔNG ghi `(content gap)` trong heading output. Chỉ dùng nội bộ khi phân tích đối thủ, KHÔNG xuất ra outline hay article.

---

## 1. Chuẩn bị
- **Input**: Từ khóa chính + tất cả từ khóa phụ do user cung cấp (không giới hạn số lượng)
- **Action**: Tạo folder output: `Keywords/Home Credit/[keyword-slug]/`
- **Load persona files** (đọc cả 4 file trước khi bắt đầu):
    - `Persona Brand/Home Credit/persona-home-credit-skill.md`
    - `Persona Brand/Home Credit/writing-style-analysis.md`
    - `Persona Brand/Home Credit/dich-vu-hcvn.md`
    - `Persona Brand/Home Credit/internal-links-database.md`

## 2. Phase 1: Search Intent Analysis (Deep)
**Goal**: Phân tích intent sâu bằng 7-type classification + Google Micro-Intent framework → quyết định format và tone bài viết.

- **Skill**: `.agent/skills/analyzing-search-intent/SKILL.md`
- **Action 1**: `search_web [keyword chính]` → phân tích SERP features live
- **Action 2**: Phân loại theo **7-Type Model**:

| # | Intent Type | Dấu hiệu nhận biết | Content Vehicle |
|---|---|---|---|
| 1 | **Informational** | Featured Snippet, PAA | Guide, Definitions, How-to |
| 2 | **Commercial** | So sánh, review, "tốt nhất" | Top X, Comparison, Buying Guide |
| 3 | **Transactional** | Ads, Products, "mua", "đăng ký" | CTA rõ ràng, Trust signals, Pricing |
| 4 | **Navigational** | Brand name, trang cụ thể | Homepage, Official profile |
| 5 | **Brand** | Tên thương hiệu cụ thể | About page, Brand story |
| 6 | **News** | Trending, "mới nhất", "cập nhật" | Tin tức, Timeline |
| 7 | **Local** | "gần đây", tên thành phố, "ở đâu" | Map, Address, Local schema |

- **Action 3**: Xác định **Micro-Intent** (Know / Do / Go):
    - **Know Simple**: Câu trả lời đơn → Cảnh báo "Zero-click" risk, cần mở rộng nội dung
    - **Know**: Cần giải thích chi tiết → Guide format
    - **Do**: Hành động cụ thể → CTA, bước thực hiện
    - **Go**: Điều hướng → Link trực tiếp

- **Action 4**: Xác định **Secondary Intent** (nếu có). Ví dụ: "vay ngân hàng lãi suất bao nhiêu" = Informational + Commercial

- **Output bắt buộc** (lưu vào `search-intent.md`):
```
Keyword: [keyword]
Primary Intent: [Type] (Confidence: High/Med/Low)
Secondary Intent: [Type nếu có]
Micro-Intent: [Know/Do/Go]
User Motivation: [1 câu mô tả mục đích thực sự của người tìm]
Recommended Format: [Blog Guide / Listicle / Comparison / LP]
SERP Features: [Snippet, PAA, Ads, Maps...]
Content Tone: [Informational / Commercial-Informational / Transactional]
```

- **Quyết định tự động dựa trên intent**:
    - Intent Informational thuần → Title dạng "X là gì?", giọng văn kiến thức
    - Intent Commercial → Title chứa từ khóa thương mại, heading so sánh/giá
    - Intent Transactional → Title chứa CTA, heading H2 promote HC đặt cao hơn

- **Output**: `Keywords/Home Credit/[keyword-slug]/search-intent.md`

## 3. Phase 2: Semantic Research & Entity Discovery
**Goal**: Xây dựng entity map + query clusters + content hierarchy dựa trên dữ liệu thực.

- **Skill 1**: `.agent/skills/extracting-keywords/SKILL.md`
- **Skill 2**: `.agent/skills/analyzing-semantic-seo/SKILL.md`

### 2a. Entity Extraction
- **Action**: Dùng `search_web` với operators:
    - `"định nghĩa [keyword]"` → tìm core entities
    - `site:.gov.vn OR site:.edu.vn "[keyword]"` → authority context
    - `"[keyword]" site:homecredit.vn` → xem HC đã có content nào liên quan
- **Entity Types bắt buộc trích xuất**:
    - **Person**: Chuyên gia, tổ chức liên quan (ví dụ: NHNN, Bộ Tài chính)
    - **Organization**: Ngân hàng, CTTC, cơ quan quản lý
    - **Concept**: Khái niệm chuyên ngành (lãi suất cơ bản, lãi kép, tín chấp...)
    - **Location**: Địa điểm nếu có intent Local
    - **Time**: Mốc thời gian, deadline, cập nhật mới nhất
- **Output**: Bảng Entity Map trong `research.md`

### 2b. Query Cluster Generation
- **Action**: Phân loại queries theo 5 nhóm:
    - **What** (Định nghĩa): "[keyword] là gì"
    - **How** (Quy trình): "cách tính [keyword]", "hướng dẫn [keyword]"
    - **Why** (Giải thích): "tại sao [keyword] tăng/giảm"
    - **Comparison** (So sánh): "[A] và [B]", "nên chọn [X] hay [Y]"
    - **Best/Top** (Xếp hạng): "[keyword] tốt nhất", "top [keyword]"
- Mỗi query cluster → map sang 1 H2/H3 trong outline

### 2c. Content Hierarchy
- Xác định vai trò bài viết:
    - **Pillar Page**: Topic rộng, bao quát (ví dụ: "lãi suất ngân hàng")
    - **Cluster Page**: Topic cụ thể, chi tiết (ví dụ: "cách tính lãi suất vay")
- Xác định internal linking strategy:
    - Pillar → Clusters (link xuôi)
    - Clusters → Pillar (link ngược)
    - Cluster ↔ Cluster (link ngang giữa các bài liên quan)

- **Inputs**: Target Keyword + `search-intent.md`
- **Output**: `Keywords/Home Credit/[keyword-slug]/research.md` (bao gồm Entity Map, Query Clusters, Content Hierarchy)

## 4. Phase 3: Competitor Intelligence
**Goal**: Tổng hợp heading structure top 3 đối thủ → dùng làm template gốc cho outline.

// turbo
- **Skill**: `.agent/skills/analyzing-competitors/SKILL.md`
- **Action 1**: `search_web [keyword chính]`
- **Action 2**: Dùng `read_url_content` đọc top 3 bài organic, trích xuất **toàn bộ H2/H3**
- **Action 3**: Tổng hợp heading đối thủ thành bảng so sánh nội bộ:

```
| Topic | ĐT1 | ĐT2 | ĐT3 | Outline HC |
|---|---|---|---|---|
| [topic] | ✅/❌ | ✅/❌ | ✅/❌ | ✅ / ✅ (content gap) |
```

- **Nguyên tắc**:
    - Coi outline đối thủ là **template**: mọi topic đối thủ cover → outline HC **PHẢI có**
    - Topic nào ≥2 đối thủ cover → heading **bắt buộc** trong outline
    - Topic nào 0 đối thủ cover nhưng liên quan KW phụ → heading **mới** (ghi nhận nội bộ là content gap, nhưng KHÔNG gắn `(content gap)` vào heading output)
    - Heading HC phải **chi tiết hơn** đối thủ: tách H3 rõ ràng hơn, thêm sub-topic cụ thể
- **Bảng so sánh KHÔNG đưa vào outline output** — chỉ dùng nội bộ
- **Danh sách đối thủ (brand + URL) PHẢI đưa vào outline output**
- **Output**: `Keywords/Home Credit/[keyword-slug]/competitors/` (lưu từng file đối thủ riêng)

## 5. Phase 4: Service Matching
**Goal**: Xác định keyword/chủ đề có liên quan đến dịch vụ HC nào → tạo heading promote.

- **Action**: Đọc `dich-vu-hcvn.md` → match keyword chính/phụ vào bảng mapping:

| Nhóm keyword/chủ đề | Dịch vụ HC | Link |
|---|---|---|
| Vay, lãi suất, tiền mặt, tín chấp | Vay tiền mặt | https://www.homecredit.vn/vay-tien-online-nhanh |
| Thẻ tín dụng, credit card, hạn mức | Thẻ tín dụng | https://www.homecredit.vn/the-tin-dung-online |
| Trả sau, mua trước trả sau, BNPL | Tài khoản trả sau | https://www.homepaylater.vn/?utm_source=homeweb |
| Điện thoại, laptop, tablet, điện máy | Vay trả góp điện máy | https://www.homecredit.vn/vay-tra-gop-thiet-bi-dien-tu |
| Xe máy, Honda, Yamaha, Suzuki, SYM, Yadea, VinFast, Piaggio | Vay trả góp xe máy | https://www.homecredit.vn/mua-xe-may-tra-gop |
| Thẩm mỹ, thể thao, giáo dục, nội thất, nha khoa, xây dựng | Trả góp DV/SP khác | https://www.homecredit.vn/vay-tra-gop-online-san-pham-dich-vu-khac |
| Bảo hiểm (chung) | Bảo hiểm | https://www.homecredit.vn/bao-hiem |
| Tai nạn, chất lỏng, hư hỏng thiết bị | BH Thiệt hại do tai nạn và chất lỏng | https://www.homecredit.vn/bao-hiem/bao-hiem-thiet-hai-do-tai-nan-va-chat-long |
| Thẻ, bảo vệ thẻ, mất thẻ | BH Thẻ 3 trong 1 | https://www.homecredit.vn/bao-hiem/bao-hiem-the-3-trong-1 |
| Màn hình, rơi vỡ, nứt kính | BH Rơi vỡ Màn hình | https://www.homecredit.vn/bao-hiem/bao-hiem-roi-vo-man-hinh |
| An tâm tài chính, bảo vệ tài chính | Gói An tâm Tài chính | https://www.homecredit.vn/bao-hiem/goi-an-tam-tai-chinh |
| Xe máy, bảo vệ xe máy | BH BV Xe máy Toàn diện | https://www.homecredit.vn/bao-hiem/bao-hiem-bao-ve-xe-may-toan-dien-moi |
| Xe máy điện, xe điện | BH BV Xe máy điện Toàn diện | https://www.homecredit.vn/bao-hiem/bao-hiem-bao-ve-xe-may-dien-toan-dien |
| Thiết bị di động, bảo vệ điện thoại | BH BV Toàn diện Thiết bị di động | https://www.homecredit.vn/bao-hiem/bao-hiem-bao-ve-toan-dien-thiet-bi-di-dong |
| Nội thất, trang thiết bị, đồ gia dụng | BH Trang thiết bị Nội thất | https://www.homecredit.vn/bao-hiem/bao-hiem-trang-thiet-bi-noi-that |
| Tai nạn cá nhân | BH Tai nạn Cá nhân | https://www.homecredit.vn/bao-hiem/bao-hiem-tai-nan |
| Sức khỏe, nội trú, nằm viện | BH Sức khỏe Nội trú | https://www.homecredit.vn/bao-hiem/bao-hiem-suc-khoe-noi-tru |
| Sức khỏe toàn diện, khám chữa bệnh | BH Sức khỏe Toàn diện | https://www.homecredit.vn/bao-hiem/bao-hiem-suc-khoe-toan-dien |
| Bệnh hiểm nghèo, ung thư, bệnh nặng | BH Bệnh hiểm nghèo | https://www.homecredit.vn/bao-hiem/bao-hiem-benh-hiem-ngheo |

- **Nguyên tắc**:
    - Match → **BẮT BUỘC** thêm **1 H2** promote dịch vụ, đặt **trước Kết bài**
    - Heading dạng: `## [Số]. [Hành động] cùng Home Credit` — ví dụ: `## 5. Mua xe máy trả góp cùng Home Credit`
    - Nội dung: giới thiệu ngắn gọn + gắn **internal link** từ bảng mapping
    - Nhiều dịch vụ match → chọn **1 dịch vụ liên quan nhất**
    - Không match → **bỏ qua**, không thêm heading promote
    - Heading promote phải **tự nhiên**, không gượng ép

**Lead Generation Title Priority (bắt buộc):**
- Khi keyword chính/phụ **liên quan đến dịch vụ HC** hoặc **chứa intent thương mại** (mua ở đâu, giá, bao nhiêu tiền, có nên mua, so sánh...) → **Title và heading PHẢI ưu tiên chứa từ khóa thương mại đó**
- **Ví dụ**: KW "bảo hiểm xe máy giá bao nhiêu" → Title: `Bảo hiểm xe máy giá bao nhiêu? Bảng giá cập nhật 2026`
- KW informational thuần túy (lãi kép là gì, GDP là gì) → giữ title informational bình thường

## 6. Phase 5: Tạo Outline
**Goal**: Tạo outline theo đúng template HCVN.

// turbo
- **Skill**: `.agent/skills/generating-outlines-home-credit/SKILL.md`
- **Inputs**: KW chính + KW phụ + research + competitor insights + service matching result
- **Template output**:

```markdown
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

## Intro (70 đến 150 chữ)
## 1. [KW chính] là gì?
## 2. [Phân loại / Đặc điểm]
## 3. [Lợi ích / Hướng dẫn] (chứa H3 con)
### 3.1. [Sub-topic]
### 3.2. [Sub-topic]
## 4. [Sai lầm / Rủi ro / Lưu ý]
## [Số]. [Heading promote dịch vụ HC — nếu match]
## Kết bài
## FAQ (3 đến 5 câu)
### [Câu hỏi 1]?
### [Câu hỏi 2]?
### [Câu hỏi 3]?
## Disclaimer

---
[Disclaimer đầy đủ]
## Đang so với các đối thủ
- **[Brand 1]**: [URL]
- **[Brand 2]**: [URL]
- **[Brand 3]**: [URL]
---
[Signature đầy đủ, in nghiêng — chọn theo chủ đề từ persona Mục 11+12]
```

- **Output**: `Keywords/Home Credit/[keyword-slug]/outline/outline.md`

### Outline Checklist (nội bộ, KHÔNG xuất ra)
- [ ] Title chứa KW chính, ≤ 60 ký tự
- [ ] Meta 130 đến 160 ký tự, chứa KW chính
- [ ] H2 đánh số, ≥ 3 H2, 1 đến 2 H2 chứa KW chính
- [ ] H3 phân cấp (3.1, 3.2...), không bold
- [ ] FAQ 3 đến 5 câu, sau Kết bài, trước Disclaimer
- [ ] Internal links chỉ `homecredit.vn`, không gom cụm
- [ ] Nếu keyword match dịch vụ HC → có heading promote trước Kết bài
- [ ] Disclaimer + Signature đầy đủ, đúng chủ đề
- [ ] KHÔNG có emdash (—) hoặc dash (–, -)
- [ ] KHÔNG có flair words

## 7. Phase 6: Viết bài (Content Writing)
**Goal**: Viết bài hoàn chỉnh theo đúng persona HCVN.

- **Skill**: `.agent/skills/writing-semantic-content/SKILL.md`
- **Inputs**: `research.md` + `outline.md` + persona files
- **Output**: `Keywords/Home Credit/[keyword-slug]/article.md`

### Quy tắc viết bài HCVN (override semantic-seo defaults)

#### SEO Metadata Table (bắt buộc đầu bài)
```markdown
| | |
|---|---|
| **Keyword chính** | [primary keyword] |
| **Keyword phụ** | [liệt kê TẤT CẢ KW phụ, mỗi KW 1 hàng] |
| | [secondary keyword 2] |
| | ... (tất cả KW phụ) |
| **Slug** | [keyword-slug] |
| **Meta title** | [≤ 60 ký tự, chứa KW chính] |
| **Meta description** | [130 đến 160 ký tự, chứa KW chính] |
| **Outline** | H1: [title] |
| | - H2: [section] |
| | -- H3: [subsection] |
| | ... |

---
```

#### Intro
- 100 đến 200 chữ, chứa KW chính trong 100 từ đầu
- Xưng "bạn", ngôi thứ hai
- Mở bài bằng **bối cảnh vấn đề** hoặc **giá trị cần truyền tải**, không mở bằng câu hỏi quang quang
- Kết bằng "Cùng Home Credit khám phá..." hoặc "Trong bài viết này, Home Credit sẽ..."

#### Nội dung chính
- **Đoạn văn**: Ưu tiên độ sâu phân tích, không giới hạn số dòng cứng. Mỗi đoạn nên triển khai **đủ ý** trước khi xuống dòng mới.
- **Câu**: Viết tự nhiên, không giới hạn số chữ cứng. Ưu tiên câu rõ ràng, mạch lạc, tránh câu thừa từ nhưng cũng không ngắt cách giả tạo.
- **Giọng văn**: Chuyên môn nhưng dễ hiểu, xưng "bạn". Không quá suồng sã như nói chuyện, cũng không quá khô khan như sách giáo khoa.
- **Chiều sâu phân tích (phân loại H3)**:
    - **H3 chính** (liên quan trực tiếp KW chính/phụ): phân tích sâu, ví dụ cụ thể, giải thích cơ chế, đủ nội dung để đứng độc lập
    - **H3 phụ** (bổ trợ, không chứa KW): viết ngắn gọn 2-3 câu hoặc gom thành bullet list. Không kéo dài nội dung phụ, tập trung vào nội dung chính có trong keyword
    - Nội dung nào có **trình tự, bước, quy trình** → BẮT BUỘC viết dạng bullet list thay vì đoạn văn dài
- **Câu chuyển liên kết**: Dùng **câu chuyển chuyển tiếp** giữa các đoạn: "Nhờ cơ chế cộng dồn này,...", "Vì vậy,...", "Trong thực tế,...", "Tuy nhiên,..."
- **Nhận xét sau bảng/dữ liệu**: Sau mỗi bảng so sánh hoặc ví dụ tính toán, **BẮT BUỘC** có 1 đoạn nhận xét/phân tích kết quả (không để bảng lơ lửng).
- **Bullet list**: Đầu bullet KHÔNG in đậm. Chỉ bold từ khóa chính/phụ khi xuất hiện tự nhiên trong bullet.
- **Bold rule**: Chỉ bold keyword chính + keyword phụ. KHÔNG bold sapo, label bullet, cú pháp, nút UI, hay text khác. Bold keyword trong heading H2/H3 được phép.
- **Bảng so sánh**: Dùng khi cần phân biệt 2 khái niệm liên quan
- **Ví dụ minh họa**: Luôn có ví dụ cụ thể (con số, tình huống) sau phần định nghĩa hoặc công thức

#### Keyword Density
- Mật độ từ khóa: **1% đến 1.5%** (tổng số từ khóa / tổng số từ)
- KW chính: mật độ **1% đến 1.5%** trên tổng số từ
- KW phụ xuất hiện **ít nhất 2 lần** mỗi từ

#### Internal Links
- **Nguồn link bắt buộc**: Đọc `Persona Brand/Home Credit/internal-links-database.md` để chọn URL + anchor text phù hợp context bài viết
- Chỉ domain `www.homecredit.vn`
- **KHÔNG** chèn link external
- Mật độ: **0.8% đến 1.2%**
- Phân bổ tự nhiên qua anchor text, KHÔNG gom cụm
- **KHÔNG** dùng dạng `>>> Xem thêm: [Title](link)`. Chỉ đi link qua **anchor text** tự nhiên trong câu văn.
- Mỗi URL chỉ xuất hiện **1 lần duy nhất** trong toàn bài
- Chọn 10 đến 15 link từ database có chủ đề liên quan nhất đến nội dung bài

#### Hình ảnh
- Mỗi H2 section: **1 ảnh + 1 caption** (1 câu mô tả ngắn)
- Tổng: 4 đến 6 ảnh/bài
- Format: WebP, 1920x1080, ≤ 150KB
- ❌ Không watermark, không hoạt hình 2D/3D, không tiền ngoại tệ, không nhà/ô tô, không logo thương hiệu khác
- ✅ Prefer ảnh từ Shutterstock
- ✅ Bài TW/CD: ảnh đúng hãng, đúng dòng SP
- ✅ Ảnh AI → ghi signal "AI" bên dưới (chỉ bài kiến thức tài chính, không dùng hình AI chứa người)

#### FAQs
- 3 đến 5 câu hỏi, dạng H3 đầy đủ
- Mỗi câu trả lời 2 đến 4 câu
- Dựa trên KW chính/phụ

#### Kết bài
- 2 đến 3 câu tóm tắt
- Chứa KW chính
- CTA dẫn về blog: "ghé thăm blog Tài chính số Toàn diện của Home Credit"

#### Disclaimer (bắt buộc, trước chữ ký)
> *Lưu ý: Thông tin trong bài mang tính chất tham khảo, được tổng hợp từ thị trường và không đại diện cho toàn bộ sản phẩm, dịch vụ của Home Credit.*

#### Chữ ký (Signature) — chọn theo chủ đề
Chọn **đúng 1 signature** từ bảng tra cứu (persona Mục 11+12), viết ra **đầy đủ, in nghiêng**, phân cách bằng `---`:

| Chủ đề | Signature |
|---|---|
| Vay tiền mặt, vay online | Signature 1 – Cash Loan |
| Vay trả góp xe máy | Signature 2 – Two Wheel |
| Trả góp điện thoại, laptop, điện máy | Signature 3 – Consumer Durables |
| Thẻ tín dụng | Signature 4 – Credit Card |
| Bảo hiểm | Signature 5 – VAS Bảo hiểm |
| Mua trước trả sau, Home PayLater | Signature 6 – Home PayLater |
| Kiến thức tài chính, quản lý chi tiêu | Signature 7 – Cẩm nang Tài chính |
| Ứng dụng Home Credit | Signature bổ sung – Ứng dụng HC |

## 8. Phase 7: Fact-Checking & Deep Research (Auto-Correction)
**Goal**: Xác minh 100% claims trong bài, chống hallucination. Tự động sửa lỗi, KHÔNG cần user check.

- **Skill**: `.agent/skills/rechecking-facts/SKILL.md`
- **Input**: `article.md`

### 7a. Claim Extraction (bắt buộc trích xuất đầy đủ)
Đọc toàn bộ `article.md`, tìm và liệt kê **mọi claim** thuộc 5 loại:

| # | Loại claim | Ví dụ | Mức độ rủi ro |
|---|---|---|---|
| 1 | **Giá cả, chi phí** | "Lãi suất từ 5,5%/năm", "Hạn mức 250 triệu" | Cao |
| 2 | **Thông số kỹ thuật** | "Duyệt vay 3 phút", "Giải ngân 10 phút" | Cao |
| 3 | **Quy định pháp lý** | "Theo Nghị định X", "NHNN quy định" | Rất cao |
| 4 | **Số liệu thống kê** | "Lạm phát 3 đến 4%", "Tăng trưởng tín dụng" | Cao |
| 5 | **Thông tin dịch vụ HC** | Features, ưu đãi, điều kiện vay Home Credit | Cao |

### 7b. Deep Verification (dùng search_web)
Với **mỗi claim** đã trích xuất, thực hiện verify bằng `search_web`:

- `site:homecredit.vn [thông tin dịch vụ]` → verify thông tin HC chính xác
- `site:sbv.gov.vn [quy định]` → verify quy định NHNN
- `"[số liệu cụ thể]" site:.vn` → verify số liệu VN
- `site:[ngân hàng].com.vn "lãi suất"` → verify lãi suất từng NH
- `"[technical_spec]"` → tìm thông số chính thức

### 7c. Auto-Resolution (TỰ ĐỘNG SỬA, không hỏi user)
Sau khi verify, phân loại mỗi claim:

| Status | Hành động | Ví dụ |
|---|---|---|
| ✅ **Verified** | Giữ nguyên | Claim đúng với nguồn chính thức |
| ⚠️ **Needs Nuance** | Sửa trực tiếp trong `article.md` | "Tiết kiệm 50%" → "Tiết kiệm đến 50% tùy điều kiện" |
| ❌ **False/Hallucinated** | Sửa hoặc xóa khỏi `article.md` | Số liệu sai, thông tin cũ, claim không có nguồn |

**Nguyên tắc Auto-Fix**:
- Claim sai → sửa ngay trong `article.md`, KHÔNG chỉ ghi note
- Claim không verify được → xóa hoặc thay bằng thông tin chung an toàn
- Thông tin HC sai → verify trên `homecredit.vn` rồi sửa chính xác
- Số liệu cũ → update bằng data mới nhất từ search

### 7d. Fact-Check Report Output
```markdown
# Fact-Check Report

## 1. Verified Claims
- [Claim] → Source: [URL]

## 2. Corrections Made (đã sửa trong article.md)
- **Original**: [Claim sai]
- **Corrected To**: [Claim đúng]
- **Source**: [URL/Context]

## 3. Removed Claims (không verify được)
- [Claim đã xóa] → Lý do: [không tìm thấy nguồn]
```

- **Output**: `Keywords/Home Credit/[keyword-slug]/fact-check-report.md` + Corrected `article.md`

## 9. Phase 8: Rephrase & Uniqueness Check
**Goal**: Viết lại toàn bộ câu văn để đạt **≥ 90% độ unique**, chống trùng lặp với các bài cùng chủ đề trên SERP. Tự động thực hiện, KHÔNG cần user rephrase thủ công.

### 8a. Xác định phạm vi rephrase
Chỉ rephrase **phần editorial** (câu văn, đoạn mô tả). KHÔNG thay đổi:
- Metadata table (SEO table đầu bài)
- Bảng số liệu (lãi suất, giá, thông số)
- Công thức toán học
- Internal links và anchor text
- Disclaimer + Signature (nội dung brand cố định)

### 8b. Kỹ thuật rephrase (áp dụng từng đoạn)
Với **mỗi đoạn văn** trong bài, thực hiện ít nhất 3 trong 5 kỹ thuật sau:

| # | Kỹ thuật | Ví dụ |
|---|---|---|
| 1 | **Đổi cấu trúc câu** | Bị động → chủ động, đảo vế trước/sau |
| 2 | **Thay từ đồng nghĩa** | "quan trọng" → "then chốt", "ảnh hưởng" → "chi phối" |
| 3 | **Thêm góc nhìn riêng** | "Nhiều người lầm tưởng rằng...", "Theo kinh nghiệm thực tế..." |
| 4 | **Thêm ví dụ/ngữ cảnh riêng** | Ví dụ cụ thể không trùng với đối thủ |
| 5 | **Thay đổi thứ tự trình bày** | Đưa kết luận lên đầu, giải thích sau |

### 8c. Nguyên tắc rephrase HCVN
- Giữ nguyên **giọng văn persona**: thân thiện, xưng "bạn", câu ≤ 25 chữ, đoạn ≤ 4 dòng
- Giữ nguyên **mật độ KW**: KW chính đạt 1% đến 1.5%, KW phụ ≥ 2 lần mỗi từ
- KHÔNG rephrase **thuật ngữ chuyên ngành** (lãi suất cơ bản, lãi suất thả nổi, tín chấp...)
- KHÔNG rephrase **tên riêng** (NHNN, BIDV, Home Credit, Techcombank...)
- Sau rephrase, verify lại KW count để đảm bảo không bị mất keyword

### 8d. Self-Check Uniqueness
Sau khi rephrase xong, thực hiện kiểm tra:
- So sánh bản rephrase với bản gốc → ước tính % câu đã thay đổi
- Mục tiêu: **≥ 80% câu văn** phải có cấu trúc khác bản gốc
- Các đoạn **định nghĩa chuyên ngành** (dễ trùng nhất) → phải thêm ví dụ riêng hoặc góc nhìn mới
- Nếu chưa đạt → rephrase thêm các đoạn còn giống bản gốc

### 8e. Hướng dẫn user kiểm tra thủ công (nếu cần)
Ghi chú vào delivery: User có thể verify bằng tool bên ngoài:
- **Duplichecker** (duplichecker.com): Free, 1000 từ/lần
- **Quetext** (quetext.com): Free 500 từ, hiển thị % trùng
- **SmallSEOTools** (smallseotools.com): Free 1000 từ/lần
- **Copyscape** (copyscape.com): Paid, chuẩn nhất

- **Output**: Rephrased `article.md` (≥ 90% unique content)

## 10. Phase 9: HCVN Quality Audit (Cross-Validation)
**Goal**: Kiểm tra toàn diện bài viết, cross-validate với Intent Report + Entity Map + Fact-Check. Tự động sửa lỗi.

- **Skill**: `.agent/skills/auditing-content/SKILL.md`
- **Inputs**: `article.md` + `outline.md` + `research.md` + `search-intent.md` + `fact-check-report.md` + persona files

### HCVN Audit Checklist

#### A. Title & Meta
- [ ] Title chứa KW chính, ≤ 60 ký tự
- [ ] Meta Description 130 đến 160 ký tự, chứa KW chính

#### B. Heading Structure
- [ ] H2 đánh số (1., 2., 3...)
- [ ] H3 phân cấp (3.1, 3.2...)
- [ ] ≥ 3 H2 (không đếm FAQs)
- [ ] 1 đến 2 H2 chứa KW chính
- [ ] H2 KHÔNG dạng câu hỏi (trừ FAQs)

#### C. Content Quality
- [ ] Intro 100 đến 200 chữ, KW chính trong 100 từ đầu
- [ ] Mỗi H3 có đủ chiều sâu phân tích (đủ nội dung để đứng độc lập)
- [ ] Sau bảng/dữ liệu có đoạn nhận xét/phân tích
- [ ] Giọng văn xưng "bạn", chuyên môn nhưng dễ hiểu
- [ ] Bullet: **đậm** + `:` + giải thích
- [ ] KHÔNG emdash (—) hoặc dash (–, -)
- [ ] KHÔNG flair words
- [ ] KHÔNG emoji

#### D. Keywords & Links
- [ ] Mật độ KW: 1% đến 1.5%
- [ ] KW chính đạt mật độ 1% đến 1.5%
- [ ] KW phụ xuất hiện ít nhất 2 lần mỗi từ
- [ ] Internal links chỉ `homecredit.vn`
- [ ] Mật độ link 0.8% đến 1.2%, phân bổ tự nhiên
- [ ] KHÔNG external links

#### E. Service Promote
- [ ] Nếu keyword match dịch vụ HC → có H2 promote trước Kết bài
- [ ] Link đúng từ bảng mapping `dich-vu-hcvn.md`
- [ ] Heading tự nhiên, không gượng ép

#### F. Closing
- [ ] Kết bài chứa KW chính + CTA
- [ ] FAQs 3 đến 5 câu, dựa trên KW chính/phụ
- [ ] Disclaimer đầy đủ, trước chữ ký
- [ ] Signature đúng mẫu, in nghiêng, sau `---`

#### G. Intent Alignment (cross-validate với `search-intent.md`)
- [ ] Content format khớp với Recommended Format từ Intent Report
- [ ] Tone bài viết khớp với Content Tone đã xác định
- [ ] Nếu Commercial Intent → có heading so sánh/giá
- [ ] Nếu Transactional Intent → CTA rõ ràng, H2 promote HC nổi bật
- [ ] User Motivation từ Intent Report được trả lời đầy đủ trong bài

#### H. Entity Coverage (cross-validate với `research.md`)
- [ ] Tất cả **Primary Entities** từ Entity Map xuất hiện trong bài
- [ ] **Related Entities** được nhắc đến tự nhiên trong context phù hợp
- [ ] Entities được dùng **contextually** (giải thích, so sánh), không phải keyword stuffing
- [ ] Tất cả **Query Clusters** từ research.md đều có heading/content tương ứng

#### I. Fact-Check Cross-Reference (validate với `fact-check-report.md`)
- [ ] Tất cả claims trong "Corrections Made" đã được sửa đúng trong `article.md`
- [ ] Không còn claim nào trong "Removed Claims" xuất hiện trong `article.md`
- [ ] Không có claim mới chưa verify (nếu article bị sửa sau fact-check)

- **Action**: Nếu phát hiện lỗi ở bất kỳ mục nào → **Auto-fix** trực tiếp trong `article.md`
- **Output**: `Keywords/Home Credit/[keyword-slug]/audit-report.md` + Final `article.md`

## 11. Phase 10: Post-Production Self-Verification (Automated Gate)
**Goal**: Kiểm tra tự động lần cuối bằng script/command. Đảm bảo article sẵn sàng publish mà KHÔNG cần user review thủ công.

Chạy các lệnh kiểm tra tự động trên `article.md`:

### 11a. Keyword Count Verification
- Đếm số lần xuất hiện KW chính → phải ≥ 5 lần
- Đếm từng KW phụ → mỗi KW phải ≥ 2 lần
- Nếu thiếu → inject tự nhiên vào đoạn văn phù hợp

### 11b. Formatting Scan
- Scan toàn bài tìm emdash (—) và endash (–) → phải = 0
- Scan tìm emoji characters → phải = 0
- Scan tìm external links (không phải homecredit.vn hoặc homepaylater.vn) → phải = 0
- Nếu phát hiện → **auto-fix** ngay


### 11d. Structure Validation
- Verify Title ≤ 60 ký tự (đếm chính xác)
- Verify Meta Description 130 đến 160 ký tự
- Verify Intro trong 70 đến 150 chữ
- Verify có Disclaimer + Signature đầy đủ

### 11e. Final Verdict
Sau khi chạy xong tất cả checks:
- Nếu **tất cả PASS** → article sẵn sàng publish
- Nếu có **FAIL** → auto-fix rồi chạy lại verification
- Lặp tối đa **2 lần** trước khi thông báo user

## 12. Lưu và Thông báo
// turbo
- Thông báo user hoàn thành, kèm link đến tất cả artifacts:
    - `search-intent.md` (Intent Report đầy đủ: 7-type + Micro-Intent + SERP)
    - `research.md` (Entity Map + Query Clusters + Content Hierarchy)
    - `competitors/` (folder heading structure đối thủ)
    - `outline/outline.md`
    - `article.md` (Final, đã qua Fact-Check + Rephrase + Audit + Self-Verification)
    - `fact-check-report.md` (Bao gồm Verified/Corrected/Removed)
    - `audit-report.md` (Cross-validation: Intent + Entity + Fact-Check + HCVN)

**Cam kết chất lượng**: Bài viết qua pipeline này đã được:
1. ✅ Phân tích intent sâu (7-type + Micro-Intent)
2. ✅ Trích xuất entity đầy đủ (5 loại entity)
3. ✅ Fact-check từng claim (verify + auto-correct)
4. ✅ Rephrase đạt ≥ 90% unique (chống trùng lặp SERP)
5. ✅ Audit cross-validate (Intent + Entity + Fact-Check + HCVN Persona)
6. ✅ Post-production self-verification (automated scan)
→ **Không cần user review thủ công trước khi publish**
