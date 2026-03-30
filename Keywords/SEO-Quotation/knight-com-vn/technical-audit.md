# Technical SEO Audit — knight.com.vn

**Ngày phân tích:** 16/03/2026  
**CMS:** WordPress + Yoast SEO Premium  
**IP Server:** 103.77.162.35

---

## 1. Core Web Vitals & Tốc độ

### Mobile (Performance Score: 40/100 🔴)

| Chỉ số | Giá trị | Trạng thái |
|--------|---------|------------|
| LCP (Largest Contentful Paint) | 10.1s | 🔴 Kém |
| INP (Interaction to Next Paint) | 572ms | 🔴 Kém |
| CLS (Cumulative Layout Shift) | 0.063 | 🟢 Tốt |
| FCP (First Contentful Paint) | 6.3s | 🔴 Kém |
| TTFB (Time to First Byte) | 2.4s | 🔴 Kém |
| Speed Index | 13.1s | 🔴 Kém |

### Desktop (Performance Score: 47/100 🔴)

| Chỉ số | Giá trị | Trạng thái |
|--------|---------|------------|
| LCP (Largest Contentful Paint) | 3.6s | 🔴 Kém |
| INP (Interaction to Next Paint) | 72ms | 🟢 Tốt |
| CLS (Cumulative Layout Shift) | 0.083 | 🟢 Tốt |
| FCP (First Contentful Paint) | 1.0s | 🟡 Cần cải thiện |
| Speed Index | 5.0s | 🔴 Kém |

**Nhận xét:** Website **rất chậm** trên cả hai nền tảng. TTFB cao (2.4s mobile) cho thấy server response time kém — có thể do hosting yếu hoặc thiếu CDN. LCP 10.1s trên mobile là mức rất nghiêm trọng, ảnh hưởng trực tiếp đến thứ hạng Google.

**Điểm Core Web Vitals: 3/10** 🔴

---

## 2. Mobile-Friendliness

| Tiêu chí | Đánh giá |
|----------|----------|
| Responsive Design | ✅ Tốt — Layout responsive đầy đủ |
| Font Size | ✅ Dễ đọc trên mobile |
| Tap Targets | ✅ Các nút bấm đủ kích thước |
| Viewport Meta | ✅ Có cấu hình viewport |
| Floating CTA | ✅ WhatsApp, Zalo, Live Chat luôn hiện |
| Hamburger Menu | ✅ Menu responsive hoạt động tốt |

**Nhận xét:** Thiết kế mobile tốt, giao diện hiện đại, dễ sử dụng. Tuy nhiên, tốc độ tải trên mobile là vấn đề lớn nhất.

**Điểm Mobile-Friendly: 8/10** 🟢

---

## 3. Indexing & Crawlability

| Tiêu chí | Kết quả |
|----------|---------|
| Robots.txt | ✅ Cho phép crawl toàn bộ (`Disallow:` trống) |
| Sitemap Index | ✅ `sitemap_index.xml` với 11 sub-sitemaps |
| Tổng URL trong sitemap | ~267+ URLs (10 pages, 37 posts, 220 news) |
| Canonical Tag | ✅ Self-referencing đúng |
| Hreflang | ✅ `vi`, `en`, `x-default` |
| Noindex | ✅ Không phát hiện noindex sai |
| Robots Meta | ✅ `index, follow, max-image-preview:large` |
| Service pages | 20+ trang dịch vụ |
| News articles | ~169 bài viết blog/tin tức |

**Nhận xét:** Indexing rất tốt. Website có cấu trúc sitemap rõ ràng (Yoast SEO quản lý), robots.txt cho phép crawl toàn bộ. Hreflang được triển khai đúng cho phiên bản song ngữ (VI/EN).

**Điểm Indexing: 9/10** 🟢

---

## 4. Schema & Structured Data

| Schema Type | Triển khai |
|------------|-----------|
| Organization | ✅ Có — logo, social profiles, contact |
| WebPage | ✅ Có — publication/modification dates |
| WebSite + SearchAction | ✅ Có — internal search target |
| BreadcrumbList | ✅ Có — breadcrumb schema |
| Product | ❌ Không có |
| FAQ | ❌ Không có |
| Article | ❌ Không có (cho blog/news) |
| Service | ❌ Không có |
| LocalBusiness | ❌ Không có (cho 4 chi nhánh) |
| HowTo | ❌ Không có |

**Nhận xét:** Schema cơ bản đã có (Yoast auto-generate). Tuy nhiên **thiếu** nhiều schema quan trọng cho ngành logistics: Service, LocalBusiness (4 chi nhánh), FAQ (FAQ page), Article (169 bài blog). Đây là cơ hội lớn để cải thiện rich snippets.

**Điểm Schema: 5/10** 🟡

---

## 5. Security & HTTPS

| Tiêu chí | Kết quả |
|----------|---------|
| HTTPS | ✅ SSL Certificate hoạt động |
| HTTP→HTTPS Redirect | ✅ Tự động redirect |
| Mixed Content | ✅ Không phát hiện |
| SSL Provider | Cloudflare (ước lượng từ IP) |

**Nhận xét:** Security đạt chuẩn, không có vấn đề gì cần khắc phục.

**Điểm Security: 10/10** 🟢

---

## 6. Heading Hierarchy & On-Page

| Vấn đề | Chi tiết |
|--------|---------|
| H1 Tag | ✅ Mỗi trang có 1 H1 duy nhất |
| H2 Hierarchy | ⚠️ Nhiều trang dịch vụ dùng H3 thay vì H2 cho tiêu đề service |
| Title Tag | ✅ Có — nhưng một số trang có brand cắt cụt |
| Meta Description Homepage | ✅ "Knight Logistics - Công ty logistics TPHCM với hơn 20 năm kinh nghiệm" |
| OG Tags | ✅ og:title, og:description, og:image đầy đủ |
| OG Title Homepage | ⚠️ "Trang chủ" — quá ngắn, thiếu keyword |

**Nhận xét:** On-page cơ bản khá tốt nhờ Yoast SEO. Tuy nhiên OG Title trang chủ chỉ là "Trang chủ" — thiếu keyword optimization. Heading hierarchy trên nhiều service page không chuẩn (H3 thay H2).

---

## Bảng tổng hợp Technical SEO

| Hạng mục | Điểm (/10) | Trạng thái | Ghi chú |
|----------|-----------|------------|---------|
| Core Web Vitals | 3 | 🔴 | LCP 10.1s mobile, TTFB 2.4s — rất chậm |
| Mobile-Friendly | 8 | 🟢 | Design responsive tốt, chỉ tốc độ kém |
| Indexing | 9 | 🟢 | 267+ URLs, sitemap/canonical/hreflang đúng |
| Schema | 5 | 🟡 | Thiếu Service, LocalBusiness, Article, FAQ |
| HTTPS/Security | 10 | 🟢 | SSL + redirect hoàn chỉnh |
| **Tổng Technical** | **35/50** | 🟡 | **Điểm yếu chính: Tốc độ + Schema** |
