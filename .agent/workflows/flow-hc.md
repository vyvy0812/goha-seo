---
description: Premium Home Credit Vietnam Blog SEO Workflow — Full Pipeline (10 Phases)
---

# Home Credit Vietnam — Full Writing Pipeline

Workflow viết bài hoàn chỉnh cho **Blog Home Credit Vietnam** (homecredit.vn/blog). Kết hợp Semantic SEO + HCVN Persona + Quality Audit + Fact Check.
**Command:** `/flow-hc [keyword chính] [keyword phụ 1] [keyword phụ 2] ...`

## 🚨 GLOBAL HARD RULES (KHÔNG ĐƯỢC SKIP)
1. **CHUỖI 10 PHASE BẮT BUỘC**: Agent BẮT BUỘC phải thực thi tuần tự từ Phase 1 đến Phase 10. Tạo file `task.md` để track tiến độ. KHÔNG ĐƯỢC dùng tool `notify_user` ngắt ngang khi chưa hoàn thành 10 Phase và tạo xong toàn bộ báo cáo.
2. **CONTENT FRESHNESS**: Luôn dùng `search_web` để verify thông tin mới nhất.
3. **PERSONA RULES**: Không Emoji (thay bằng Lưu ý/Quan trọng). Không Emdash/Dash (-/—). 100% tiếng Việt. Sentence Case Headings. Bold (In đậm) CHỈ dành cho Keyword. KHÔNG ghi `(content gap)` vào output.
4. **TÀI LIÊU BẮT BUỘC CẦN ĐỌC TRƯỚC VÀ ÁP DỤNG TRONG XUYÊN SUỐT**:
   - `Persona Brand/Home Credit/persona-home-credit-skill.md`
   - `Persona Brand/Home Credit/writing-style-analysis.md`
   - `Persona Brand/Home Credit/dich-vu-hcvn.md`
   - `Persona Brand/Home Credit/internal-links-database.md`

---

## 🛠 QUY TRÌNH 10 PHASE CHI TIẾT

### PREPARATION
- **Output**: Tạo folder `Keywords/Home Credit/[keyword-slug]/`

### PHASE 1: Search Intent Analysis
- **Action**: `search_web [keyword chính]` → phân tích SERP features live.
- **Output**: `search-intent.md` dựa trên 7-Type Model:
| Intent Type | Dấu hiệu nhận biết | Content Vehicle |
|---|---|---|
| **Informational** | Snippet, PAA | Guide, Definitions, How-to |
| **Commercial** | So sánh, review | Top X, Comparison, Buying Guide |
| **Transactional** | Ads, "mua", "đăng ký" | CTA, Landing page |
*(Lưu ý: Identify Micro-Intent: Know/Do/Go và Content Tone).*

### PHASE 2: Semantic Research & Entity Discovery
- **Action**: Dùng `search_web` với toán tử `"định nghĩa [keyword]"` và `site:.gov.vn OR site:.edu.vn`.
- **Output**: `research.md` (Gồm Entity Map: Person, Organization, Concept, Location, Time. Và Query Clusters: What, How, Why, Comparison, Best/Top).

### PHASE 3: Competitor Intelligence
- **Action**: Đọc top 3 bài organic đối thủ, trích xuất toàn bộ H2/H3.
- **Output**: `competitors/[competitor_name].md`. Lập bảng so sánh Topic để tìm content gap. (Ghi nhớ: Outline HC 5-6 H2, merge ý nhỏ thành H3. Phần nào cần thì phải đi sâu chi tiết, VD: list đủ ưu - nhược điểm).

### PHASE 4: Service Matching
- **Action**: Đọc `dich-vu-hcvn.md`. Map keyword với dịch vụ tương ứng (Vay tiền mặt, Thẻ tín dụng, PayLater, Vay trả góp điện máy/xe máy, Bảo hiểm...).
- **Quy tắc**: Nếu có match → BĂT BUỘC tạo 1 Heading dạng quảng cáo (Lead Generation) đặt trước Kết bài.
  - **Heading hấp dẫn**: Phải mang tính kêu gọi mạnh (VD: `Cần thanh khoản gấp? Trải nghiệm ngay khoản vay trực tuyến...`). Ưu tiên chứa từ khóa thương mại nếu phù hợp.
  - **Nội dung CTA Copywriting**: Viết nội dung cực kỳ mượt mà, thuyết phục khách hàng.
  - **Trình bày lợi ích bằng Bullet points**: Bắt buộc tạo danh sách gạch đầu dòng (3-4 bullets) liệt kê các quyền lợi nổi bật. Mỗi bullet in đậm vế đầu (VD: `- **Duyệt vay siêu tốc:** Chờ 3 phút...`).
  - **Action Link (Call-to-action)**: Bắt buộc chèn một câu kêu gọi hành động ở cuối đoạn, trong đó **ẩn trực tiếp internal link vào keyword dịch vụ** (VD: `...bằng cách đăng ký [vay tiền mặt](link) tại Home Credit ngay hôm nay!`).

### PHASE 5: Tạo Outline
- **Output**: `outline/outline.md`. Template BẮT BUỘC:
```markdown
<style>
@import url('https://fonts.googleapis.com/css2?family=Libre+Franklin:ital,wght@0,400;0,700;1,400&display=swap');
* { font-family: 'Libre Franklin', sans-serif !important; font-size: 12pt !important; }
h1, h2, h3 { font-size: 12pt !important; }
</style>

# Outline: [Title ≤ 60 chars]

| Field | Value |
|---|---|
| Title | [Title] |
| Meta | [130-160 chars] |
| KW chính/phụ | [Liệt kê] |
| Mật độ | KW (1-1.5%), Link nội (0.8-1.2%) |

---
## Intro (70-150 chữ)
## 1. [KW chính] là gì?
## ... (H2 đánh số 2., 3. không lạm dụng)
## [Số]. [Heading quảng cáo dịch vụ HC - nếu có]
## Kết bài
## FAQ (3-5 câu H3, ví dụ: ### 6.1. Câu hỏi?)
## Disclaimer
---
*Lưu ý: Thông tin trong bài mang tính chất tham khảo, được tổng hợp từ thị trường và không đại diện cho toàn bộ sản phẩm, dịch vụ của Home Credit.*
## Đang so với các đối thủ (List 3 URLs)
---
[Chữ ký chuẩn theo Persona Mục 11+12, in nghiêng 100%]
```

### PHASE 6: Viết bài (Content Writing)
- **Output**: `article.md`.
- **Luật Viết (Critical)**:
  - Header đầu bài phải có **SEO Metadata Table**.
  - **Độ dài bài viết**: BẮT BUỘC tối thiểu 2500 từ. Cần khai thác nội dung chuyên sâu, phân tích chi tiết để đạt dung lượng, tuyệt đối không viết lan man hoặc nhồi nhét từ vô nghĩa.
  - **Giọng văn**: Xưng "bạn", không dùng từ lóng hay thuật ngữ hàn lâm quá mức. Intro 100-200 chữ có KW chính.
  - **Format**: Đoạn ≤ 4 câu. Câu ≤ 25 chữ.
  - **Bảng**: Khi ghi "Bảng" hoặc liệt kê "Ưu - Nhược điểm", bắt buộc trình bày bằng dạng Markdown Table. **Lưu ý bảng ưu/nhược điểm: mỗi ý phải được xuống dòng (dùng `<br>- `) để dễ đọc, không viết gộp thành đoạn văn dài.** **Sau mỗi bảng phải có nhận xét.** KHÔNG tự động chèn/add hình ảnh vào nội dung bài viết.
  - **Internal Link**: CHỈ domain `homecredit.vn`. Lập danh sách link từ `internal-links-database.md`. KHÔNG dùng block liên kết kiểu `>>> Xem thêm: [Title]`. Chỉ đi anchor text khi có từ ngữ chính xác về bài viết (VD: "quản lý chi tiêu" -> dẫn về bài quản lý chi tiêu). Ưu tiên UX, gắn link đúng bối cảnh. Lưu ý anchor text: nên là main keyword của bài đích (Ví dụ: trỏ về bài định nghĩa thì anchor text phải là "tiết kiệm là gì" thay vì chỉ hyper chữ "tiết kiệm" để người đọc rõ context).
  - **Mật độ KW**: Chính (1-1.5%). Phụ (xuất hiện ≥ 2 lần).
  - Kết bài phải có CTA trỏ về: `blog [Cẩm nang tài chính số](https://www.homecredit.vn/blog)`.

### PHASE 7: Deep Research Fact-Checking
- **Action**: Trích xuất tất cả "claims" từ bài viết (Lãi suất, Giá, Thông số, Khoản luật, Định nghĩa).
- Dùng `search_web` (tối thiểu 3 thao tác) đối chiếu chéo.
- **Auto-Fix**: Sửa trực tiếp thông tin sai trong `article.md`.
- **Output**: `fact-check-report.md`. Chia 3 mục: Verified, Corrections Made, Removed Claims.

### PHASE 8: Rephrase & Uniqueness Check (Chống Trùng Lặp)
- **Goal**: Viết lại toàn bộ câu văn (Rephrase) để bài viết đạt **≥ 90% độ unique**, đảm bảo không trùng lặp (plagiarism) với các bài trên SERP.
- **Action**: Không tự ý sửa SEO metadata, thẻ bảng, link. CHỈ viết lại phần văn bản editorial.
- **5 Kỹ thuật bắt buộc**: (1) Đảo cấu trúc câu (Bị động ↔ Chủ động), (2) Thay từ đồng nghĩa phong phú hơn, (3) Thêm góc nhìn riêng ("Nhiều người lầm tưởng..."), (4) Thêm ví dụ ngữ cảnh mới, (5) Thay đổi trình tự giải thích ý. Cứ làm cho đến khi đạt trên 90% độ nguyên bản.

### PHASE 9: HCVN Quality Audit
- **Action**: Compare `article.md` với `outline.md` & `search-intent.md`.
- **Checklist Audit**:
  - H2 không dạng câu hỏi.
  - Không emoji, Không emdash. KW chính đủ mật độ ~1.2%. Link đủ ~1%.
  - Entity đầy đủ, Intent KHỚP 100%.
- **Output**: `audit-report.md` (Chấm điểm 1-10 + Nhận xét Lỗi/Đã auto-fix).

### PHASE 10: Auto-Validation & Deliver
- Confirm final count của keywords & links. Nếu Pass tất cả, gọi `notify_user` bàn giao đầy đủ 7 tài nguyên.
