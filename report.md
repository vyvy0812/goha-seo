# WordPress Security Audit: zamst.vn
Date: 2026-03-19

## Executive Summary
- **Risk Level: HIGH**
- Total findings: 14 (2 critical, 4 high, 5 medium, 3 low)
- WordPress: 6.9.4 (latest)
- Theme: Flatsome 3.20.1
- Plugins detected: 3 (contact-form-7, woocommerce, gtranslate)

---

## Findings by Severity

### CRITICAL

#### 1. XML-RPC Fully Exposed with All Methods
- **Path:** `/xmlrpc.php`
- **Evidence:** Returns 80+ methods including `system.multicall`, `wp.getUsersBlogs`, `pingback.ping`
- **Risk:** Enables credential brute-force (amplified via `system.multicall` — hundreds of login attempts per single HTTP request), DDoS amplification via `pingback.ping`, SSRF attacks
- **Remediation:** Block xmlrpc.php entirely unless needed for Jetpack/mobile apps. Add to .htaccess or server config:
  ```
  <Files xmlrpc.php>
    Require all denied
  </Files>
  ```
  Or use Cloudflare WAF rule to block POST to `/xmlrpc.php`

#### 2. wp-admin/install.php Returns 200
- **Path:** `/wp-admin/install.php`
- **Evidence:** HTTP 200 response instead of redirect to login or 403
- **Risk:** If database connection is ever lost or reset, this page could allow an attacker to re-initialize WordPress and gain full admin access
- **Remediation:** Block access via server config or add redirect rule. Restrict to known IPs.

---

### HIGH

#### 3. No HSTS (Strict-Transport-Security) Header
- **Evidence:** Header absent from response. HTTP→HTTPS redirect exists (301) but without HSTS, first visit is vulnerable to SSL stripping (MITM)
- **Risk:** Man-in-the-middle attack on first connection, session hijacking
- **Remediation:** Add header: `Strict-Transport-Security: max-age=31536000; includeSubDomains`

#### 4. readme.html Exposed
- **Path:** `/readme.html`
- **Evidence:** Returns default WordPress readme (200 OK)
- **Risk:** Confirms WordPress installation, provides system requirements info. Combined with version disclosure, helps attackers target specific exploits.
- **Remediation:** Delete or block access to `readme.html`

#### 5. wp-links-opml.php Exposed
- **Path:** `/wp-links-opml.php`
- **Evidence:** Returns 200 with OPML XML containing site title
- **Risk:** Information disclosure, confirms WordPress
- **Remediation:** Block access or delete file

#### 6. Login Page Exposed Without CAPTCHA
- **Path:** `/wp-login.php`
- **Evidence:** Standard WordPress login form, no CAPTCHA, no rate limiting visible
- **Risk:** Combined with active xmlrpc.php, the login is attackable from two vectors. Even with xmlrpc blocked, login page without CAPTCHA is brute-forceable.
- **Remediation:** Add reCAPTCHA or Turnstile, limit login attempts (Limit Login Attempts Reloaded plugin), consider hiding login URL (WPS Hide Login)

---

### MEDIUM

#### 7. No X-Frame-Options Header
- **Evidence:** Header absent
- **Risk:** Site can be embedded in iframes on malicious sites → clickjacking attacks
- **Remediation:** Add `X-Frame-Options: SAMEORIGIN` header

#### 8. No Content-Security-Policy Header
- **Evidence:** Only `upgrade-insecure-requests` directive present (set by Cloudflare), no full CSP
- **Risk:** No protection against XSS, no control over resource loading origins
- **Remediation:** Implement CSP starting with report-only mode

#### 9. No Permissions-Policy Header
- **Evidence:** Header absent
- **Risk:** Browser features (camera, microphone, geolocation) not explicitly restricted
- **Remediation:** Add `Permissions-Policy: camera=(), microphone=(), geolocation=()`

#### 10. No Referrer-Policy Header
- **Evidence:** Header absent
- **Risk:** Full URL with query params leaked to external sites via Referer header
- **Remediation:** Add `Referrer-Policy: strict-origin-when-cross-origin`

#### 11. WordPress Version Disclosed (Multiple Vectors)
- **Evidence:** Version 6.9.4 exposed via RSS feed generator tag, `?ver=` params on assets, wp-emoji-release
- **Risk:** Attackers can target version-specific vulnerabilities. Currently on latest (6.9.4), but becomes a risk when updates are delayed.
- **Remediation:** Remove generator meta tag (add to theme's functions.php):
  ```php
  remove_action('wp_head', 'wp_generator');
  ```

---

### LOW

#### 12. PHP Version Disclosed
- **Evidence:** `X-Powered-By: PHP/8.2.29` header
- **Risk:** Minor info disclosure, helps attackers fingerprint stack
- **Remediation:** Disable in php.ini: `expose_php = Off`

#### 13. wp-cron.php Publicly Accessible
- **Evidence:** Returns 200 (empty body — normal behavior)
- **Risk:** Can be used for DoS by flooding wp-cron with requests, forcing WordPress to process scheduled tasks
- **Remediation:** Disable public wp-cron, use server-side cron instead:
  ```php
  define('DISABLE_WP_CRON', true);
  ```
  Then add server cron: `*/15 * * * * curl https://zamst.vn/wp-cron.php`

#### 14. Plugin readme.txt Files Exposed
- **Evidence:** contact-form-7 (v6.1.4), woocommerce (v10.4.4), gtranslate (v3.0.9) — all readme.txt accessible with version numbers
- **Risk:** Reveals exact plugin versions for targeted exploit lookup
- **Remediation:** Block access to readme.txt in plugins directory

---

## What's Good (Defenses Detected)

| Check | Status |
|-------|--------|
| HTTPS | ✅ Active, HTTP→HTTPS 301 redirect |
| REST API Users | ✅ Blocked (401 Unauthorized) |
| Author Enumeration | ✅ Returns 404 for `/?author=N` |
| X-Content-Type-Options | ✅ Check via Cloudflare |
| .env file | ✅ Not found (404) |
| .git directory | ✅ Blocked (403) |
| wp-config backups | ✅ Blocked (403) |
| debug.log | ✅ Blocked (403) |
| Directory listing (uploads) | ✅ Blocked (403) |
| CDN/WAF | ✅ Cloudflare active |
| Mixed content | ✅ None detected |
| WordPress version | ✅ Latest (6.9.4) |
| SSL Certificate | ✅ Valid (expires May 15, 2026) |

---

## Technology Stack

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
| SSL Expiry | May 15, 2026 |

---

## Recommendations (Priority Order)

### Immediate (This Week)
1. **Block xmlrpc.php** — Highest risk. Use Cloudflare WAF rule or .htaccess. This single change eliminates brute-force amplification and DDoS vectors.
2. **Block install.php** — Prevent potential site takeover on DB failure.
3. **Add CAPTCHA to login** — Use Cloudflare Turnstile (free) on wp-login.php.

### Short-term (This Month)
4. **Add HSTS header** — Enable via Cloudflare SSL/TLS settings → Edge Certificates → HSTS.
5. **Add security headers** — X-Frame-Options, Referrer-Policy, Permissions-Policy. All configurable in Cloudflare or .htaccess.
6. **Delete readme.html** from WordPress root.
7. **Block plugin readme.txt** access via server config.

### Ongoing
8. **Hide PHP version** — `expose_php = Off` in Hostinger PHP settings.
9. **Remove WP version from source** — functions.php filter.
10. **Switch to server cron** — Disable public wp-cron.php.
11. **Monitor for plugin updates** — Contact Form 7, WooCommerce, GTranslate.
12. **SSL renewal** — Certificate expires May 15, 2026 (57 days). Ensure auto-renewal is configured.

---

## Scan Metadata
- Scan date: 2026-03-19 03:25 UTC
- Target: https://zamst.vn/
- Total requests: ~25
- Scanner: WP Security Audit (External) — Claude Code skill
- Checks: version detection, theme/plugin enumeration, security headers, attack surface probes, SSL/TLS, XML-RPC, user enumeration, directory listing, sensitive file exposure
