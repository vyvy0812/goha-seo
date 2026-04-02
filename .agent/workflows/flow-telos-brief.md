---
description: Premium Telos Academy Workflow — Full Brief & Outline Extraction (Research → Competitor → Outline)
---

# Telos Academy Brief & Outline Workflow

Workflow chuyên biệt tạo Content Brief (Research) và Outline cho **Telos Academy** - Học viện đào tạo Thiết kế UI/UX & Product Design hàng đầu.
Quy trình được ráp nối từ các skill tân tiến nhất: Nhận diện Intent, Khai thác Entity, Scrape Đối thủ bằng subagent, và Tạo Outline chuẩn Semantic SEO.

**Quy tắc tiêu chuẩn Telos Academy:**
- **Không dùng Em Dash (—)**: Thay bằng short dash (-).
- **Ngôn ngữ chuyên ngành**: Sử dụng chuẩn xác các thuật ngữ Product Design (UI/UX, Wireframe, Prototype, System Design) nhưng giải thích dễ hiểu.
- **Tính thực tiễn (Practicality)**: Outline luôn phải hướng người đọc đến việc THỰC HÀNH, tránh lý thuyết suông. Ưu tiên các định dạng step-by-step, case study.
- **Service Integration**: Luôn tìm cách lồng ghép khéo léo các khóa học của Telos (UI/UX cơ bản, Figma thực chiến, Design System) vào các H2/H3 giải pháp.

**Command:** `/telos-brief [keyword]`

**Tài liệu tham chiếu:**
- `Persona Brand/Telos Academy/persona-telos.md` (Định hình văn phong & Core Value của Telos)
- `Persona Brand/Telos Academy/central-entity-telos.md` (Danh sách khóa học và dịch vụ cốt lõi)

---

## 1. Chuẩn bị (Preparation)
- **Input**: Từ khóa mục tiêu do user cung cấp.
- **Action**: Tạo folder làm việc: `Keywords/Telos Academy/[keyword-slug]`
- **Prerequisite Check**: Tải các file Persona của Telos Academy vào context.

## 2. Phase 1: Search Intent Analysis (Optimized)
**Goal**: Giải mã Micro-Intent của người dùng (Know/Do/Go) dựa trên dữ liệu SERP thực tế.

- **Action**: Sử dụng tool `search_web "[keyword]"` để phân tích kết quả tìm kiếm hiện tại (có Featured Snippet, Video, PAA không?).
- **Skill**: `.agent/skills/analyzing-search-intent/SKILL.md`
- **Output**: Lưu thành file `search-intent.md`.

## 3. Phase 2: Semantic & Entity Research
**Goal**: Xây dựng nền tảng ngữ nghĩa (Semantic Foundation) và trích xuất Entity chuẩn UI/UX.

- **Action**: Dùng `search_web` tìm kiếm các định nghĩa chuyên sâu.
- **Skill**: `.agent/skills/extracting-keywords/SKILL.md`
- **Inputs**: Mục tiêu từ khóa + `search-intent.md`.
- **Output**: Lưu bản đồ ngữ nghĩa thành file `research.md`.

## 4. Phase 3: Competitor Intelligence (Turbo Scrape)
**Goal**: Cào (scrape) cấu trúc heading của Top 3 đối thủ để tìm Content Gap.

// turbo-all
- **Skill**: `.agent/skills/analyzing-competitors/SKILL.md`
- **Action**: Sử dụng `browser_subagent` tự động search Google từ khoá, truy cập 3 bài viết top 1-2-3 (organic không ads) và trích xuất toàn bộ H1, H2, H3.
- **Output**: Lưu báo cáo vào file `competitor-insights.md` (hoặc lưu trong thư mục `competitors/`).

## 5. Phase 4: Strategic Outline Generation
**Goal**: Gom toàn bộ Research Data và Render ra một bản Brief & Outline duy nhất, sạch sẽ, chuẩn chỉ cho Writer.

- **Skill**: `.agent/skills/generating-outlines-telos/SKILL.md`
- **Inputs**:
    - Dữ liệu Intent, Keyword, Entities, Competitor đã thu thập.
    - `Persona Brand/Telos Academy/central-entity-telos.md` (Để map khóa học UI/UX vào giải pháp)
- **Action**: 
    - Sinh ra bản Brief & Outline gộp chung (Research trên đầu, Outline chi tiết ở dưới).
    - Outline chỉ chứa `Heading` và `Guideline` viết (Không dùng "Semantic Expansion", không phân chia Do/Know).
    - KHÔNG dùng từ ngữ hoa mỹ (flair words).
    - CHỈ viết hoa chữ cái đầu tiên của câu trong tất cả các Heading (Sentence case).
- **Output**: Lưu file duy nhất vào `brief.md` (xoá bỏ các file research tạm nếu muốn gom gọn thành 1).

## 6. Lưu và Báo Cáo
- Hoàn tất lưu file: `brief.md` (chứa toàn bộ Insight và Khung bài viết).
- Báo cáo cho User đường dẫn file và hỏi xem User có muốn đi tiếp sang Phase Viết Bài (Content Writing) không.
