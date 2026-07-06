---
title: "Nhật ký công việc Tuần 3"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.3. </b> "
---
### Mục tiêu tuần 3:

* Giới thiệu về Amazon EC2 và các khái niệm cơ bản.
* Tìm hiểu về các loại instance, AMI, EBS volumes và Elastic IP.
* Thực hành khởi chạy, kết nối và quản lý các EC2 instances.
* Tìm hiểu và thực hành triển khai ứng dụng Node.js trên EC2.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu các khái niệm cơ bản Amazon EC2<br>- Các loại Instance Types (T2, T3, M5, C5...)<br>- AMI (Amazon Machine Images)<br>- EBS volumes và các tùy chọn lưu trữ | 05/05/2026 | 05/05/2026 | <https://000004.awsstudygroup.com/> |
| 3 | - Tạo Linux EC2 instance (Amazon Linux 2023)<br>- Kết nối SSH với key pair<br>- Cấu hình Security Groups<br>- Cài đặt và cấu hình Node.js trên Linux | 05/06/2026 | 05/06/2026 | <https://000004.awsstudygroup.com/> |
| 4 | - Triển khai ứng dụng Node.js trên Linux<br>- Cài đặt cơ sở dữ liệu MySQL<br>- Thiết lập PM2 cho quản lý tiến trình<br>- Cấu hình Nginx làm reverse proxy | 05/07/2026 | 05/07/2026 | <https://000004.awsstudygroup.com/> |
| 5 | - Tạo Windows Server 2025 EC2 instance<br>- Kết nối RDP (Remote Desktop)<br>- Cài đặt Git, VS Code, Node.js trên Windows<br>- Cấu hình Windows Firewall | 05/08/2026 | 05/08/2026 | <https://000004.awsstudygroup.com/> |
| 6 | - Triển khai ứng dụng Node.js trên Windows<br>- Cài đặt MySQL trên Windows Server<br>- Kiểm tra các thao tác CRUD<br>- So sánh triển khai Linux vs Windows | 05/09/2026 | 05/09/2026 | <https://000004.awsstudygroup.com/> |

### Kết quả đạt được tuần 3:

* Hiểu các khái niệm cơ bản Amazon EC2 và các loại instance types:
  * General Purpose (T2, T3, M5) - cân bằng tính toán, bộ nhớ, mạng
  * Compute Optimized (C5, C6) - bộ xử lý hiệu suất cao
  * Memory Optimized (R5, X1) - hiệu suất nhanh cho tập dữ liệu lớn
  * Storage Optimized (I3, D2) - I/O tuần tự cao

* Nắm được các mô hình định giá EC2 để tối ưu chi phí:
  * On-Demand - trả theo giờ/giây, không cam kết
  * Reserved Instances - cam kết 1 hoặc 3 năm, giảm giá tới 75%
  * Spot Instances - giảm giá tới 90%, có thể bị gián đoạn
  * Savings Plans - mô hình định giá linh hoạt

* Thành thạo AMI (Amazon Machine Images):
  * Mẫu instance được cấu hình sẵn
  * Tạo AMI tùy chỉnh để tái sử dụng
  * Chia sẻ AMI và marketplace
  * Quản lý vòng đời AMI

* Triển khai thành công ứng dụng Node.js trên Linux EC2:
  * Khởi chạy Amazon Linux 2023 instance
  * Cấu hình Security Groups (cổng SSH 22, HTTP 80, cổng ứng dụng tùy chỉnh)
  * Kết nối qua SSH sử dụng key pair PEM
  * Thiết lập Elastic IP cho IP công khai tĩnh
  * Cài đặt Node.js, npm, và Git
  * Sao chép ứng dụng AWS FCJ User Management (Node.js + Express)
  * Cấu hình kết nối cơ sở dữ liệu MySQL
  * Thiết lập Express-Handlebars cho templating
  * Thực hiện các thao tác CRUD (tạo, đọc, cập nhật, xóa người dùng)
  * Cài đặt PM2 cho quản lý tiến trình và tự động khởi động lại
  * Cấu hình PM2 startup script cho system boot
  * Thiết lập Nginx làm reverse proxy
  * Thực hiện logging và giám sát

* Triển khai thành công ứng dụng Node.js trên Windows EC2:
  * Khởi chạy Windows Server 2025 instance
  * Kết nối qua RDP (Remote Desktop Protocol)
  * Cấu hình Windows Firewall rules và Security Groups cho cổng RDP 3389
  * Cài đặt Git for Windows, Visual Studio Code, Node.js runtime
  * Cấu hình biến môi trường PATH
  * Sao chép kho lưu trữ ứng dụng và cài đặt các gói npm
  * Cấu hình cơ sở dữ liệu MySQL trên Windows
  * Triển khai ứng dụng Node.js với PM2-Windows hoặc node-windows
  * Kiểm tra chức năng ứng dụng

* So sánh triển khai Linux vs Windows:
  * Linux: Nhẹ, hiệu suất tốt hơn, chi phí thấp hơn, phù hợp cho khối công việc sản xuất
  * Windows: Giao diện quen thuộc, tích hợp .NET, công cụ doanh nghiệp
  * Cả hai: Hỗ trợ Node.js đầy đủ, sẵn sàng cho sản xuất
  * Thực tiễn tốt nhất: Chọn dựa trên chuyên môn nhóm và yêu cầu khối công việc


