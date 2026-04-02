# Content Brief & Outline: Thiết kế giao diện app bằng Figma iOS

## I. RESEARCH & SEO DATA

| Tiêu chí | Dữ liệu chi tiết |
| :--- | :--- |
| **Primary Keyword** | Thiết kế giao diện app bằng Figma iOS |
| **Secondary Keywords** | thiết kế app ios figma, nguyên tắc thiết kế ui ios, kích thước chuẩn app iphone figma, vẽ app ios đẹp |
| **Entities & Jargon** | Human Interface Guidelines (HIG), Safe Area, Retina Display, San Francisco Font, Glassmorphism, Tab Bar, Apple Design Resources |
| **User Intent** | Designer muốn nắm rõ đặc điểm thiết kế cho hệ điều hành iOS của Apple thay vì thiết kế chung chung. Họ cần xin file UI Kit chính hãng Apple. |
| **Competitor Insights** | Đối thủ hiếm khi giải thích khái niệm Safe area (tai thỏ / màn hình khuyết) cũng như nguyên tắc sử dụng Font San Francisco. Bài này sẽ đào sâu chi tiết kỹ thuật đó. |

## II. WRITING GUIDELINES (Tiêu chuẩn bài viết)
- Không dùng Em-dash (—), chỉ dùng short-dash (-).
- Giọng văn: Là một Mentor UI/UX thực chiến, hướng dẫn Step-by-step, đi thẳng vấn đề, không vòng vo.
- Chỉ viết hoa chữ cái đầu tiên của Tiêu đề (Sentence case). Không dùng từ ngữ sáo rỗng, hoa mỹ.
- Độ dài đoạn văn: Tối đa 4 dòng. Viết ngắn gọn, dễ quét mắt.
- [key_takeaways] block: Bắt buộc chèn block 5-7 gạch đầu dòng tóm tắt bài viết ngay sau đoạn mở bài.

---

## III. CHI TIẾT OUTLINE

# H1: Hướng dẫn thiết kế giao diện app ios bằng figma chuẩn nguyên tắc apple
**Guideline viết Mở bài**: Đề cập đến sức chi trả, thói quen khó tính của người dùng Apple. Nếu Designer không tuân thủ Human Interface Guidelines (HIG), App có thể bị App Store từ chối (reject). Chèn đoạn block shortcode `[key_takeaways]` tại đây.

## 1. Những đặc tính riêng biệt của thiết kế ui cho ios
**Guideline viết**: So sánh nhanh 3 điểm cốt lõi phân biệt iOS với Android.
### 1.1. Kiểu chữ san francisco (typography)
**Guideline viết**: Bắt buộc cài đặt Font San Francisco – Font chữ mặc định mà Apple luôn dùng cho hệ điều hành. Chỉ cách tải SF PRO trên trang web Apple Developer.
### 1.2. Đường cong liên tục và hiệu ứng kính mờ (glassmorphism)
**Guideline viết**: Phân tích việc nút vuông iOS không bo một góc nhọn mà là góc cong liên tục (squircle) rất mượt. Dùng hiệu ứng Background Blur của Figma để làm kính mờ.

## 2. Kích thước frame iphone chuẩn và vùng an toàn (safe area)
**Guideline viết**: Trình bày thông số thực hành cho File thiết kế.
### 2.1. Chọn frame và độ phân giải hiển thị (retina @2x, @3x)
**Guideline viết**: Nên vẽ ở kích thước điểm Base (1x) là 393x852px (Dòng iPhone Pro). Sau đó xuất file ảnh chế độ 2x, 3x cho độ nét Retina. Mở tính năng chọn Frame có sẵn trong Figma mặc định.
### 2.2. Xử lý vùng an toàn với notch và dynamic island
**Guideline viết**: Cảnh báo lỗi tân binh: đặt quá nhiều text dính vào cạnh viền. Buộc phải chừa khoản trống trên cùng (Navigation, giọt nước) và thanh que Home Indicator bên dưới mép màn hình.

## 3. Cách lấy bộ apple design resources ngay trong figma
**Guideline viết**: Hướng dẫn dùng phím `Shift + I` truy cập Community để tải UI Kit chính thống của Apple cung cấp bản sao chuẩn nhất mọi Icon, Tab, Widget mới nhất của iOS 17+.  

## 4. Thực hành làm app ios chuyên nghiệp với khoá học ui/ux tại Telos
**Guideline viết**: Cấu hình không thể tạo nên giải pháp. Đừng chỉ xếp các Button của Apple cạnh nhau và mong nó đẹp. Giới thiệu lộ trình Bootcamp UI/UX Toàn Diện – Nơi Mentor kèm bạn vẽ case study App tài chính, y tế với phong cách tối giản tuyệt mỹ của iOS. Sản phẩm dùng đi xin việc ngay. Dẫn link nội bộ.

## FAQ (Câu hỏi thường gặp)
### File tải font san francisco không cài được trên windows?
**Guideline viết**: Apple hạn chế font SF trên MacOS. Nếu chạy Windows, thiết kế tạm bằng Font Inter (của Google) với tỷ lệ gần giống nhất 98%, sau đó Coder có thể gọi API CSS để map font chuẩn khi lập trình.
### Thiết kế chế độ dark mode ios cần chú ý điều gì?
**Guideline viết**: Cảnh báo: màu nền đen không nên dùng mã thuần #000000 mà nên dùng nền xám cực tối (midnight black) để mảng chữ không bị chói mắt.

## Kết luận
**Guideline viết**: Khẳng định sự nghiêm ngặt là điều làm nên đẳng cấp của UI iOS. Hãy Follow nguyên lý HIG để tăng tỷ lệ được xuất bản App.
