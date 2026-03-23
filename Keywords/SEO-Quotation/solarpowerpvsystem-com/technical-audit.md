# Technical SEO Audit — solarpowerpvsystem.com/vietnamese/

> Ngày đánh giá: 23/03/2026

---

## 1. Core Web Vitals & Tốc độ

| Chỉ số | Mobile | Desktop | Đánh giá |
|--------|--------|---------|----------|
| **Performance Score** | 64/100 | 73/100 | 🟡 Cần cải thiện |
| **FCP** (First Contentful Paint) | 2.4s | 0.9s | 🟡/🟢 |
| **LCP** (Largest Contentful Paint) | 6.5s | 1.7s | 🔴/🟡 |
| **TBT** (Total Blocking Time) | 0ms | 0ms | 🟢/🟢 |
| **CLS** (Cumulative Layout Shift) | 0.152 | 0.301 | 🟡/🔴 |
| **Speed Index** | 5.3s | 2.1s | 🔴/🟡 |

**Nhận xét:**
- LCP Mobile **6.5s** — vượt ngưỡng tối đa 2.5s của Google rất xa → cần tối ưu hình ảnh, lazy loading, CDN
- CLS Desktop **0.301** — vượt ngưỡng 0.1 → có vấn đề layout shift, có thể do banner slider không set kích thước cố định
- TBT = 0ms → website không có JavaScript blocking → tốt

## 2. Mobile-Friendliness

| Tiêu chí | Trạng thái | Ghi chú |
|----------|-----------|---------|
| Responsive Design | 🟢 Có | Menu hamburger, content stack dọc |
| Font Size | 🟢 Đủ lớn | Đọc được trên mobile |
| Tap Targets | 🟡 Trung bình | Một số link/button quá gần nhau |
| Viewport Config | 🟢 Có | meta viewport đúng chuẩn |

**Điểm Mobile-Friendly: 7/10**

## 3. Indexing & Crawlability

| Tiêu chí | Trạng thái | Ghi chú |
|----------|-----------|---------|
| Số trang index (Google VN) | 🟡 ~19 trang | Rất ít trang được Google VN index cho phiên bản tiếng Việt |
| robots.txt | 🟡 Không truy cập được (403) | Server chặn direct fetch, cần kiểm tra cấu hình |
| sitemap.xml | 🟡 Không truy cập được (403) | Có link Sitemap trong footer nhưng không crawl được trực tiếp |
| Canonical Tags | 🟡 Cần kiểm tra | Trang đa ngôn ngữ → cần hreflang + canonical chính xác |
| Hreflang | 🔴 Không rõ | Website có nhiều ngôn ngữ nhưng không thấy hreflang tags |

**Điểm Indexing: 4/10**

## 4. Schema & Structured Data

| Loại Schema | Có/Không | Ghi chú |
|-------------|---------|---------|
| Organization | 🟢 Có | JSON-LD cơ bản |
| Product | 🟢 Có | Trên trang sản phẩm |
| Breadcrumb | 🟡 Cơ bản | Có breadcrumb nhưng chưa rõ schema |
| FAQ | 🔴 Không | Không có FAQ schema |
| Article/BlogPosting | 🔴 Không | Trang tin tức không có Article schema |
| LocalBusiness | 🔴 Không | Phù hợp cho thị trường VN nhưng chưa có |

**Điểm Schema: 4/10**

## 5. Security & HTTPS

| Tiêu chí | Trạng thái | Ghi chú |
|----------|-----------|---------|
| HTTPS | 🟢 Có | SSL certificate hoạt động |
| HTTP → HTTPS redirect | 🟢 Có | Tự động chuyển hướng |
| Mixed Content | 🟢 Không phát hiện | |

**Điểm Security: 9/10**

---

## Bảng tổng điểm Technical SEO

| Hạng mục | Điểm (/10) | Trạng thái | Ghi chú |
|----------|-----------|------------|---------|
| Core Web Vitals | 4 | 🔴 | LCP Mobile quá chậm (6.5s), CLS Desktop cao (0.301) |
| Mobile-Friendly | 7 | 🟢 | Responsive tốt, một số tap target cần cải thiện |
| Indexing | 4 | 🔴 | Rất ít trang index tại VN, thiếu hreflang |
| Schema | 4 | 🟡 | Có cơ bản nhưng thiếu FAQ, Article, LocalBusiness |
| HTTPS/Security | 9 | 🟢 | HTTPS hoạt động tốt |
| **Tổng Technical** | **28/50** | 🟡 | **Cần cải thiện đáng kể** |
