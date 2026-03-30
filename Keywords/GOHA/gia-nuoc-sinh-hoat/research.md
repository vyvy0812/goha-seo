# Semantic Analysis: Giá Nước Sinh Hoạt

## 1. Entity Interpretation

| Category | Entities | Relevance |
|:---|:---|:---|
| **Organization** | UBND cấp tỉnh, Bộ Tài chính, Sawaco (Tổng công ty Cấp nước Sài Gòn), Viwasupco (Nước sạch Sông Đà), HAWS (Hà Nội Water) | Primary |
| **Concept** | Giá bán lẻ nước sạch, bậc thang lũy tiến, định mức tiêu thụ nước, khung giá nước sạch sinh hoạt, phí dịch vụ thoát nước (TDVTN), thuế GTGT nước sạch | Primary |
| **Legal/Regulation** | Thông tư 44/2021/TT-BTC, Nghị định 177/2013/NĐ-CP, Nghị định 149/2016/NĐ-CP, QĐ 3541/QĐ-UBND Hà Nội, QĐ 25/2019/QĐ-UBND TPHCM, QĐ 17/2021/QĐ-UBND TPHCM | Primary |
| **Location** | Hà Nội, TPHCM, Đà Nẵng, đô thị đặc biệt, đô thị loại 1-5, khu vực nông thôn | Primary |
| **Metric** | đồng/m³, m³/người/tháng, m³/đồng hồ/tháng, thuế GTGT 5%, TDVTN 30% (2025), phí BVMT | Primary |
| **Person** | Chủ hộ, nhân khẩu đăng ký, hộ nghèo/cận nghèo, hộ gia đình chính sách | Secondary |
| **Time/Event** | Lộ trình tăng giá nước 2019-2022 TPHCM, điều chỉnh giá nước Hà Nội 07/2023, dự báo giá nước 2026 | Secondary |

## 2. Keyword Clusters

### Cluster A: Định nghĩa & Khái niệm
- **Intent**: Informational
- **Keywords**: giá nước, giá nước sinh hoạt, giá nước sạch, giá nước nhà nước, 1 khối nước bao nhiêu tiền, giá nước sinh hoạt là gì, giá nước máy

### Cluster B: Bảng giá theo địa phương
- **Intent**: Informational / Local
- **Keywords**: giá nước sinh hoạt tại tphcm, giá nước sạch hà nội mới nhất, giá nước sinh hoạt hà nội, bảng giá nước sinh hoạt, giá nước sinh hoạt đà nẵng, giá nước sinh hoạt 2025, giá nước sinh hoạt 2026

### Cluster C: Đối tượng sử dụng
- **Intent**: Informational / Commercial
- **Keywords**: giá nước kinh doanh, giá nước sản xuất, giá nước hành chính sự nghiệp, giá nước hộ nghèo, giá nước doanh nghiệp

### Cluster D: Cách tính & Hướng dẫn
- **Intent**: Informational (Do)
- **Keywords**: cách tính tiền nước, cách tính tiền nước sinh hoạt hàng tháng, công thức tính tiền nước, cách tính tiền nước theo bậc thang, cách đọc đồng hồ nước

### Cluster E: Pháp lý & Quy định
- **Intent**: Informational
- **Keywords**: thông tư 44/2021 giá nước, khung giá nước sạch, nguyên tắc xác định giá nước, cơ quan quyết định giá nước, quy định giá nước sinh hoạt

### Cluster F: Phí & Thuế liên quan
- **Intent**: Informational
- **Keywords**: phí dịch vụ thoát nước, thuế GTGT nước sạch, phí bảo vệ môi trường nước thải, TDVTN là gì, phí xử lý nước thải

### Cluster G: Tiết kiệm & Thực hành
- **Intent**: Informational (Do)
- **Keywords**: cách tiết kiệm nước sinh hoạt, thanh toán hóa đơn nước online, cách thanh toán tiền nước, đăng ký định mức nước

## 3. Data Points (Latest Research - 03/2026)

### Khung giá nước sạch quốc gia (TT 44/2021/TT-BTC)
| Khu vực | Giá tối thiểu | Giá tối đa |
|---------|---------------|------------|
| Đô thị đặc biệt, đô thị loại 1 | 3.500 đồng/m³ | 18.000 đồng/m³ |
| Đô thị loại 2, 3, 4, 5 | 3.000 đồng/m³ | 15.000 đồng/m³ |
| Khu vực nông thôn | 2.000 đồng/m³ | 11.000 đồng/m³ |

### Giá nước Hà Nội 2025 (QĐ 3541/QĐ-UBND)
| Bậc | Mức sử dụng | Hộ dân cư | Hộ nghèo/cận nghèo |
|-----|------------|-----------|-------------------|
| 1 | 0-10m³/tháng | 8.500 đồng/m³ | 5.973 đồng/m³ |
| 2 | 10-20m³/tháng | 9.900 đồng/m³ | - |
| 3 | 20-30m³/tháng | 16.000 đồng/m³ | - |
| 4 | Trên 30m³/tháng | 27.000 đồng/m³ | - |

Đối tượng khác tại Hà Nội:
- Cơ quan hành chính, sự nghiệp: 13.500 đồng/m³
- Đơn vị sản xuất: 16.000 đồng/m³
- Đơn vị kinh doanh dịch vụ: 29.000 đồng/m³

### Giá nước TPHCM 2025 (QĐ 25/2019/QĐ-UBND)
| Mức sử dụng | Hộ dân cư | Hộ nghèo/cận nghèo |
|-------------|-----------|-------------------|
| Dưới 4m³/người/tháng | 6.700 đồng/m³ | 6.300 đồng/m³ |
| Từ 4-6m³/người/tháng | 12.900 đồng/m³ | 12.900 đồng/m³ |
| Trên 6m³/người/tháng | 14.400 đồng/m³ | 14.400 đồng/m³ |

Đối tượng khác tại TPHCM:
- Cơ quan hành chính, sự nghiệp: 13.000 đồng/m³
- Doanh nghiệp sản xuất: 12.100 đồng/m³
- Đơn vị kinh doanh dịch vụ: 21.300 đồng/m³

### Phí bổ sung năm 2025
- Thuế GTGT: 5% trên giá bán nước
- TDVTN (TPHCM): 30% trên giá nước cấp
- Thuế GTGT trên TDVTN: 8% (01/01-30/06/2025), 10% (01/07-31/12/2025)
- Phí BVMT nước thải (Hà Nội): 10% trên giá nước

### Dự báo giá nước 2026
- TPHCM: Giá bình quân bán lẻ dự kiến 12.848 đồng/m³ (tăng ~4,1%)
- Hà Nội: Dự kiến tăng 3-5% so với 2025
- TDVTN dự kiến tiếp tục tăng 5%/năm

## 4. LSI/Semantic Keywords (Must appear in article)
- nước sạch, nước sinh hoạt, nước máy
- đồng/m³, m³/tháng, khối nước
- bậc thang lũy tiến, định mức tiêu thụ
- đồng hồ nước, chỉ số đồng hồ
- hóa đơn nước, thanh toán tiền nước
- thuế giá trị gia tăng (GTGT/VAT)
- phí thoát nước, xử lý nước thải
- UBND, Bộ Tài chính, Sở Tài chính
- đơn vị cấp nước, công ty cấp nước
- tiết kiệm nước, sử dụng nước hợp lý
- khung giá nước sạch, giá bán lẻ bình quân

## 5. Strategic Recommendations
- Bài viết PHẢI có bảng giá chi tiết cho ít nhất Hà Nội và TPHCM (2 thị trường lớn nhất)
- Cần có ít nhất 2 ví dụ tính tiền nước cụ thể (1 cho Hà Nội, 1 cho TPHCM)
- Dẫn nguồn pháp lý cụ thể: Thông tư 44/2021, QĐ 3541, QĐ 25/2019
- Phân biệt rõ: giá nước chưa VAT vs. tổng thanh toán (bao gồm VAT + TDVTN)
- Cập nhật dự báo giá nước 2026 để đảm bảo freshness
- Kết nối GOHA qua góc độ tài chính cá nhân / quản lý chi phí doanh nghiệp
