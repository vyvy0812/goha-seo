# 🔴 BÁO CÁO KỸ THUẬT SEO — zamst.vn

> **Ngày phân tích:** 19/03/2026
> **Đánh giá chung:** WEBSITE BỊ HACK NGHIÊM TRỌNG — Cần xử lý KHẨN CẤP
> **Mức độ rủi ro:** 🔴 CRITICAL

---

## 1. TỔNG QUAN VẤN ĐỀ

### 1.1 Japanese SEO Spam Hack (Cloaking Attack) — 🔴 CRITICAL

Website zamst.vn đang bị tấn công **Japanese Keyword Hack** — một trong những hình thức hack SEO phổ biến và nguy hiểm nhất. Hacker đã cài mã độc vào WordPress core, tạo ra **hàng nghìn trang spam bằng tiếng Nhật** được Google index.

**Bằng chứng:**

| Tiêu chí | Chi tiết |
|----------|---------|
| **Google SERP** | Tìm `site:zamst.vn` trên Google → hiển thị hàng nghìn trang tiếng Nhật (đồ chơi, thẻ bài, đá quý, thời trang Nhật) |
| **Cloaking** | Trang hiển thị bình thường khi truy cập bằng trình duyệt, nhưng Google thấy nội dung spam tiếng Nhật |
| **URL pattern** | Các URL spam dạng `?p=28963530413825` — ID post rất lớn, không tồn tại trong DB thật |
| **Truy cập trực tiếp** | Khi truy cập URL spam bằng trình duyệt → trả về 404 (cơ chế ẩn mã độc) |

**Cơ chế hoạt động:**
```
Googlebot → zamst.vn/?p=xxxxx → Mã độc phát hiện User-Agent → Trả nội dung spam tiếng Nhật
Người dùng → zamst.vn/?p=xxxxx → Phát hiện trình duyệt thường → Trả 404/trang bình thường
```

---

## 2. PHÂN TÍCH TECHNICAL CHI TIẾT

### 2.1 Core Web Vitals & Tốc độ

| Metric | Mobile | Desktop | Đánh giá |
|--------|--------|---------|----------|
| **Performance Score** | 80 | 97 | 🟡 Mobile cần cải thiện |
| **LCP** | 4.6s | 0.7s | 🔴 Mobile quá chậm (chuẩn < 2.5s) |
| **INP/TBT** | 0ms | 0ms | 🟢 Tốt |
| **CLS** | 0.012 | 0.004 | 🟢 Tốt |
| **SEO Score (Lighthouse)** | 54 | 54 | 🔴 Rất thấp |

**Vấn đề LCP Mobile (4.6s):**
- Render-blocking resources (CSS/JS chặn render)
- Hình ảnh chưa tối ưu — tiết kiệm được ~462 KiB
- Thiếu lazy loading cho ảnh below-the-fold
- Cache policy chưa hiệu quả cho static assets

---

### 2.2 Indexing & Crawlability — 🔴 CRITICAL

| Kiểm tra | Kết quả | Đánh giá |
|----------|---------|----------|
| **sitemap.xml** | ❌ 404 Not Found | 🔴 |
| **sitemap_index.xml** | ❌ 404 Not Found | 🔴 |
| **wp-sitemap.xml** | ❌ 404 Not Found | 🔴 |
| **robots.txt** | ✅ Có (Cloudflare managed) | 🟡 Lỗi cú pháp |
| **Noindex** | ❌ Trang bị block khỏi indexing | 🔴 |
| **Meta Description** | ❌ Thiếu | 🔴 |
| **Trang Google index** | ⚠️ Hàng nghìn trang spam tiếng Nhật | 🔴 |

**Vấn đề nghiêm trọng:**
1. **Không có sitemap** → Google không có bản đồ chính thức để crawl
2. **Trang bị noindex** → Trang chính không được index (có thể do mã độc chèn thêm)
3. **robots.txt lỗi** → Có lỗi cú pháp ảnh hưởng crawl
4. **Không có meta description** → Không hiển thị mô tả trên SERP

---

### 2.3 Security Audit — Tổng hợp từ báo cáo đồng nghiệp

#### 🔴 CRITICAL (2 lỗi)

**① XML-RPC Fully Exposed** (`/xmlrpc.php`)
- Trả về 80+ methods bao gồm `system.multicall`, `wp.getUsersBlogs`, `pingback.ping`
- **Rủi ro:** Brute-force mật khẩu (hàng trăm lần thử/request), DDoS amplification, SSRF
- **Cách sửa:**
```apache
# Thêm vào .htaccess
<Files xmlrpc.php>
    Require all denied
</Files>
```
Hoặc tạo Cloudflare WAF rule block POST đến `/xmlrpc.php`

**② wp-admin/install.php trả về 200**
- Nếu DB bị mất kết nối → attacker có thể re-initialize WordPress và chiếm quyền admin
- **Cách sửa:**
```apache
# Thêm vào .htaccess
<Files install.php>
    Require all denied
</Files>
```

---

#### 🟠 HIGH (4 lỗi)

**③ Thiếu HSTS Header**
- HTTP→HTTPS redirect có (301) nhưng không có HSTS → vulnerable với SSL stripping (MITM)
- **Cách sửa:** Vào Cloudflare → SSL/TLS → Edge Certificates → Bật HSTS
```
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

**④ readme.html Exposed** (`/readme.html`)
- Xác nhận WordPress installation, cung cấp system requirements info
- **Cách sửa:** Xóa file `readme.html` khỏi root WordPress

**⑤ wp-links-opml.php Exposed**
- Trả về 200 với OPML XML chứa site title → information disclosure
- **Cách sửa:** Block hoặc xóa file

**⑥ Login Page không có CAPTCHA** (`/wp-login.php`)
- Không CAPTCHA, không rate limiting → brute-force được từ 2 vectors (xmlrpc + login form)
- **Cách sửa:**
  - Cài Cloudflare Turnstile (miễn phí) trên wp-login
  - Cài plugin **Limit Login Attempts Reloaded**
  - Cân nhắc plugin **WPS Hide Login** để đổi URL đăng nhập

---

#### 🟡 MEDIUM (5 lỗi)

| # | Lỗi | Rủi ro | Cách sửa |
|---|------|--------|----------|
| ⑦ | Thiếu X-Frame-Options | Clickjacking | Header: `X-Frame-Options: SAMEORIGIN` |
| ⑧ | Thiếu Content-Security-Policy | XSS, resource injection | Triển khai CSP (bắt đầu report-only) |
| ⑨ | Thiếu Permissions-Policy | Camera/mic/GPS không bị giới hạn | `Permissions-Policy: camera=(), microphone=(), geolocation=()` |
| ⑩ | Thiếu Referrer-Policy | URL leak ra ngoài | `Referrer-Policy: strict-origin-when-cross-origin` |
| ⑪ | WordPress Version lộ | Attacker target exploit theo version | Xóa generator meta tag trong functions.php |

---

#### 🟢 LOW (3 lỗi)

| # | Lỗi | Cách sửa |
|---|------|----------|
| ⑫ | PHP Version lộ (`X-Powered-By: PHP/8.2.29`) | php.ini: `expose_php = Off` |
| ⑬ | wp-cron.php public | `define('DISABLE_WP_CRON', true);` + server cron |
| ⑭ | Plugin readme.txt lộ version | Block access trong server config |

---

### 2.4 Điểm mạnh (Defenses đã có)

| Check | Status |
|-------|--------|
| HTTPS | ✅ Active, HTTP→HTTPS 301 redirect |
| REST API Users | ✅ Blocked (401 Unauthorized) |
| Author Enumeration | ✅ Trả 404 cho `/?author=N` |
| X-Content-Type-Options | ✅ Qua Cloudflare |
| File nhạy cảm (.env, .git, wp-config backup, debug.log) | ✅ Blocked (403) |
| Directory listing (uploads) | ✅ Blocked (403) |
| CDN/WAF | ✅ Cloudflare active |
| Mixed content | ✅ Không phát hiện |
| WordPress version | ✅ Latest (6.9.4) |
| SSL Certificate | ✅ Valid (hết hạn 15/05/2026) |

---

### 2.5 Technology Stack

| Component | Value |
|-----------|-------|
| WordPress | 6.9.4 (latest) |
| PHP | 8.2.29 |
| Web Server | LiteSpeed |
| Hosting | Hostinger (hpanel) |
| CDN/WAF | Cloudflare |
| Theme | Flatsome 3.20.1 (UX-Themes) |
| WooCommerce | 10.4.4 |
| Contact Form 7 | 6.1.4 |
| GTranslate | 3.0.9 |
| SSL Issuer | Google Trust Services (WE1) |

---

## 3. BẢNG ĐIỂM TECHNICAL SEO

| Hạng mục | Điểm (/10) | Trạng thái | Ghi chú |
|----------|-----------|------------|---------|
| Core Web Vitals (Mobile) | 5/10 | 🟡 | LCP mobile 4.6s, cần tối ưu |
| Core Web Vitals (Desktop) | 9/10 | 🟢 | Xuất sắc |
| Mobile-Friendly | 7/10 | 🟢 | Responsive OK, LCP cần cải thiện |
| Indexing & Sitemap | 1/10 | 🔴 | KHÔNG có sitemap, bị noindex, nghìn trang spam |
| Schema & Structured Data | 3/10 | 🔴 | Thiếu schema cơ bản (Product, Breadcrumb, Organization) |
| HTTPS/Security | 3/10 | 🔴 | SSL OK nhưng 14 lỗ hổng bảo mật nghiêm trọng |
| **TỔNG TECHNICAL** | **28/60** | 🔴 | **YẾU — BỊ HACK + nhiều lỗ hổng** |

---

## 4. KẾ HOẠCH SỬA CHỮA — CHIA THEO ĐỘ ƯU TIÊN

### 🚨 PHASE 1: XỬ LÝ HACK — KHẨN CẤP (Ngay lập tức, trong 1-3 ngày)

#### Bước 1: Sao lưu toàn bộ trước khi xử lý
```bash
# Backup toàn bộ qua Hostinger hpanel
# Backup database riêng biệt
# Lưu danh sách plugin/theme đang dùng
```

#### Bước 2: Quét và xóa mã độc

1. **Kiểm tra `.htaccess`** (file GỐC, root WordPress)
   - Tìm và xóa code lạ, đặc biệt:
     - Dòng chứa `base64_decode`, `eval()`, `preg_replace` với pattern lạ
     - RewriteRule chuyển hướng đến domain lạ
     - Điều kiện RewriteCond kiểm tra User-Agent (đây là cơ chế cloaking)
   - **Thay bằng .htaccess sạch:**
   ```apache
   # BEGIN WordPress
   <IfModule mod_rewrite.c>
   RewriteEngine On
   RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
   RewriteBase /
   RewriteRule ^index\.php$ - [L]
   RewriteCond %{REQUEST_FILENAME} !-f
   RewriteCond %{REQUEST_FILENAME} !-d
   RewriteRule . /index.php [L]
   </IfModule>
   # END WordPress
   ```

2. **Kiểm tra `wp-config.php`**
   - Tìm code lạ chèn thêm (thường ở đầu hoặc cuối file)
   - Đặc biệt tìm: `@include`, `require_once` trỏ đến file lạ

3. **Kiểm tra WordPress Core Files**
   - So sánh `index.php`, `wp-blog-header.php`, `wp-load.php` với bản gốc
   - **Tốt nhất: Cài lại WordPress core** (giữ lại `wp-config.php` và folder `wp-content`)
   ```bash
   # Tải WordPress 6.9.4 sạch
   # Xóa tất cả file ngoại trừ wp-config.php và wp-content/
   # Upload lại core files sạch
   ```

4. **Quét thư mục `wp-content/`**
   - `wp-content/uploads/` → Tìm file `.php` (KHÔNG nên có file PHP trong uploads)
   ```bash
   # Tìm file PHP trong uploads
   find wp-content/uploads -name "*.php" -type f
   ```
   - `wp-content/themes/flatsome/functions.php` → Kiểm tra code chèn thêm
   - `wp-content/plugins/` → Tìm plugin lạ không nằm trong danh sách (CF7, WooCommerce, GTranslate)

5. **Kiểm tra Database**
   - Bảng `wp_users` → Tìm user admin lạ, xóa ngay
   - Bảng `wp_options` → Tìm option chứa script lạ (`siteurl`, `home`, `active_plugins`)
   - Bảng `wp_posts` → Tìm post có ID cực lớn (>1 triệu) — đây là spam posts
   ```sql
   -- Tìm user lạ
   SELECT * FROM wp_users ORDER BY ID DESC;
   
   -- Tìm post spam (ID lớn bất thường)
   SELECT ID, post_title, post_status FROM wp_posts WHERE ID > 1000000 LIMIT 50;
   
   -- Kiểm tra siteurl và home
   SELECT * FROM wp_options WHERE option_name IN ('siteurl', 'home', 'active_plugins');
   ```

#### Bước 3: Đổi toàn bộ credential
- ✅ Mật khẩu WordPress Admin (tất cả user)
- ✅ Mật khẩu Database
- ✅ Mật khẩu SFTP/FTP
- ✅ API Keys (nếu có)
- ✅ WordPress Security Keys (regenerate trong wp-config.php)
  - Truy cập: https://api.wordpress.org/secret-key/1.1/salt/
  - Copy và thay thế toàn bộ block `AUTH_KEY`, `SECURE_AUTH_KEY`... trong wp-config.php

#### Bước 4: Cài plugin bảo mật
- Cài **Wordfence** hoặc **Sucuri Security** → chạy Full Scan
- Cài **Limit Login Attempts Reloaded**
- Bật 2FA cho tất cả admin accounts

---

### 🔧 PHASE 2: VÁ LỖ HỔNG BẢO MẬT (Trong tuần đầu)

#### Bước 5: Block attack vectors
```apache
# Thêm vào .htaccess sau khi đã clean

# Block xmlrpc.php
<Files xmlrpc.php>
    Require all denied
</Files>

# Block install.php
<Files install.php>
    Require all denied
</Files>

# Block readme.html
<Files readme.html>
    Require all denied
</Files>

# Block plugin readme.txt
<DirectoryMatch "wp-content/plugins">
    <Files readme.txt>
        Require all denied
    </Files>
    <Files README.txt>
        Require all denied
    </Files>
</DirectoryMatch>

# Block wp-links-opml.php
<Files wp-links-opml.php>
    Require all denied
</Files>
```

#### Bước 6: Thêm Security Headers
Cấu hình trong **Cloudflare** (Workers hoặc Transform Rules):
```
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

#### Bước 7: Ẩn thông tin nhạy cảm
```php
// Thêm vào functions.php của theme (hoặc tạo custom plugin)

// Xóa WordPress version
remove_action('wp_head', 'wp_generator');

// Xóa version từ CSS/JS
function remove_version_scripts_styles($src) {
    if (strpos($src, 'ver=')) {
        $src = remove_query_arg('ver', $src);
    }
    return $src;
}
add_filter('script_loader_src', 'remove_version_scripts_styles', 9999);
add_filter('style_loader_src', 'remove_version_scripts_styles', 9999);
```

```ini
; Trong php.ini (Hostinger hpanel → PHP Configuration)
expose_php = Off
```

#### Bước 8: Server-side Cron
```php
// Thêm vào wp-config.php
define('DISABLE_WP_CRON', true);
```
Sau đó trong Hostinger hpanel → Cron Jobs, thêm:
```
*/15 * * * * curl -s https://zamst.vn/wp-cron.php > /dev/null 2>&1
```

---

### 📋 PHASE 3: KHÔI PHỤC SEO (Trong tháng đầu)

#### Bước 9: Xử lý Google Search Console

1. **Xác minh quyền sở hữu** trên Google Search Console (nếu chưa có)
2. **URL Removal Tool:**
   - Gỡ toàn bộ URL spam tiếng Nhật
   - Sử dụng tính năng "Remove URLs with this prefix" cho pattern spam
3. **Submit Sitemap mới:**
   - Cài plugin **Yoast SEO** hoặc **Rank Math** để tự động generate sitemap
   - Submit `https://zamst.vn/sitemap.xml` trong Search Console
4. **Request Indexing** cho các trang chính (homepage, product pages, blog)
5. **Security Issues tab:** Kiểm tra nếu Google đã phát hiện và gắn cờ

#### Bước 10: Tạo XML Sitemap

**Hiện tại KHÔNG có sitemap nào hoạt động:**
- `/sitemap.xml` → 404
- `/sitemap_index.xml` → 404
- `/wp-sitemap.xml` → 404

**Cách sửa:**
- Cài **Yoast SEO** hoặc **Rank Math** → tự động tạo sitemap
- Kiểm tra robots.txt trỏ đúng URL sitemap
- Submit trong Google Search Console

#### Bước 11: Sửa On-Page SEO cơ bản

| Vấn đề | Cách sửa |
|--------|----------|
| Thiếu Meta Description | Thêm meta description cho tất cả trang qua SEO plugin |
| Trang bị noindex | Kiểm tra và gỡ directive noindex (có thể do mã độc chèn) |
| Thiếu Schema | Triển khai Organization, Product, Breadcrumb schema qua Yoast/Rank Math |
| robots.txt lỗi | Sửa lỗi cú pháp, đảm bảo sitemap URL chính xác |

---

### 🔄 PHASE 4: TỐI ƯU HIỆU NĂNG (Tháng 2-3)

#### Bước 12: Cải thiện LCP Mobile (4.6s → dưới 2.5s)

| Action | Chi tiết | Tiết kiệm ước tính |
|--------|---------|-------------------|
| Optimize Images | Chuyển sang WebP, nén ảnh, lazy loading | ~462 KiB |
| Eliminate Render-Blocking | Defer/async CSS/JS không critical | 1-2s |
| Preload LCP Image | `<link rel="preload" as="image">` cho banner chính | 0.5-1s |
| Browser Caching | Cache static assets 1 năm | Repeat visits nhanh hơn |
| Critical CSS | Inline critical CSS, defer non-critical | 0.5-1s |

#### Bước 13: Tối ưu thêm
- Enable Gzip/Brotli compression (qua Cloudflare)
- Minify CSS/JS (WP Rocket hoặc LiteSpeed Cache)
- Tối ưu font loading (`font-display: swap`)
- Giảm DOM size nếu quá lớn

---

## 5. CHECKLIST TỔNG HỢP

### Ngay lập tức (1-3 ngày) 🚨
- [ ] Backup toàn bộ website + database
- [ ] Scan và xóa mã độc (.htaccess, wp-config.php, core files)
- [ ] Cài lại WordPress core sạch
- [ ] Quét wp-content/uploads tìm file PHP
- [ ] Kiểm tra database (wp_users, wp_posts, wp_options)
- [ ] Đổi TẤT CẢ mật khẩu (WP admin, DB, FTP, API keys)
- [ ] Regenerate WordPress Security Keys
- [ ] Cài Wordfence/Sucuri scan toàn bộ
- [ ] Block xmlrpc.php
- [ ] Block install.php
- [ ] Thêm CAPTCHA cho wp-login.php

### Trong tuần đầu 🔧
- [ ] Thêm HSTS header (qua Cloudflare)
- [ ] Thêm security headers (X-Frame-Options, CSP, Referrer-Policy, Permissions-Policy)
- [ ] Xóa readme.html
- [ ] Block plugin readme.txt
- [ ] Ẩn PHP version
- [ ] Ẩn WordPress version
- [ ] Chuyển sang server-side cron

### Trong tháng đầu 📋
- [ ] Setup Google Search Console (nếu chưa có)
- [ ] Gỡ URL spam tiếng Nhật qua URL Removal Tool
- [ ] Cài Yoast/Rank Math → tạo sitemap
- [ ] Submit sitemap mới
- [ ] Thêm meta description cho tất cả trang
- [ ] Gỡ noindex directive
- [ ] Triển khai schema (Organization, Product, Breadcrumb)
- [ ] Sửa robots.txt

### Tháng 2-3 🔄
- [ ] Tối ưu LCP mobile (ảnh, render-blocking, preload)
- [ ] Cài WP Rocket hoặc LiteSpeed Cache
- [ ] Tối ưu font loading
- [ ] Monitoring liên tục qua Wordfence + GSC

---

## 6. CÔNG CỤ KHUYẾN NGHỊ

| Mục đích | Plugin/Tool | Ghi chú |
|----------|------------|---------|
| Bảo mật | Wordfence Premium | Scan malware, firewall, 2FA |
| SEO | Rank Math hoặc Yoast SEO | Sitemap, schema, meta tags |
| Cache/Speed | LiteSpeed Cache | Server đang dùng LiteSpeed — tương thích nhất |
| Login Security | Limit Login Attempts Reloaded | Chặn brute-force |
| Login Hide | WPS Hide Login | Đổi URL wp-login |
| Backup | UpdraftPlus | Backup tự động ra cloud |
| WAF | Cloudflare (đã có) | Thêm custom WAF rules |

---

> **⚠️ LƯU Ý QUAN TRỌNG:**
> Việc dọn hack CHỈ giải quyết triệu chứng. Cần xác định **vector xâm nhập** (entry point) — có thể là plugin lỗi cũ, mật khẩu yếu, hoặc lỗ hổng theme — để ngăn tái nhiễm. Nếu không tìm được entry point, rất có khả năng website sẽ bị hack lại trong 1-2 tuần.
