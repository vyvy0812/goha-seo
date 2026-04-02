---
description: SEO Quotation & Data Analysis — Phân tích hiện trạng SEO website + Xuất báo giá kèm Roadmap 12 tháng
---

# SEO Quotation & Data Analysis Workflow

Workflow phân tích toàn diện hiện trạng SEO của một website và xuất **báo giá chuyên nghiệp** kèm **roadmap triển khai 12 tháng**.

**Command:** `/seo-quotation [URL website]`

**Tài liệu tham chiếu:**
- `.agent/skills/analyzing-competitors/SKILL.md` — Competitor Benchmark (Phase 4)
- `.agent/skills/analyzing-search-intent/SKILL.md` — Keyword Intent (Phase 3)
- `.agent/skills/extracting-keywords/SKILL.md` — Entity & Keyword Extraction (Phase 3)
- `.agent/skills/analyzing-semantic-seo/SKILL.md` — Content Gap Analysis (Phase 5)
- `tools/rank-checker/` — Ranking data (nếu có)
- `Persona Brand/` — Brand voice (nếu báo giá cho brand nội bộ)

**GOHA Brand Assets:**
- **Logo (SVG):** `https://static.goha.vn/wp-content/uploads/2025/06/Full.svg`
- **Background (PNG):** `https://static.goha.vn/wp-content/uploads/2025/07/Background-1.png`

**GOHA Google Ads Pricing:**
- **Phí Setup:** 5,000,000 ₫ (1 lần) — audit, keyword research, campaign structure, conversion tracking, ad copy
- **Phí quản lý:** 20% ngân sách quảng cáo thực chi/tháng
- **Phí tối thiểu:** 4,000,000 ₫/tháng (áp dụng khi ngân sách Ads < 20 triệu/tháng)

---

## Phase 1: Thu thập thông tin khách hàng

**Goal**: Xác nhận đầy đủ thông tin trước khi phân tích.

- **Action**: Hỏi user cung cấp:
    1. **URL website** cần phân tích
    2. **Ngành hàng / Lĩnh vực** (F&B, Công nghiệp, SaaS, Dịch vụ, E-commerce...)
    3. **Mục tiêu kinh doanh** (tăng traffic, tăng leads, tăng doanh thu, brand awareness)
    4. **Đối thủ chính** (nếu biết, liệt kê 2-3 URL)
    5. **Ngân sách dự kiến** (nếu chia sẻ)
    6. **Đã từng làm SEO chưa?** (có/không, bao lâu)
- **Action**: Tạo folder: `Keywords/SEO-Quotation/[domain-slug]/`
- **Output**: Ghi nhận thông tin vào `client-brief.md`

---

## Phase 2: Technical SEO Audit

**Goal**: Đánh giá sức khỏe kỹ thuật của website.

- **Action**: Sử dụng `search_web` và `browser_subagent` để kiểm tra:

### 2.1 Core Web Vitals & Tốc độ
- Truy cập PageSpeed Insights: `https://pagespeed.web.dev/analysis?url=[URL]`
- Ghi nhận điểm **LCP**, **FID/INP**, **CLS** cho cả Mobile & Desktop
- Đánh giá: Tốt (xanh) / Cần cải thiện (vàng) / Kém (đỏ)

### 2.2 Mobile-Friendliness
- Kiểm tra responsive design qua browser
- Đánh giá: font size, tap targets, viewport config

### 2.3 Indexing & Crawlability
- `search_web "site:[domain]"` — đếm số trang đã index
- Kiểm tra `robots.txt` (`[URL]/robots.txt`)
- Kiểm tra `sitemap.xml` (`[URL]/sitemap.xml`)
- Phát hiện: noindex, canonical issues, redirect chains

### 2.4 Schema & Structured Data
- Sử dụng `search_web "site:[domain] schema markup"` hoặc truy cập Rich Results Test
- Kiểm tra: Organization, Breadcrumb, Product, FAQ, Article schema

### 2.5 Security & HTTPS
- Kiểm tra SSL certificate
- Mixed content warnings
- HTTP → HTTPS redirect

- **Output**: `technical-audit.md` với bảng điểm:

```markdown
| Hạng mục | Điểm (/10) | Trạng thái | Ghi chú |
|----------|-----------|------------|---------|
| Core Web Vitals | | 🟢/🟡/🔴 | |
| Mobile-Friendly | | 🟢/🟡/🔴 | |
| Indexing | | 🟢/🟡/🔴 | |
| Schema | | 🟢/🟡/🔴 | |
| HTTPS/Security | | 🟢/🟡/🔴 | |
| **Tổng Technical** | **/50** | | |
```

---

## Phase 3: Keyword Landscape Analysis

**Goal**: Xây dựng bản đồ từ khóa hiện tại và phát hiện cơ hội mới.

- **Skill**: `.agent/skills/analyzing-search-intent/SKILL.md`
- **Skill**: `.agent/skills/extracting-keywords/SKILL.md`

### 3.1 Keyword hiện tại
- `search_web "site:[domain]"` — lấy danh sách trang đã index
- Phân tích Title & Meta của các trang chính
- Xác định keyword nào đang được target

### 3.2 Keyword Opportunity
- Sử dụng `search_web` với các biến thể:
    - `"[ngành hàng] + [dịch vụ/sản phẩm]"` — tìm keyword thương mại
    - `"[keyword chính] là gì"`, `"cách [keyword]"` — tìm keyword thông tin
    - `"[keyword] giá"`, `"mua [keyword]"` — tìm keyword giao dịch
- Phân nhóm theo Search Intent: Informational / Commercial / Transactional / Navigational

### 3.3 Keyword Prioritization Matrix
- Đánh giá theo: Search Volume (ước lượng) × Relevance × Difficulty × Business Value
- Phân loại: Quick Win / Strategic / Long-term / Low Priority

- **Output**: `keyword-analysis.md` với:
    - Danh sách keyword hiện tại (và đánh giá)
    - 30-50 keyword cơ hội mới (phân nhóm theo intent)
    - Priority Matrix table

---

## Phase 4: Competitor Benchmark

**Goal**: So sánh trực tiếp với top 3 đối thủ cùng ngành.

// turbo
- **Skill**: `.agent/skills/analyzing-competitors/SKILL.md`
- **Action**: Xác định top 3 đối thủ:
    - Nếu user đã cung cấp → dùng luôn
    - Nếu chưa → `search_web "[keyword chính ngành]"` → lấy top 3 organic
- **Action**: Với mỗi đối thủ, phân tích bằng `browser_subagent` & `search_web`:

### 4.1 Visibility & Rankings
- `search_web "site:[competitor]"` — số trang index
- So sánh top keyword rankings (nếu có dữ liệu)

### 4.2 Content Volume & Quality
- Đếm số bài blog / trang sản phẩm
- Đánh giá chất lượng nội dung (depth, freshness, media)

### 4.3 Backlink Profile (ước lượng)
- `search_web "link:[competitor]"` hoặc kiểm tra qua các nguồn public
- So sánh domain authority (ước lượng)

### 4.4 Technical Comparison
- PageSpeed Insights cho từng đối thủ
- Schema implementation

- **Output**: `competitor-benchmark.md` với bảng so sánh:

```markdown
| Tiêu chí | Website KH | Đối thủ 1 | Đối thủ 2 | Đối thủ 3 |
|----------|-----------|-----------|-----------|-----------|
| Số trang index | | | | |
| Tốc độ Mobile | | | | |
| Tốc độ Desktop | | | | |
| Schema | | | | |
| Số bài content | | | | |
| Backlink (ước lượng) | | | | |
| **Tổng điểm** | | | | |
```

---

## Phase 5: Content Audit & Gap Analysis

**Goal**: Đánh giá nội dung hiện có và xác định khoảng trống cần lấp.

- **Skill**: `.agent/skills/analyzing-semantic-seo/SKILL.md`

### 5.1 Content Inventory
- Liệt kê tất cả trang nội dung chính (từ sitemap hoặc crawl)
- Phân loại: Pillar / Supporting / Product / Service / Blog / Landing Page
- Đánh giá từng trang: word count (ước lượng), freshness, keyword alignment

### 5.2 Content Quality Score
- Đánh giá mỗi trang theo:
    - **Relevance**: Nội dung có match keyword target?
    - **Depth**: Đủ chi tiết hay thin content?
    - **Freshness**: Cập nhật gần nhất?
    - **Entity Coverage**: Có cover đủ entity quan trọng?

### 5.3 Content Gap
- So sánh topic clusters của website vs. đối thủ
- Xác định: topic nào đối thủ có mà website chưa có?
- Đề xuất: bài viết mới cần tạo (kèm keyword target)

- **Output**: `content-gap.md` với:
    - Content Inventory table
    - Gap Analysis (danh sách topic thiếu)
    - Đề xuất Content Roadmap ưu tiên

---

## Phase 6: Backlink Profile Analysis

**Goal**: Đánh giá hồ sơ backlink hiện tại.

### 6.1 Backlink Overview
- Sử dụng `search_web "[domain] backlinks"`, `"link:[domain]"` để thu thập dữ liệu công khai
- Ước lượng: tổng số backlinks, referring domains, dofollow/nofollow ratio

### 6.2 Backlink Quality Assessment
- Phân loại nguồn: Editorial / Guest Post / Directory / Forum / Social / Spam
- Đánh giá: có toxic links không? Có cần disavow?

### 6.3 Competitor Backlink Gap
- So sánh profile backlink với top 3 đối thủ
- Xác định: đối thủ có backlink từ nguồn nào mà website chưa có?

- **Output**: `backlink-analysis.md`

---

## Phase 7: UX & Conversion Signals

**Goal**: Đánh giá trải nghiệm người dùng và khả năng chuyển đổi.

- **Action**: Truy cập website bằng `browser_subagent`, đánh giá:

### 7.1 Navigation & Structure
- Menu có rõ ràng, dễ dùng?
- Breadcrumb có hoạt động?
- Search functionality?

### 7.2 CTA & Conversion Points
- Có CTA rõ ràng trên mỗi trang?
- Form liên hệ / đặt hàng hoạt động?
- Số điện thoại, Zalo, chat có visible?

### 7.3 Visual & Trust Signals
- Design chuyên nghiệp hay cũ kỹ?
- Có testimonials, chứng nhận, case study?
- Ảnh chất lượng hay stock photo chung?

### 7.4 Mobile Experience
- Trải nghiệm mobile thực tế (layout, font, tap targets)
- Popup có cản trở không?

- **Output**: `ux-signals.md` với nhận xét + điểm UX (/20)

---

## Phase 8: SEO Scorecard

**Goal**: Chấm điểm tổng thể SEO (0-100) dựa trên tất cả dữ liệu thu thập.

- **Action**: Tổng hợp từ Phase 2-7, tính điểm theo bảng trọng số:

```markdown
| Hạng mục | Trọng số | Điểm | Điểm (có trọng số) |
|----------|---------|------|-------------------|
| Technical SEO | 25% | /50 | |
| Keyword & Rankings | 20% | /20 | |
| Content Quality | 20% | /20 | |
| Backlink Profile | 15% | /15 | |
| Competitor Position | 10% | /10 | |
| UX & Conversion | 10% | /20 | |
| **TỔNG ĐIỂM SEO** | **100%** | | **/100** |
```

- **Xếp hạng**:
    - **80-100**: Xuất sắc — Tối ưu chi tiết & mở rộng
    - **60-79**: Khá — Cần cải thiện một số mảng
    - **40-59**: Trung bình — Cần đầu tư nghiêm túc
    - **20-39**: Yếu — Cần xây dựng lại nền tảng
    - **0-19**: Rất yếu — Gần như bắt đầu từ đầu

- **Output**: `seo-scorecard.md`

---

## Phase 9: Báo giá & Roadmap 12 tháng

**Goal**: Xuất báo cáo báo giá hoàn chỉnh, chuyên nghiệp, sẵn sàng gửi khách hàng.

- **Action**: Tổng hợp tất cả output từ Phase 1-8 vào một báo cáo duy nhất.

### 9.1 Executive Summary
- Tóm tắt 3-5 điểm mạnh chính
- Tóm tắt 3-5 điểm yếu / vấn đề cấp bách
- SEO Score tổng thể + xếp hạng
- Kết luận ngắn: cơ hội lớn nhất là gì?

### 9.2 Roadmap 12 tháng

#### Quý 1 (Tháng 1-3): Foundation — Xây nền tảng
| Tháng | Hạng mục | Chi tiết |
|-------|----------|---------|
| 1 | Technical SEO Fix | Sửa lỗi crawl, tối ưu sitemap/robots.txt, fix broken links, cải thiện Core Web Vitals |
| 1 | On-Page Cơ bản | Tối ưu Title, Meta Description, Heading cho top 20 trang quan trọng nhất |
| 2 | Keyword Strategy | Chọn 30-50 keyword mục tiêu, phân nhóm theo intent |
| 2 | Content Audit | Đánh giá nội dung hiện có: giữ / cải thiện / xóa / merge |
| 3 | Schema & Structured Data | Triển khai Organization, Product, FAQ, Breadcrumb schema |
| 3 | Internal Linking v1 | Xây dựng cấu trúc silo + internal link cho content hiện tại |

#### Quý 2 (Tháng 4-6): Growth — Sản xuất nội dung
| Tháng | Hạng mục | Chi tiết |
|-------|----------|---------|
| 4 | Content Production (Pillar) | Viết 4-6 bài Pillar Content (2500+ từ) cho topic clusters chính |
| 4 | Backlink Outreach v1 | Bắt đầu chiến dịch guest posting + digital PR (10-15 backlinks/tháng) |
| 5 | Content Production (Support) | Viết 8-10 bài Supporting Content liên kết về Pillar |
| 5 | Local SEO (nếu có) | Tối ưu Google Business Profile, citations, local keywords |
| 6 | Content Refresh | Cập nhật & tối ưu lại bài cũ dựa trên dữ liệu GSC 3 tháng đầu |
| 6 | Backlink Outreach v2 | Tiếp tục link building + broken link building |

#### Quý 3 (Tháng 7-9): Scale — Mở rộng & tối ưu
| Tháng | Hạng mục | Chi tiết |
|-------|----------|---------|
| 7 | Topical Authority Expansion | Mở rộng topic clusters mới dựa trên keyword gaps đã phát hiện |
| 7 | Advanced On-Page | Tối ưu NLP/Entity, Featured Snippet optimization |
| 8 | Content Production (Scale) | Sản xuất 10-15 bài/tháng theo editorial calendar |
| 8 | UX & CRO | Cải thiện page layout, CTA, mobile UX |
| 9 | Link Building (Authority) | Backlink chất lượng cao (DA 50+), digital PR campaigns |
| 9 | Mid-Term Review | Báo cáo 9 tháng: so sánh rankings, traffic, conversions vs. baseline |

#### Quý 4 (Tháng 10-12): Dominate — Chiếm lĩnh & duy trì
| Tháng | Hạng mục | Chi tiết |
|-------|----------|---------|
| 10 | Content Domination | Cập nhật Pillar Content, thêm multimedia (video, infographic) |
| 10 | Advanced Schema | Triển khai HowTo, Video, Review schema |
| 11 | Competitor Counter | Phân tích lại đối thủ, phản công keyword bị vượt mặt |
| 11 | Content Pruning | Xóa/consolidate thin content, redirect 301 trang yếu |
| 12 | Annual Review & Renewal | Báo cáo ROI 12 tháng, đề xuất chiến lược năm 2 |
| 12 | Knowledge Base | Xây dựng tài liệu quy trình SEO nội bộ cho khách hàng |

### 9.3 KPI & Mục tiêu theo quý

```markdown
| KPI | Baseline (hiện tại) | Quý 1 | Quý 2 | Quý 3 | Quý 4 |
|-----|---------------------|-------|-------|-------|-------|
| Organic Traffic/tháng | [số hiện tại] | +20% | +50% | +100% | +150% |
| Keywords Top 10 | [số hiện tại] | +10 KW | +25 KW | +40 KW | +60 KW |
| Keywords Top 3 | [số hiện tại] | +3 KW | +8 KW | +15 KW | +25 KW |
| Domain Authority | [điểm] | +2 | +5 | +8 | +12 |
| Leads/tháng từ SEO | [số hiện tại] | +15% | +40% | +80% | +120% |
| Tỷ lệ Bounce Rate | [%] | -5% | -10% | -15% | -20% |
```

### 9.4 Bảng báo giá

Điều chỉnh giá dựa trên quy mô website (số trang, ngành, cạnh tranh):

```markdown
| Hạng mục | Basic | Pro | Enterprise |
|----------|-------|-----|-----------|
| **Số keyword mục tiêu** | 20-30 | 50-80 | 100+ |
| **Bài viết mới/tháng** | 4 | 8-10 | 15-20 |
| **Backlinks/tháng** | 5-10 | 15-25 | 30-50 |
| **Technical SEO Audit** | 1 lần/quý | Hàng tháng | Hàng tuần |
| **Báo cáo ranking** | Hàng tháng | 2 lần/tháng | Hàng tuần |
| **Content Refresh** | Quý 1 lần | Hàng tháng | Hàng tháng |
| **Schema & Structured Data** | Cơ bản | Nâng cao | Full |
| **Local SEO** | - | Có | Có + Maps Ads |
| **CRO / UX Audit** | - | Quý 1 lần | Hàng tháng |
| **Account Manager riêng** | - | - | Có |
| **Giá/tháng (tham khảo)** | [Tùy ngành] | [Tùy ngành] | [Tùy ngành] |
```

> Ghi chú: Giá cụ thể được điền dựa trên phân tích thực tế từ Phase 1-8. Các yếu tố ảnh hưởng: quy mô website, mức độ cạnh tranh ngành, trạng thái SEO hiện tại (SEO Score), và mục tiêu KPI.

### 9.5 Điều khoản & Cam kết
- Thời gian hợp đồng tối thiểu: **6 tháng** (khuyến nghị 12 tháng)
- Báo cáo tiến độ: định kỳ theo gói
- Cam kết: tăng trưởng organic traffic tối thiểu **X%** sau 6 tháng (tùy baseline)
- Không cam kết ranking vị trí cụ thể (tuân thủ Google Guidelines)

- **Output**: `seo-quotation-report.md` — Báo cáo hoàn chỉnh sẵn sàng gửi khách hàng

---

## Final Delivery
- Thông báo user hoàn tất phân tích.
- Liệt kê tất cả artifacts:
    - `client-brief.md`
    - `technical-audit.md`
    - `keyword-analysis.md`
    - `competitor-benchmark.md`
    - `content-gap.md`
    - `backlink-analysis.md`
    - `ux-signals.md`
    - `seo-scorecard.md`
    - `seo-quotation-report.md` (BÁO CÁO CHÍNH)
