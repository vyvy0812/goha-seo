# Audit Report: Các di tích lịch sử ở TP.HCM

**Ngày audit:** 26/03/2026
**Điểm tổng:** 5/10

---

## Tóm tắt lỗi nghiêm trọng

| # | Mức độ | Vấn đề | Chi tiết |
|---|--------|--------|----------|
| 1 | CRITICAL | Thiếu SEO Metadata Table | Bài viết không có bảng metadata bắt buộc (Keyword chính, Keyword phụ, Slug, Meta title, Meta description, Outline) |
| 2 | CRITICAL | Thiếu [key_takeaways] shortcode | Theo Global Rule #4, bài viết PHẢI có block `[key_takeaways]...[/key_takeaways]` sau intro, trước ảnh đầu tiên |
| 3 | CRITICAL | Vi phạm Brand CTA | Lời kết nhắc trực tiếp "Vietnam Airlines", "chuyến bay", "khoang thương gia" - vi phạm quy tắc "No Aviation CTA" |
| 4 | CRITICAL | Giá vé Dinh Độc Lập sai | Bài ghi "65.000 VNĐ". Thực tế 2026: 40.000 VNĐ (chỉ Dinh) hoặc 80.000 VNĐ (toàn bộ) |
| 5 | MAJOR | Giá vé Bến Nhà Rồng sai | Bài ghi "Khách quốc tế: 40.000 VNĐ". Thực tế: 25.000 VNĐ |
| 6 | MAJOR | Chùa Giác Lâm thiếu số nhà | Bài ghi "Đường Lạc Long Quân". Chính xác: Số 565 Lạc Long Quân |
| 7 | MAJOR | Thiếu giờ mở cửa nhiều địa điểm | Bến Nhà Rồng, Bảo tàng Lịch sử, Bảo tàng Mỹ thuật, Nhà thờ Đức Bà, Chùa Giác Lâm, Chợ Bến Thành đều thiếu giờ mở cửa |
| 8 | MAJOR | Keyword density thấp | Keyword chính "các di tích lịch sử ở tphcm" xuất hiện khoảng 4-5 lần (yêu cầu: 10-15 lần) |
| 9 | MAJOR | Em dash (–) có thể còn sót | Cần rà soát toàn bộ, thay bằng dấu gạch ngắn (-) theo Global Rule #3 |
| 10 | MINOR | Meta title và H1 không khớp Outline | Outline đề xuất H1 khác, bài dùng "Khám phá 10+ di tích lịch sử ở Thành phố Hồ Chí Minh" |

---

## 1. Structural Audit (Outline vs Article)

| Outline Section | Article Match | Status | Notes |
|-----------------|---------------|--------|-------|
| H1: Các di tích lịch sử ở TP.HCM: Lớp lang ký ức giữa lòng đô thị | H1: Hành trình 2026: Khám phá 10+ di tích lịch sử ở Thành phố Hồ Chí Minh | ⚠️ | H1 khác outline, nhưng vẫn chứa keyword. Nội dung user cung cấp dùng "Khám phá 10+ di tích lịch sử ở Thành phố Hồ Chí Minh" |
| H2: 1. Khúc tráng ca của tự do và độc lập | H2: 1. Khúc tráng ca của tự do và độc lập | ✅ | Khớp hoàn toàn |
| -- H3: Dinh Độc Lập | H3: Dinh Độc Lập - Biểu tượng của hòa bình thống nhất | ✅ | Đầy đủ |
| -- H3: Bến Nhà Rồng | H3: Bến Nhà Rồng - Nơi khởi nguồn một hành trình vĩ đại | ✅ | Đầy đủ |
| -- H3: Bảo tàng Lịch sử TPHCM | H3: Bảo tàng Lịch sử Thành phố Hồ Chí Minh - Nơi lưu giữ cội nguồn | ✅ | Đầy đủ |
| H2: 2. Nhìn lại những năm tháng lửa đạn | H2: 2. Nhìn lại những năm tháng lửa đạn và tinh thần bất khuất | ✅ | Khớp |
| -- H3: Địa đạo Củ Chi | H3: Địa đạo Củ Chi - Thành phố ngầm kỳ vĩ | ✅ | Đầy đủ |
| -- H3: Hầm bí mật Biệt động SG | H3: Di tích Hầm bí mật chứa vũ khí Biệt động Sài Gòn | ✅ | Đầy đủ |
| -- H3: Bảo tàng Chứng tích Chiến tranh | H3: Bảo tàng Chứng tích Chiến tranh | ✅ | Đầy đủ |
| -- H3: Khu di tích Ngã Ba Giồng | H3: Khu di tích lịch sử Ngã Ba Giồng - Hào khí Nam Kỳ khởi nghĩa | ✅ | Đầy đủ |
| H2: 3. Dấu ấn kiến trúc và giao thoa văn hóa | H2: 3. Dấu ấn kiến trúc và sự giao thoa văn hóa | ✅ | Khớp |
| -- H3: Nhà thờ Đức Bà và Bưu điện | H3: Nhà thờ Đức Bà và Bưu điện Thành phố | ✅ | Đầy đủ |
| -- H3: UBND, Nhà hát, Bảo tàng Mỹ thuật | H3: Trụ sở UBND, Nhà hát TP & Bảo tàng Mỹ thuật | ✅ | Đầy đủ |
| -- H3: Lăng Ông Bà Chiểu | H3: Lăng Tả quân Lê Văn Duyệt (Lăng Ông Bà Chiểu) | ✅ | Đầy đủ |
| -- H3: Chợ Bến Thành | H3: Chợ Bến Thành - Biểu tượng giao thương hơn một thế kỷ | ✅ | Đầy đủ |
| H2: 4. Kinh nghiệm tham quan 2026 | H2: 4. Kinh nghiệm tham quan các di tích lịch sử tại TP.HCM 2026 | ✅ | Khớp |
| -- H3: Thời điểm lý tưởng | H3: Thời điểm lý tưởng trong ngày | ✅ | Đầy đủ |
| -- H3: Trang phục và quy định | H3: Lưu ý về trang phục và quy định | ✅ | Đầy đủ |
| H2: 5. FAQ | H2: 5. Câu hỏi thường gặp về các di tích lịch sử ở Sài Gòn | ✅ | 3 câu hỏi đúng như outline |
| H2: Lời kết | H2: Lời kết – Cất cánh cùng Heritage khám phá hồn cốt Việt | ✅ | Có nhưng vi phạm No Aviation CTA |

**Kết luận cấu trúc:** 15/17 sections khớp (88%). Thiếu SEO Metadata Table và Key Takeaways ở đầu bài.

---

## 2. Semantic Audit (Research vs Article)

### Primary Entities

| Entity | Có trong bài | Ngữ cảnh tự nhiên |
|--------|-------------|-------------------|
| Dinh Độc Lập (Hội trường Thống Nhất) | ✅ | Tự nhiên |
| Bến Nhà Rồng (Bảo tàng Hồ Chí Minh) | ✅ | Tự nhiên |
| Địa đạo Củ Chi | ✅ | Tự nhiên |
| Bảo tàng Chứng tích Chiến tranh | ✅ | Tự nhiên |
| Nhà thờ Đức Bà & Bưu điện Trung tâm | ✅ | Tự nhiên |
| KTS Ngô Viết Thụ | ✅ | Tự nhiên |

### Secondary Entities

| Entity | Có trong bài | Ngữ cảnh tự nhiên |
|--------|-------------|-------------------|
| Chợ Bến Thành | ✅ | Tự nhiên |
| Lăng Ông Bà Chiểu | ✅ | Tự nhiên |
| Hầm bí mật Biệt động Sài Gòn | ✅ | Tự nhiên |
| Tả quân Lê Văn Duyệt | ✅ | Tự nhiên |

### Concept/Era Entities

| Entity | Có trong bài |
|--------|-------------|
| Hòn ngọc Viễn Đông | ✅ |
| Kiến trúc Đông Dương / Indochine | ✅ |
| Ngày Thống nhất 30/4/1975 | ✅ |

**Missing Entities:** Không có entity bị thiếu từ research.md.
**Intent Alignment:** 7/10 - Thỏa mãn tốt intent Informational/Know/Go, nhưng thiếu thông tin planning chi tiết (nhiều địa điểm thiếu giờ mở cửa).

---

## 3. Brand & Persona Audit (Heritage Vietnam Airlines)

### Tone Check
| Tiêu chí | Đánh giá | Ghi chú |
|----------|----------|---------|
| Sang trọng & Tinh tế | ✅ 9/10 | Từ vựng Heritage đạt chuẩn: *thâm trầm, rêu phong, vương giả, kiêu hãnh, trầm mặc* |
| Giàu cảm xúc & Hình ảnh | ✅ 9/10 | Miêu tả sinh động, gợi hình rất tốt |
| Trân trọng & Tự hào | ✅ 9/10 | Giọng văn tôn kính, tự hào dân tộc |
| Hàn lâm nhưng Gần gũi | ✅ 8/10 | Kiến thức lịch sử/kiến trúc sâu, diễn đạt mượt |

### CTA - Vi phạm CRITICAL

> Bài viết kết thúc: "Cùng **Vietnam Airlines**, hãy để biểu tượng Hoa Sen Vàng kiêu hãnh đưa đón bạn trên những **chuyến bay đẳng cấp** và êm ái. Từ **khoang thương gia** nhìn xuống thành phố..."

**Quy tắc vi phạm:** Workflow Global Rule - "Heritage Vietnam Airline is an independent lifestyle/travel entity. DO NOT mention Vietnam Airlines, flight bookings, or airline services in the CTA or content."

**Khuyến nghị:** Thay toàn bộ đoạn CTA. Chỉ dùng "Heritage" như một tạp chí du lịch/phong cách sống, không nhắc hãng hàng không.

---

## 4. Hard Data Audit (Giá vé, Địa chỉ, Giờ mở cửa)

| Địa điểm | Địa chỉ | Giá vé | Giờ mở cửa | Mục đích |
|----------|---------|--------|------------|----------|
| Dinh Độc Lập | ✅ Đúng | ❌ Sai (ghi 65K, đúng: 40K hoặc 80K) | ⚠️ Thiếu chi tiết (có 2 cổng với giờ khác nhau) | ✅ |
| Bến Nhà Rồng | ✅ Đúng | ❌ Sai (ghi 40K quốc tế, đúng: 25K) | ❌ Thiếu | ✅ |
| Bảo tàng Lịch sử | ✅ Đúng | ✅ Đúng (30K) | ❌ Thiếu | ✅ |
| Địa đạo Củ Chi | ⚠️ Thiếu chi tiết | ✅ Đúng (35K nội địa) | ❌ Thiếu | ✅ |
| Hầm bí mật Biệt động | ✅ Đúng | ❌ Thiếu giá vé | ✅ Có giờ | ✅ |
| Bảo tàng Chứng tích CT | ✅ Đúng | ✅ Đúng (40K) | ❌ Thiếu | ⚠️ |
| Ngã Ba Giồng | ✅ Đúng | ❌ Thiếu giá vé | ❌ Thiếu | ⚠️ Thiếu mục đích cụ thể |
| Nhà thờ Đức Bà & Bưu điện | ✅ Đúng | ❌ Thiếu giá vé | ❌ Thiếu | ✅ |
| UBND, Nhà hát, BT Mỹ thuật | ✅ Đúng | ❌ Thiếu giá vé | ❌ Thiếu | ✅ |
| Lăng Ông Bà Chiểu | ✅ Đúng | ✅ Miễn phí | ❌ Thiếu | ✅ |
| Chùa Giác Lâm | ❌ Thiếu số nhà (565) | ✅ Miễn phí | ❌ Thiếu | ✅ |
| Chợ Bến Thành | ✅ Đúng | ❌ Thiếu giá vé | ❌ Thiếu | ✅ |

**Tổng:** 4/12 địa điểm có giá vé chính xác. 1/12 có giờ mở cửa. Cần bổ sung toàn diện.

---

## 5. Keyword Density Check

### Primary Keyword: "các di tích lịch sử ở tphcm"

Đếm các biến thể trong bài:
- "các di tích lịch sử ở TP.HCM" / "các di tích lịch sử ở tphcm": ~4 lần
- "di tích lịch sử" (không full phrase): ~3 lần thêm
- **Tổng keyword chính (exact + near-match): khoảng 7 lần**
- **Yêu cầu: 10-15 lần** → ❌ THIẾU (cần thêm 3-8 lần)

### Secondary Keywords

| Keyword phụ | Xuất hiện | Status |
|-------------|-----------|--------|
| Di tích lịch sử văn hóa ở TPHCM | ~2 lần | ✅ |
| Các di sản văn hóa ở TPHCM | ~2 lần | ✅ |
| 10 di tích lịch sử ở Thành phố Hồ Chí Minh | ~1 lần (trong H1) | ⚠️ Cần thêm |

### LSI/Semantic Keywords (từ research.md)

| LSI Keyword | Có | Status |
|-------------|----|----|
| giá vé dinh độc lập 2026 | ✅ | Có |
| kiến trúc nhà thờ đức bà | ✅ | Có nhưng không dùng exact phrase |
| lịch sử bến nhà rồng | ✅ | Tự nhiên |
| kinh nghiệm tham quan | ✅ | Có (H2 section 4) |
| giờ mở cửa | ✅ | Có nhưng thiếu nhiều |
| du lịch sài gòn | ❌ | Không xuất hiện |
| trải nghiệm văn hóa sài gòn | ❌ | Không xuất hiện |

---

## 6. Formatting & Global Rules Check

| Rule | Status | Chi tiết |
|------|--------|----------|
| No Emoji | ✅ | Không có emoji |
| No Em Dash (—) | ⚠️ | Bài dùng dấu "–" (en dash) tại nhiều nơi - cần kiểm tra kỹ có em dash không. Nên thống nhất dùng "-" |
| [key_takeaways] shortcode | ❌ | Hoàn toàn thiếu |
| SEO Metadata Table | ❌ | Hoàn toàn thiếu |
| Expert Blockquote | N/A | Không có blockquote chuyên gia |
| Sentence Case Headings | ✅ | Đạt chuẩn |
| Đoạn văn ≤ 4 dòng | ⚠️ | Một số đoạn dài (L17-21, L107-109) cần chia nhỏ |
| Post-merger Address Format | N/A | TPHCM chưa có thông tin sáp nhập mới, format hiện tại OK |

---

## 7. Khuyến nghị hành động cụ thể

### CRITICAL (Phải sửa ngay)

1. **Thêm SEO Metadata Table** ngay đầu bài viết theo format chuẩn workflow (trước H1).

2. **Thêm `[key_takeaways]` block** sau đoạn intro, trước ảnh đầu tiên. Gợi ý 5-7 bullet:
   - TP.HCM lưu giữ 10+ di tích lịch sử cấp quốc gia và thành phố.
   - Dinh Độc Lập và Bến Nhà Rồng là hai biểu tượng mang tầm vóc quốc gia.
   - Địa đạo Củ Chi trải rộng hơn 200 km, cách trung tâm khoảng 70 km.
   - Chùa Giác Lâm (1744) là ngôi tổ đình cổ nhất thành phố.
   - Thời điểm tham quan lý tưởng: buổi sáng từ 7:30 - 10:30.
   - Nên dành tối thiểu 2 ngày cho hành trình trọn vẹn.

3. **Sửa CTA cuối bài:** Xóa toàn bộ đề cập "Vietnam Airlines", "chuyến bay", "khoang thương gia". Thay bằng CTA mời gọi trải nghiệm Heritage như tạp chí du lịch/phong cách sống.

4. **Cập nhật giá vé Dinh Độc Lập:** Sửa "65.000 VNĐ" thành:
   - Vé toàn bộ (Dinh + Nhà Trưng bày): 80.000 VNĐ/người lớn
   - Vé giới hạn (chỉ Dinh): 40.000 VNĐ/người lớn

5. **Cập nhật giá vé Bến Nhà Rồng:** Sửa "Khách quốc tế: 40.000 VNĐ" thành "Khách quốc tế: 25.000 VNĐ".

### MAJOR (Nên sửa)

6. **Tăng Keyword Density:** Thêm "các di tích lịch sử ở TP.HCM" / "di tích lịch sử" một cách tự nhiên vào các đoạn dẫn nhập H2 và kết bài. Target: 10-15 lần tổng cộng.

7. **Bổ sung giờ mở cửa** cho tất cả 12 địa điểm (hiện chỉ 2/12 có giờ mở cửa).

8. **Chùa Giác Lâm:** Sửa "Đường Lạc Long Quân" thành "Số 565 Lạc Long Quân".

9. **Bổ sung giá vé** cho các địa điểm thiếu: Nhà thờ Đức Bà (miễn phí), Chợ Bến Thành (miễn phí), Ngã Ba Giồng (miễn phí), UBND/Nhà hát/BT Mỹ thuật (Bảo tàng Mỹ thuật: 30.000 VNĐ).

10. **Bổ sung LSI keywords:** Thêm tự nhiên "du lịch Sài Gòn", "trải nghiệm văn hóa Sài Gòn" vào bài.

### MINOR (Cải thiện)

11. **Chia nhỏ đoạn văn dài:** Đoạn về Nhà thờ Đức Bà và Bưu điện có tendency dài, cần tách.

12. **Thống nhất label "Địa chỉ" vs "Vị trí":** Một số dùng "Địa chỉ", một số dùng "Vị trí" - nên thống nhất dùng "Địa chỉ" cho tất cả.

13. **Chùa Giác Lâm nằm sai nhóm:** Trong outline, Chùa Giác Lâm không có trong Section 3 (Dấu ấn kiến trúc). Bài viết đã thêm vào Section 3 - nên giữ nhưng cần lưu ý đây là expansion ngoài outline gốc.
