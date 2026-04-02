---
name: generating-outlines-telos
description: >
  Generates a consolidated Brief & Outline for Telos Academy. Combines research data with a practical, flair-free, sentence-case outline format.
  Triggers: telos outline, create telos brief, /generate-outline-telos
---

# Generating Telos Academy Outline & Brief

## Purpose
Tạo ra một bản Brief & Outline duy nhất, hoàn chỉnh cho đội ngũ Content Writer của Telos Academy. File này chứa toàn bộ Research Data (Context, Entities) ở đầu trang và một Outline sạch (chỉ gồm Heading + Guideline viết), hoàn toàn không chứa thuật ngữ nhồi nhét khó hiểu (không dùng "Semantic Expansion", "Intent Do/Know" v.v...).

## Process

### Phase 1: Context & Research Aggregation
Thu thập toàn bộ thông tin đã research (Nghiên cứu Intent, Keyword Clusters, Competitor Data) và gom lại vào phần đầu của Outline.

### Phase 2: Generation - The "Telos Standard" Outline Format
Sinh dàn ý với các quy tắc kiểm soát chất lượng gắt gao:

1. **Heading Formatting (Bắt buộc)**:
   - **Sentence Case**: Chỉ ĐƯỢC PHÉP viết hoa chữ cái ĐẦU TIÊN của dòng heading (hoặc danh từ riêng như Figma, UI/UX, Telos). Ví dụ đúng: `Cách dùng figma trên điện thoại để preview ứng dụng`. Ví dụ sai: `Cách Dùng Figma Trên Điện Thoại`.
   - **No Flair Words**: Không dùng từ ngữ hoa mỹ, sáo rỗng, giật tít lố lăng (Ví dụ: siêu xịn, bí mật, thần thánh, đỉnh cao). Đi thẳng vào vấn đề theo phong cách UI/UX chuyên nghiệp.
2. **Structure**: Dàn ý chỉ tập trung hiển thị Heading (H1, H2, H3) và ngay bên dưới là text Guideline hướng dẫn chi tiết người viết (Nên nhắc đến gì, dùng ví dụ nào).
3. **Service Matching**: Ở H2 gần cuối bài, phải có 1 mục quảng bá tự nhiên khoá học/dịch vụ của Telos dựa vào `central-entity-telos.md`.

### Khung Template Bắt Buộc (Mẫu Output)

```markdown
# Content Brief & Outline: [Từ khoá chính]

## I. RESEARCH & SEO DATA

| Tiêu chí | Dữ liệu chi tiết |
| :--- | :--- |
| **Primary Keyword** | [Từ khoá] |
| **Secondary Keywords** | [List từ khoá vệ tinh] |
| **Entities & Jargon** | [Các thuật ngữ chuyên ngành lĩnh vực UI/UX bắt buộc xuất hiện] |
| **User Intent** | [Vài dòng ngắn gọn người dùng thực sự muốn tìm kiếm điều gì khi gõ từ khoá này] |
| **Competitor Insights** | [1-2 điểm đặc biệt mà đối thủ đang làm tốt hoặc Nội dung đối thủ thiếu sót mà ta cần bổ sung] |

## II. WRITING GUIDELINES (Tiêu chuẩn bài viết)
- Không dùng Em-dash (—), chỉ dùng short-dash (-).
- Giọng văn: Là một Mentor UI/UX thực chiến, hướng dẫn Step-by-step, đi thẳng vấn đề, không vòng vo.
- Chỉ viết hoa chữ cái đầu tiên của Tiêu đề (Sentence case). Không dùng từ ngữ sáo rỗng, hoa mỹ.
- Độ dài đoạn văn: Tối đa 4 dòng. Viết ngắn gọn, dễ quét mắt.
- [key_takeaways] block: Bắt buộc chèn block 5-7 gạch đầu dòng tóm tắt bài viết ngay sau đoạn mở bài.

---

## III. CHI TIẾT OUTLINE

# H1: [Tiêu đề H1 - Tiếng Việt chuẩn, Sentence case, chứa từ khoá chính]
**Guideline viết Mở bài**: Dẫn dắt ngắn gọn vào vấn đề của người dùng. Trình bày tại sao kiến thức này quan trọng. Chèn đoạn block shortcode `[key_takeaways]` tại đây.

## [Số]. [H2 - Sentence case, giải quyết cụm ý định đầu tiên]
**Guideline viết**: Hướng dẫn tác giả cần viết nội dung gì. (Ví dụ: Định nghĩa ngắn, so sánh với công cụ khác, đưa ra ví dụ thực tế).

### [Số].[Số]. [H3 - Sentence case]
**Guideline viết**: Chi tiết hơn cần nói điểm 1, điểm 2. Không được bôi chữ.

## [Số]. [H2 - Khóa học Telos tương ứng hoặc Dịch vụ Mentor]
**Guideline viết**: Lồng ghép tự nhiên khoá học X. Nêu bật lộ trình thực chiến, người dạy chuyên môn cao. Dẫn link nội bộ.

## FAQ (Câu hỏi thường gặp)
### [H3 Câu 1]
**Guideline viết**: Viết câu trả lời trực diện trong 40-50 chữ.

## Kết luận
**Guideline viết**: Tóm tắt lại giá trị bài viết. Kêu gọi hành động (CTA) tải template hoặc xem khoá học.
```

## Self-Check
- [ ] Các Heading có phải là Sentence Case (chỉ viết hoa chữ đầu) chưa?
- [ ] Có từ ngữ Flair không? (Nếu có hãy xoá ngay).
- [ ] Đã gộp bảng Research Data lên đầu Outline chưa?
- [ ] Có hoàn toàn gạt bỏ các term "Semantic Expansion", "Do/Know" khỏi phần Outline bài chưa?
