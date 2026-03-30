# Semantic Analysis: Dịch vụ bảo trì máy băm nhựa

## 1. Entity Interpretation

| Category | Entities | Relevance |
|:---|:---|:---|
| **Organization** | Trung Nguyên TNT, Cơ Khí Thành Tài, Carno Vietnam, Máy Nhựa Việt Đài, An Hoàng Minh, Hikari VN | Primary |
| **Concept** | Bảo trì phòng ngừa (Preventive Maintenance), Bảo trì khắc phục (Corrective Maintenance), Bảo dưỡng định kỳ (Scheduled Maintenance), Downtime, ROI bảo trì | Primary |
| **Machine/Equipment** | Máy băm nhựa (Plastic Granulator/Crusher), Máy nghiền nhựa (Plastic Grinder), Máy băm 1 trục, Máy băm 2 trục, Máy nghiền chậm (Low-speed Grinder) | Primary |
| **Component** | Dao băm/dao nghiền (Cutting Blades), Dao tĩnh (Fixed Blade), Dao động (Rotating Blade), Lưới sàng (Screen Mesh), Ổ bi (Bearings), Dây đai/dây curoa (Drive Belt), Trục băm (Rotor Shaft), Buồng băm (Crushing Chamber), Phễu nạp liệu (Hopper) | Primary |
| **Material** | Thép SKD11, Thép SKH51 (HSS), Hợp kim 9CrSi, Thép không gỉ (lưới sàng) | Secondary |
| **Specification** | Khe hở dao: 0.8mm (>20HP) / 0.5mm (<20HP), Tốc độ quay: 400-600 vòng/phút (1 trục), Áp suất thủy lực: 20-25MPa | Primary |
| **Service** | Mài dao, thay dao, thay lưới sàng, căn chỉnh khe hở, tra dầu mỡ, kiểm tra hệ thống điện, nối đất | Primary |
| **Location** | TP.HCM, Hải Dương (chi nhánh TNT), miền Nam – miền Bắc | Secondary |

## 2. Secondary Keywords (User-Provided - BẮT BUỘC sử dụng)

| # | Keyword phụ | Intent | Ghi chú |
|---|---|---|---|
| 1 | bảo trì máy nghiền nhựa | Commercial + Info | Synonym "nghiền" = "băm" |
| 2 | bảo dưỡng máy băm nhựa | Informational | Focus quy trình |
| 3 | bảo dưỡng máy nghiền nhựa | Informational | Synonym variation |
| 4 | sửa máy băm nhựa | Transactional | Urgent repair |
| 5 | sửa chữa máy băm nhựa | Transactional | Formal variation |
| 6 | dịch vụ sửa máy băm nhựa | Commercial | Service-seeking |
| 7 | sửa máy nghiền nhựa | Transactional | Synonym variation |
| 8 | sửa chữa máy nghiền nhựa | Transactional | Synonym variation |
| 9 | dịch vụ sửa máy nghiền nhựa | Commercial | Service-seeking |

## 3. LSI/Semantic Keywords (Bổ sung)

| Cluster | Keywords |
|---|---|
| **Bộ phận máy** | dao băm nhựa, dao nghiền nhựa, dao tĩnh, dao động, lưới sàng máy băm, ổ bi máy nghiền, dây curoa máy băm, trục băm, buồng băm |
| **Hành động bảo trì** | mài dao máy băm nhựa, thay dao máy nghiền, căn chỉnh khe hở dao, tra dầu mỡ ổ bi, kiểm tra dây đai, vệ sinh buồng băm, thay lưới sàng |
| **Lỗi/Sự cố** | máy băm nhựa bị kẹt, máy nghiền nhựa rung lắc, tiếng ồn bất thường, dao mòn, lưới sàng tắc, motor quá nhiệt, hạt nhựa không đều |
| **Chi phí & Hiệu quả** | chi phí bảo trì máy băm nhựa, giảm downtime, tăng tuổi thọ máy, tiết kiệm chi phí sửa chữa, hiệu suất nghiền |
| **Tái chế nhựa** | tái chế nhựa phế liệu, nhựa PP, nhựa PE, nhựa PET, nhựa PVC, hạt nhựa tái sinh |

## 4. Keyword Clusters

### Cluster A: Hướng dẫn bảo trì & bảo dưỡng (Informational)
- **Intent**: Know — Quy trình, checklist, hướng dẫn kỹ thuật
- **Keywords**: bảo dưỡng máy băm nhựa, bảo dưỡng máy nghiền nhựa, cách bảo trì máy băm nhựa, quy trình bảo dưỡng máy nghiền, checklist bảo trì máy băm, hướng dẫn vệ sinh máy nghiền nhựa
- **Content**: Bài viết dạng hướng dẫn toàn diện với checklist theo tần suất

### Cluster B: Dịch vụ sửa chữa (Commercial/Transactional)
- **Intent**: Do — Tìm đơn vị sửa chữa uy tín
- **Keywords**: sửa máy băm nhựa, sửa chữa máy băm nhựa, dịch vụ sửa máy băm nhựa, sửa máy nghiền nhựa, sửa chữa máy nghiền nhựa, dịch vụ sửa máy nghiền nhựa
- **Content**: Giới thiệu dịch vụ + quy trình tiếp nhận + cam kết thời gian xử lý

### Cluster C: Bảo trì dịch vụ định kỳ (Commercial)
- **Intent**: Do — Đặt lịch bảo trì chuyên nghiệp
- **Keywords**: dịch vụ bảo trì máy băm nhựa, bảo trì máy nghiền nhựa, bảo trì định kỳ máy nghiền, hợp đồng bảo trì máy ngành nhựa
- **Content**: Service page + pricing model + case study

### Cluster D: Linh kiện & thay thế (Transactional)
- **Intent**: Do — Mua linh kiện
- **Keywords**: dao băm nhựa, lưới sàng máy băm, ổ bi máy nghiền, dây curoa máy băm, linh kiện máy băm nhựa
- **Content**: Bảng giá + thông số + tư vấn chọn linh kiện phù hợp

## 5. Technical Data (Specs từ Research)

### Thông số khe hở dao tiêu chuẩn
| Công suất máy | Khe hở dao động – dao tĩnh | Ghi chú |
|---|---|---|
| > 20 HP | 0.8 mm | Điều chỉnh khi thay dao mới |
| ≤ 20 HP | 0.5 mm | Tăng nhẹ nếu vật liệu mỏng |

### Vật liệu dao băm phổ biến
| Mã thép | Ứng dụng | Đặc tính |
|---|---|---|
| SKD11 | Dao băm nhựa cứng (PP, PE, ABS) | Độ bền mài mòn cao, chống va đập |
| SKH51 (HSS) | Dao nghiền tốc độ cao | Chịu nhiệt, giữ độ sắc lâu |
| 9CrSi | Dao dạng phiến (blade) | Tinh luyện sâu, giá thành hợp lý |

### Chu kỳ bảo dưỡng khuyến nghị
| Tần suất | Hạng mục |
|---|---|
| Hằng ngày | Vệ sinh buồng băm, kiểm tra lưới sàng, nghe tiếng máy bất thường |
| Hằng tuần | Siết bu lông dao, kiểm tra đầu nối điện, vệ sinh hệ thống lọc bụi |
| 3 tháng | Bôi trơn ổ bi, kiểm tra dây đai, kiểm tra khe hở dao |
| 6 tháng | Mài/thay dao, thay lưới sàng, kiểm tra motor & hệ thống điện tổng thể |
| 12 tháng | Đại tu tổng thể: thay dây đai, thay ổ bi, kiểm tra trục băm, sơn chống gỉ |

## 6. Trung Nguyên TNT Brand Alignment

### Dịch vụ TNT liên quan
- **Bảo dưỡng chủ động**: Chính sách bảo dưỡng định kỳ miễn phí **3 – 6 – 9 – 12 tháng** trong năm đầu tiên
- **Same-day support**: Cam kết xử lý sự cố trong ngày
- **2 chi nhánh**: TP.HCM (Nam) và Hải Dương (Bắc), đội ngũ kỹ thuật hỗ trợ trực tiếp
- **Hỗ trợ kỹ thuật trọn đời** cho các dòng máy cung cấp
- **Tồn kho linh kiện chiến lược**: Luôn sẵn linh kiện để giao nhanh toàn quốc
- **Video YouTube**: "Sửa Máy Băm Liệu Siêu To Khổng Lồ cho khách hàng" (02/2026) — bằng chứng thực tế

### Sản phẩm TNT liên quan
- **Hệ thống băm & nghiền (Granulators/Crushers)**: Máy băm dạng dao phiến, máy nghiền chậm
- **Linh kiện & Vật tư**: Cung cấp đầy đủ linh kiện thay thế
- **Di sản kỹ thuật Đài Loan**: Tư duy kỹ thuật chuẩn, quy trình bài bản

## 7. Semantic Constraints

- ❌ KHÔNG nhắc đến "Máy chấm keo PVC" (ngoài phạm vi bài này)
- ❌ KHÔNG sử dụng ngôn ngữ marketing hoa mỹ — giọng văn kỹ sư thực tế
- ✅ BẮT BUỘC sử dụng đầy đủ 9 keyword phụ do user cung cấp
- ✅ BẮT BUỘC phân biệt rõ: bảo trì (maintenance) vs bảo dưỡng (servicing) vs sửa chữa (repair)
- ✅ Ưu tiên thuật ngữ: "máy băm nhựa" và "máy nghiền nhựa" sử dụng xen kẽ tự nhiên
- ✅ Đơn vị kỹ thuật: HP, kW, mm, vòng/phút, MPa — in đậm
