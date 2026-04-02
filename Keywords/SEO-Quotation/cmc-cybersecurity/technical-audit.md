# BÁO CÁO TECHNICAL AUDIT — DỰ ÁN GOOGLE ADS SEARCH

> **Khách hàng**: CMC Cyber Security  
> **Ngày phân tích**: 27/03/2026  
> **Phạm vi**: 2 website — shop.cmc.vn (B2C) & cmccybersecurity.com (B2B)  
> **Mục tiêu**: Chỉ ra các vấn đề kỹ thuật ảnh hưởng đến hiệu quả chạy Google Ads Search

---

## PHẦN 1: shop.cmc.vn (B2C — Phần mềm diệt virus)

### 1.1 Tổng quan hiện trạng SEMrush

| Metric | Giá trị | Đánh giá |
|--------|---------|----------|
| Authority Score | 18/100 | 🟡 Trung bình |
| Lưu lượng tự nhiên | 33/tháng | 🔴 Rất thấp |
| Từ khóa tự nhiên | 29 (-12%) | 🔴 Rất ít |
| Backlink | 144 | 🟡 Ít |
| Domain trỏ đến | 22 | 🔴 Rất ít |
| AI Tìm kiếm (AIO) | 0 | 🔴 Không hiện diện |

---

### 1.2 Vấn đề Technical NGHIÊM TRỌNG

#### 🔴 VẤN ĐỀ #1: Website là React SPA — Google Ads Landing Page không render được nội dung

**Mức độ**: ⚠️ CRITICAL

```html
<!-- Toàn bộ HTML trả về cho crawler/bot -->
<html lang="en">
<body>
  <noscript>You need to enable JavaScript to run this app.</noscript>
  <div id="root"></div>
  <script defer src="/static/js/main.be89507b.js"></script>
</body>
</html>
```

**Hậu quả cho Google Ads:**
- Google Ads Bot cần render JavaScript để thấy nội dung → **tăng thời gian load**
- **Landing Page Experience** bị đánh giá thấp → **Quality Score giảm** → **CPC tăng**
- Không có nội dung HTML tĩnh → Google khó đánh giá **ad relevance** giữa keyword và landing page
- Nếu bot không render được JS → hiển thị trang trắng → **bounce rate tăng vọt**

**Khuyến nghị:**
- Chuyển sang **Server-Side Rendering (SSR)** hoặc **Static Site Generation (SSG)** với Next.js
- Hoặc tối thiểu: triển khai **Pre-rendering** cho các trang landing page quan trọng

---

#### 🔴 VẤN ĐỀ #2: Không có Sitemap.xml

**Mức độ**: ⚠️ HIGH

- URL `https://shop.cmc.vn/sitemap.xml` trả về nội dung HTML React app thay vì XML sitemap hợp lệ
- robots.txt trống rỗng (chỉ có `User-agent: * / Disallow:`)
- Không khai báo sitemap trong robots.txt

**Hậu quả cho Google Ads:**
- Google không index đầy đủ các trang sản phẩm → **giảm ad relevance**
- Landing page không được index → có thể bị cảnh báo "Landing page not crawlable"

---

#### 🔴 VẤN ĐỀ #3: Meta Tags sai & thiếu

**Mức độ**: ⚠️ HIGH

| Meta Tag | Giá trị hiện tại | Vấn đề |
|----------|------------------|--------|
| `<html lang>` | `"en"` | ❌ Phải là `"vi"` — website tiếng Việt |
| `<title>` | `"Shop \| CMC Cyber Security"` | ❌ Không chứa keyword target |
| `<meta description>` | **KHÔNG CÓ** | ❌ Hoàn toàn thiếu |
| `og:title` | `"Trang chủ"` | ❌ Quá generic |
| `og:description` | **KHÔNG CÓ** | ❌ Thiếu |

**Hậu quả cho Google Ads:**
- Google Ads Quality Score bị ảnh hưởng vì landing page thiếu **keyword relevance signals**
- `lang="en"` khiến Google có thể nhầm ngôn ngữ → hiển thị sai audience

---

#### 🔴 VẤN ĐỀ #4: Hiệu suất tải trang CỰC KÉM trên Mobile

**Mức độ**: ⚠️ CRITICAL

| Metric | Mobile | Desktop | Ngưỡng tốt |
|--------|--------|---------|------------|
| **Performance Score** | **50** 🔴 | **48** 🔴 | ≥ 90 |
| **LCP** | **16.5 giây** 🔴 | 2.7 giây 🟡 | ≤ 2.5s |
| **TBT** | 370ms 🟡 | 730ms 🔴 | ≤ 200ms |
| **CLS** | 0 🟢 | 0.134 🟡 | ≤ 0.1 |
| **Field Data** | ❌ Không có | ❌ Không có | — |

**LCP 16.5 giây trên mobile là thảm họa cho Google Ads:**
- >70% traffic Google Ads đến từ mobile
- Người dùng rời trang sau 3 giây → **bounce rate >90%** dự kiến
- Google sẽ **giảm Quality Score** → CPC tăng 20-50%

**Nguyên nhân chính:**
1. Render-blocking resources: tiết kiệm được **1,950ms** nếu tối ưu
2. Webfont chưa optimize: delay **490ms** text render
3. Hình ảnh chưa tối ưu: lãng phí **~7MB** bandwidth (Desktop)
4. Cache policy quá ngắn hoặc không set

---

#### 🟡 VẤN ĐỀ #5: Thiếu Conversion Tracking Setup cho Google Ads

- Chưa xác nhận được `gtag.js` hoặc Google Tag Manager được cài đặt đúng
- Cần verify: conversion event tracking trên trang "Thank You" / "Thanh toán thành công"
- Không có Google Ads remarketing tag rõ ràng

---

#### 🟡 VẤN ĐỀ #6: Schema Markup thiếu hoàn toàn

- Không có **Product Schema** cho sản phẩm phần mềm (giá, review, availability)
- Không có **Organization Schema**
- Không có **Breadcrumb Schema**
- Không có **FAQ Schema**

**Hậu quả cho Google Ads:**
- Không hiện rich snippets → CTR quảng cáo không tận dụng được structured data
- Mất cơ hội hiện **price extension** từ structured data

---

### 1.3 Vấn đề UX/CTA cho Landing Page Ads

#### CTA hiện tại và đề xuất tối ưu

| CTA hiện tại | Vấn đề | Đề xuất thay thế |
|-------------|--------|-----------------|
| "MUA NGAY" | Quá trực tiếp, không tạo giá trị | "Bảo vệ máy tính ngay hôm nay" |
| "TẢI VỀ" | Không rõ hành động cụ thể | "Tải CMC AntiVirus bản quyền" |
| "TÌM HIỂU THÊM" | Quá chung chung | "Xem các gói bảo vệ" |

#### Trust signals hiện có (TỐT):
- ✅ Bộ Công an & Bộ Quốc phòng sử dụng từ 2014
- ✅ Chứng chỉ VB100 quốc tế
- ✅ Database 10+ triệu mẫu virus
- ✅ Giá rõ ràng: 239.000 VND/năm

#### Cần bổ sung:
- ❌ Testimonial/review từ khách hàng
- ❌ So sánh với đối thủ (Kaspersky, BKAV, Norton)
- ❌ Guarantee/đảm bảo hoàn tiền
- ❌ Urgency/scarcity elements cho ads landing page
- ❌ Form đăng ký dùng thử trên chính trang (above the fold)

---

### 1.4 Bảng điểm Technical — shop.cmc.vn

| Hạng mục | Điểm (/10) | Trạng thái | Ghi chú |
|----------|-----------|------------|---------|
| Core Web Vitals | 2/10 | 🔴 | LCP 16.5s mobile, không có field data |
| Mobile-Friendly | 7/10 | 🟢 | Responsive tốt, nhưng tốc độ quá chậm |
| Indexing & Crawlability | 2/10 | 🔴 | SPA không render, không sitemap |
| Schema & Structured Data | 1/10 | 🔴 | Hoàn toàn thiếu |
| HTTPS/Security | 8/10 | 🟢 | SSL hợp lệ, HTTPS redirect OK |
| Landing Page cho Ads | 4/10 | 🟡 | CTA yếu, thiếu conversion elements |
| **TỔNG** | **24/60** | 🔴 | **Cần cải thiện nghiêm trọng** |

---

---

## PHẦN 2: cmccybersecurity.com (B2B — Giải pháp an ninh mạng)

### 2.1 Tổng quan hiện trạng SEMrush

| Metric | Giá trị | Đánh giá |
|--------|---------|----------|
| Authority Score | 25/100 | 🟢 Tốt |
| Lưu lượng tự nhiên | 609/tháng (+11%) | 🟡 Trung bình |
| Từ khóa tự nhiên | 279 (-13%) | 🟡 Đang giảm |
| Backlink | 864 | 🟢 Khá |
| Domain trỏ đến | 346 | 🟢 Tốt |
| AI Tìm kiếm (AIO) | 14 (hiện 6% traffic) | 🟢 Có presence |

---

### 2.2 Vấn đề Technical NGHIÊM TRỌNG

#### 🔴 VẤN ĐỀ #1: Lỗi chính tả tên thương hiệu trên toàn bộ trang Dịch vụ

**Mức độ**: ⚠️ CRITICAL

Trên trang `https://cmccybersecurity.com/dich-vu/`, tên công ty bị sai chính tả thành **"CMC CYBER SECURITTY"** (thừa chữ T) tại **ít nhất 4 dịch vụ**:

1. ❌ **Dịch vụ tư vấn, đánh giá và cấp chứng chỉ PCI-DSS** → "CMC CYBER SECURITTY là doanh nghiệp..."
2. ❌ **Dịch vụ Rà soát đánh giá tấn công APT** → "CMC CYBER SECURITTY là doanh nghiệp..."
3. ❌ **Dịch vụ Rà quét lỗ hổng bảo mật** → "CMC CYBER SECURITTY là doanh nghiệp..."
4. ❌ **Dịch vụ CMC Threats Intelligence** → "CMC CYBER SECURITTY là doanh nghiệp..."

**Hậu quả cho Google Ads:**
- Khách hàng B2B click vào quảng cáo → thấy lỗi chính tả → **mất niềm tin ngay lập tức**
- Đây là doanh nghiệp an ninh mạng — lỗi chính tả trên chính website tạo ấn tượng **thiếu chuyên nghiệp**
- **Conversion rate giảm** → CPA tăng

---

#### 🔴 VẤN ĐỀ #2: Nội dung dịch vụ bị DUPLICATE — Copy-paste mô tả PCI DSS cho nhiều dịch vụ khác nhau

**Mức độ**: ⚠️ CRITICAL

**4 dịch vụ hoàn toàn khác nhau** nhưng dùng **chung 1 đoạn mô tả PCI DSS**:

```
"CMC CYBER SECURITTY là doanh nghiệp Việt Nam được quyền cấp chứng chỉ PCI DSS. 
PCI DSS là một tiêu chuẩn an ninh thông tin bắt buộc đối với khách hàng là 
các ngân hàng, cổng thanh toán,…"
```

| Dịch vụ | Mô tả đúng? |
|---------|-------------|
| Dịch vụ tư vấn, đánh giá và cấp chứng chỉ PCI-DSS | ✅ Phù hợp |
| Dịch vụ Rà soát đánh giá tấn công APT | ❌ Sai — cần mô tả APT Assessment |
| Dịch vụ Rà quét lỗ hổng bảo mật | ❌ Sai — cần mô tả Vulnerability Scanning |
| Dịch vụ CMC Threats Intelligence | ❌ Sai — cần mô tả Threat Intelligence |

**Hậu quả cho Google Ads:**
- Keyword "vulnerability assessment" hoặc "APT" → landing page nói về PCI DSS → **ad relevance = 0**
- Google Ads **Quality Score giảm mạnh** vì nội dung không match search intent
- Khách hàng B2B chuyên môn cao → phát hiện ngay → **bounce**

---

#### 🔴 VẤN ĐỀ #3: Hiệu suất tải trang — Core Web Vitals FAIL

**Mức độ**: ⚠️ HIGH

| Metric | Mobile (Field) | Mobile (Lab) | Desktop (Field) | Desktop (Lab) | Ngưỡng tốt |
|--------|------|------|---------|------|------------|
| **Performance** | — | **61** 🟡 | — | **68** 🟡 | ≥ 90 |
| **LCP** | **3.9s** 🔴 | **21.6s** 🔴 | **6.9s** 🔴 | **5.1s** 🔴 | ≤ 2.5s |
| **INP** | N/A | — | **50ms** 🟢 | — | ≤ 200ms |
| **CLS** | **0** 🟢 | — | **0.09** 🟢 | — | ≤ 0.1 |
| **FCP** | — | **2.6s** 🟡 | — | **3.4s** 🔴 | ≤ 1.8s |
| **TTFB** | — | **1.7s** 🟡 | — | **2.8s** 🔴 | ≤ 0.8s |

**LCP 6.9 giây trên Desktop là vấn đề lớn cho B2B Ads:**
- Khách hàng B2B thường search từ Desktop trong giờ làm việc
- TTFB 2.8s → server response quá chậm → có thể do shared hosting hoặc plugin nặng

**Nguyên nhân chính:**
1. **Webfont load**: tiết kiệm **3,000ms** nếu dùng `font-display: swap`
2. **Render-blocking resources**: tiết kiệm **1,440ms**
3. **Cache policy ngắn**: nhiều static asset không cache hoặc cache quá ngắn
4. **Server chậm**: TTFB 1.7-2.8s → cần upgrade hosting hoặc implement CDN

---

#### 🟡 VẤN ĐỀ #4: Footer có duplicate links

Trong phần footer, danh sách "GIẢI PHÁP & DỊCH VỤ" hiển thị **trùng lặp 2 lần** cùng 4 link:
- Sản phẩm diệt virus & Giải pháp phòng chống mã độc (x2)
- Dịch vụ Trung tâm Điều hành An ninh mạng (x2)
- Dịch vụ đánh giá và kiểm định An ninh ATTT (x2)
- Dịch vụ tư vấn & Đánh giá cấp chứng chỉ (x2)

**Hậu quả**: Không ảnh hưởng trực tiếp đến Ads, nhưng gây ấn tượng website **chưa hoàn thiện**.

---

#### 🟡 VẤN ĐỀ #5: Thiếu CTA trên Landing Page cho Ads

| Trang | CTA có sẵn | Vị trí CTA | Vấn đề |
|-------|-----------|------------|--------|
| Homepage | "Đọc tiếp", "Xem thêm" | Giữa trang | ❌ Không có CTA conversion (Liên hệ, Báo giá) |
| Trang Dịch vụ | "Liên hệ ngay" | Cuối trang | ❌ Chỉ ở cuối, không ở above-the-fold |
| Trang Pentest | "GỬI THÔNG TIN" (form) | Cuối trang | ❌ Form ở cuối, hero section không có CTA |

**Khuyến nghị cho Google Ads:**
- Thêm CTA "Nhận báo giá miễn phí" hoặc "Tư vấn chuyên gia" ở **hero section** (above the fold)
- Thêm **sticky CTA** hoặc **floating button** trên mobile
- Mỗi service page cần có form lead capture ở đầu trang

---

#### 🟡 VẤN ĐỀ #6: Sitemap & Indexing

- ✅ Sitemap hoạt động: `sitemap_index.xml` với 10 sub-sitemaps (Yoast SEO)
- ✅ robots.txt khai báo sitemap đúng
- 🟡 Có sitemap cho `post_tag` và `author` → nên noindex để tránh thin content index
- 🟡 sitemap `tuyen_dung` (tuyển dụng) lastmod: 25/09/2025 → có thể outdated

---

### 2.3 Bảng điểm Technical — cmccybersecurity.com

| Hạng mục | Điểm (/10) | Trạng thái | Ghi chú |
|----------|-----------|------------|---------|
| Core Web Vitals | 4/10 | 🟡 | LCP fail cả mobile & desktop |
| Mobile-Friendly | 7/10 | 🟢 | Responsive, nhưng UX cần cải thiện |
| Indexing & Crawlability | 7/10 | 🟢 | Sitemap tốt, cần cleanup tags |
| Schema & Structured Data | 3/10 | 🟡 | Cơ bản qua Yoast, thiếu Service schema |
| HTTPS/Security | 8/10 | 🟢 | SSL OK, HTTPS redirect OK |
| Content Quality | 2/10 | 🔴 | Typo tên brand, duplicate descriptions |
| Landing Page cho Ads | 3/10 | 🔴 | CTA yếu, form ở cuối trang |
| **TỔNG** | **34/70** | 🟡 | **Cần cải thiện nhiều điểm** |

---

---

## PHẦN 3: TỔNG HỢP ĐỀ XUẤT ƯU TIÊN CHO GOOGLE ADS

### 🚨 Ưu tiên FIX NGAY (Trước khi chạy Ads)

| # | Website | Vấn đề | Hành động | Timeline |
|---|---------|--------|-----------|----------|
| 1 | shop.cmc.vn | React SPA không render content | Triển khai SSR/Pre-rendering cho landing page | 1-2 tuần |
| 2 | shop.cmc.vn | LCP 16.5s mobile | Optimize images, defer JS, implement CDN | 1 tuần |
| 3 | shop.cmc.vn | Thiếu meta description + lang sai | Sửa sang `lang="vi"`, thêm meta description | 1 ngày |
| 4 | cmccybersecurity.com | Typo "SECURITTY" x4 | Sửa thành "SECURITY" | 30 phút |
| 5 | cmccybersecurity.com | 3 dịch vụ dùng sai mô tả PCI DSS | Viết mô tả riêng cho APT, Vulnerability, Threat Intel | 1-2 ngày |
| 6 | cmccybersecurity.com | CTA không ở above-the-fold | Thêm CTA + form lead capture ở hero section | 1-2 ngày |

### 📋 Ưu tiên TRUNG BÌNH (Tuần 1-2 của campaign)

| # | Website | Vấn đề | Hành động |
|---|---------|--------|-----------|
| 7 | shop.cmc.vn | Thiếu conversion tracking | Cài gtag.js + setup conversion events |
| 8 | shop.cmc.vn | CTA "Mua ngay" quá generic | Đổi thành "Bảo vệ máy tính ngay" / "Tải bản quyền" |
| 9 | shop.cmc.vn | Không có sitemap | Generate sitemap.xml, khai báo trong robots.txt |
| 10 | cmccybersecurity.com | LCP 6.9s desktop | Optimize server (TTFB), CDN, font-display:swap |
| 11 | cmccybersecurity.com | Footer link duplicate | Xóa bộ link trùng |

### 📌 Ưu tiên DÀI HẠN (Tháng 2-3)

| # | Website | Vấn đề | Hành động |
|---|---------|--------|-----------|
| 12 | shop.cmc.vn | Thiếu schema markup | Thêm Product, Organization, FAQ schema |
| 13 | shop.cmc.vn | Thiếu trust signals | Thêm reviews, so sánh đối thủ, đảm bảo hoàn tiền |
| 14 | cmccybersecurity.com | Thiếu Service schema | Thêm schema cho từng dịch vụ chuyên biệt |
| 15 | cmccybersecurity.com | Tag/author sitemap | Noindex hoặc cleanup thin content |

---

## PHẦN 4: KHUYẾN NGHỊ CẤU TRÚC CAMPAIGN GOOGLE ADS

### Campaign B2C — shop.cmc.vn

**Campaign Objective**: Purchase / Lead (Trial Download)

| Ad Group | Keywords chính | Landing Page | CTA đề xuất |
|----------|---------------|-------------|-------------|
| [Diệt virus] Brand | phần mềm diệt virus cmc, cmc antivirus | /cmc-antivirus | "Tải CMC AntiVirus bản quyền" |
| [Diệt virus] Generic | phần mềm diệt virus, ứng dụng diệt virus | /cmc-antivirus (so sánh) | "Dùng thử miễn phí 30 ngày" |
| [Diệt virus] Intent | cách diệt virus trên máy tính, diệt virus win 10 | Blog/hướng dẫn → CTA mua | "Giải pháp diệt virus chuyên nghiệp" |
| [Diệt virus] Commercial | phần mềm diệt virus bản quyền, mua bản quyền diệt virus | /cmc-antivirus (pricing) | "Mua bản quyền chỉ 239K/năm" |

### Campaign B2B — cmccybersecurity.com

**Campaign Objective**: Lead Generation (Form submit / Call)

| Ad Group | Keywords chính | Landing Page | CTA đề xuất |
|----------|---------------|-------------|-------------|
| [Pentest] | pentest, dịch vụ pentest, pentest services | /dich-vu/pentest | "Nhận báo giá Pentest" |
| [PCI DSS] | pci dss certification, chứng chỉ pci dss | /dich-vu/pci-dss | "Tư vấn lộ trình PCI DSS" |
| [ISO 27001] | iso/iec 27001, tiêu chuẩn iso iec 27001 | /dich-vu/iso-27001 | "Đánh giá ISO 27001 miễn phí" |
| [Security Audit] | security audit, vulnerability assessment | /dich-vu/security-audit | "Đặt lịch kiểm định hệ thống" |
| [SOC] | trung tâm điều hành an ninh mạng soc | /dich-vu/soc | "Tư vấn giải pháp SOC" |

---

> **Lưu ý quan trọng**: Các vấn đề #1-#6 (ưu tiên FIX NGAY) **BẮT BUỘC phải sửa trước khi bắt đầu chạy Google Ads**. Nếu không, ngân sách quảng cáo sẽ bị lãng phí do Quality Score thấp, bounce rate cao, và conversion rate gần bằng 0.
