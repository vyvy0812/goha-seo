$c = Get-Content "d:\goha-seo\Keywords\Home Credit\the-tin-dung-co-chuyen-khoan-duoc-khong\article.md" -Raw -Encoding UTF8
$words = ($c -split '\s+' | Where-Object { $_ -ne '' }).Count
Write-Host "Total words: $words"

$kwCount = ([regex]::Matches($c, [regex]::Escape('thẻ tín dụng có chuyển khoản được không'))).Count
Write-Host "KW main count: $kwCount"

$kwLen = 8
$density = [math]::Round(($kwCount * $kwLen / $words) * 100, 2)
Write-Host "KW density: $density %"

$linkCount = ([regex]::Matches($c, 'homecredit\.vn')).Count
Write-Host "Internal links: $linkCount"

$linkDensity = [math]::Round(($linkCount / $words) * 100, 2)
Write-Host "Link density: $linkDensity %"

# Check secondary keywords
$secondary = @(
    "có chuyển khoản từ thẻ tín dụng được không",
    "thẻ tín dụng có thể chuyển khoản được không",
    "tiền trong thẻ tín dụng có chuyển khoản được không",
    "dùng thẻ tín dụng có chuyển khoản được không",
    "mở thẻ tín dụng có chuyển khoản được không",
    "làm thẻ tín dụng có chuyển khoản được không",
    "sử dụng thẻ tín dụng có chuyển khoản được không",
    "tiền ở thẻ tín dụng có chuyển khoản được không",
    "tài khoản thẻ tín dụng có chuyển khoản được không",
    "xài thẻ tín dụng có chuyển khoản được không"
)

Write-Host "`nSecondary KW check:"
foreach ($kw in $secondary) {
    $count = ([regex]::Matches($c, [regex]::Escape($kw))).Count
    $status = if ($count -ge 1) { "OK" } else { "MISSING" }
    Write-Host "  [$status] ($count) $kw"
}
