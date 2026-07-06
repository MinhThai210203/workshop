---
title: "Nhật ký công việc Tuần 2"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.2. </b> "
---
### Mục tiêu tuần 2:

* Bắt đầu với Amazon VPC và AWS VPN Site-to-Site.
* Tìm hiểu về kiến trúc VPC, subnets, routing tables và security groups.
* Thiết lập kết nối bảo mật giữa on-premises và AWS cloud với VPN.
* Tìm hiểu và thực hành tạo VPC, Security Groups, VPN Connection.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu VPC (Virtual Private Cloud) cơ bản<br>- Hiểu về CIDR blocks, Subnets (Public/Private)<br>- Học về Internet Gateway và NAT Gateway<br>- Tạo VPC với kiến trúc multi-AZ | 28/04/2026 | 28/04/2026 | <https://000003.awsstudygroup.com/> |
| 3 | - Tìm hiểu Security Groups và Network ACLs<br>- Phân biệt tường lửa Stateful vs Stateless<br>- Cấu hình quy tắc inbound/outbound<br>- Thực hành tạo Security Groups cho EC2 | 29/04/2026 | 29/04/2026 | <https://000003.awsstudygroup.com/> |
| 4 | - Tìm hiểu Route Tables và định tuyến<br>- Cấu hình VPC Flow Logs<br>- Thiết lập giám sát CloudWatch cho VPC<br>- Sử dụng VPC Resource Map để trực quan hóa | 30/04/2026 | 30/04/2026 | <https://000003.awsstudygroup.com/> |
| 5 | - Tìm hiểu AWS Site-to-Site VPN<br>- Tạo Virtual Private Gateway và Customer Gateway<br>- Cấu hình VPN Connection<br>- Kiểm tra kết nối VPN | 01/05/2026 | 01/05/2026 | <https://000003.awsstudygroup.com/> |
| 6 | - Tìm hiểu AWS Transit Gateway<br>- Kết nối nhiều VPC qua Transit Gateway<br>- Cấu hình VPN với strongSwan<br>- Định tuyến lưu lượng qua Transit Gateway | 02/05/2026 | 02/05/2026 | <https://000003.awsstudygroup.com/> |

### Kết quả đạt được tuần 2:

* Hiểu kiến trúc Amazon VPC (Virtual Private Cloud) và cách cô lập tài nguyên mạng trên AWS:
  * Ký hiệu CIDR và lập kế hoạch địa chỉ IP
  * Triển khai multi-AZ cho tính khả dụng cao
  * Public Subnets với Internet Gateway (IGW) cho truy cập Internet
  * Private Subnets với NAT Gateway cho lưu lượng outbound
  * Route Tables và ưu tiên định tuyến (khớp tiền tố dài nhất)
  * VPC peering và VPC endpoints

* Nắm vững bảo mật mạng với Security Groups và Network ACLs:
  * Security Groups - tường lửa stateful ở cấp độ EC2 instance
  * Network ACLs - tường lửa stateless ở cấp độ subnet
  * Cấu hình quy tắc inbound (SSH, HTTP, HTTPS) và outbound
  * Đánh số quy tắc và thứ tự đánh giá
  * Chuỗi security group và tham chiếu
  * Quy tắc từ chối để chặn IP

* Triển khai giám sát và khắc phục sự cố VPC:
  * VPC Flow Logs để ghi lại thông tin lưu lượng IP
  * Xuất logs sang CloudWatch Logs hoặc S3
  * Tạo bảng điều khiển CloudWatch để trực quan hóa tài nguyên VPC
  * Thiết lập cảnh báo cho bất thường lưu lượng
  * Phân tích mẫu lưu lượng và khắc phục sự cố kết nối
  * Xác định mối đe dọa bảo mật và lưu lượng bất thường
  * Sử dụng VPC Resource Map để trực quan hóa

* Kết nối hạ tầng tại chỗ với AWS qua các giải pháp VPN:
  * Site-to-Site VPN với Virtual Private Gateway (VGW) và Customer Gateway (CGW)
  * Thiết lập đường hầm VPN IPsec giữa hạ tầng tại chỗ và AWS VPC
  * Định tuyến tĩnh vs Định tuyến động (BGP)
  * AWS Transit Gateway - kiến trúc hub-and-spoke cho kết nối multi-VPC
  * Transit Gateway attachments (VPC, VPN, Direct Connect)
  * Transit Gateway route tables
  * Cấu hình strongSwan VPN (IPsec mã nguồn mở) trên Linux EC2 instance
  * Giám sát và khắc phục sự cố VPN
  * Các mẫu tính khả dụng cao của VPN


