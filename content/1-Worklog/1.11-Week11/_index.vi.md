---
title: "Nhật ký công việc Tuần 11"
date: 2024-01-01
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---
### Mục tiêu tuần 11:

* Giới hạn quyền người dùng với IAM Permission Boundary để phòng chống privilege escalation.
* Quản lý patches và chạy commands trên nhiều EC2 instances với AWS Systems Manager.
* Centralized management và automation cho server fleet operations.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Nghiên cứu IAM Permission Boundary concepts<br>- Hiểu về effective permissions calculation<br>- Tìm hiểu privilege escalation vulnerabilities<br>- Thiết kế Permission Boundary policy cho EC2 admin | 29/06/2026 | 29/06/2026 | <https://000030.awsstudygroup.com/> |
| 3 | - Tạo IAM Permission Boundary policy<br>- Tạo IAM User với AdministratorAccess policy<br>- Apply Permission Boundary vào IAM User<br>- Verify effective permissions | 30/06/2026 | 30/06/2026 | <https://000030.awsstudygroup.com/> |
| 4 | - Test IAM User với Permission Boundary<br>- Verify EC2 operations allowed<br>- Verify other services denied<br>- Test privilege escalation scenarios<br>- Document findings và best practices | 01/07/2026 | 01/07/2026 | <https://000030.awsstudygroup.com/> |
| 5 | - Nghiên cứu AWS Systems Manager architecture<br>- Tìm hiểu Session Manager, Patch Manager, Run Command<br>- Tạo IAM Role cho Systems Manager<br>- Launch EC2 instances và attach IAM Role<br>- Configure Patch Manager với Maintenance Window | 02/07/2026 | 02/07/2026 | <https://000031.awsstudygroup.com/> |
| 6 | - Configure Run Command để execute scripts<br>- Install CloudWatch Agent trên multiple instances<br>- Run Patch Manager scan và update<br>- Test Session Manager connections<br>- Monitor operations trong Systems Manager console | 03/07/2026 | 03/07/2026 | <https://000031.awsstudygroup.com/> |

### Kết quả đạt được tuần 11:

* Thành thạo IAM Permission Boundary:
  * Hiểu rõ IAM Permission Boundary là tính năng nâng cao giới hạn quyền tối đa
  * Quyền thực tế = Identity-based policy ∩ Permission Boundary
  * Trường hợp sử dụng: Ngăn chặn leo thang đặc quyền khi người dùng tạo IAM entities mới
  * Tạo Permission Boundary policy giới hạn quyền chỉ với dịch vụ EC2
  * Tạo IAM User `EC2Admin` với AdministratorAccess nhưng áp dụng Permission Boundary
  * Kiểm tra thành công: User chỉ có quyền trên EC2, không thể truy cập S3, RDS, Lambda
  * Không thể tạo IAM users mới hoặc sửa đổi quyền (ngăn chặn leo thang đặc quyền)
  * Đơn giản hóa quản lý quyền cho nhiều người dùng với vai trò thay đổi

* Thành thạo AWS Systems Manager:
  * Hiểu các tính năng: Session Manager, Patch Manager, Run Command, Fleet Manager
  * Tạo IAM Role `SSMInstanceRole` và khởi chạy 3 EC2 instances (Amazon Linux 2)
  * Cấu hình Patch Manager với Maintenance Window (Chủ nhật hàng tuần, 2:00 AM)
  * Chạy Patch Manager scan: phát hiện thiếu 15 security patches
  * Cài đặt patch thành công: 100% instances tuân thủ
  * Cấu hình Run Command: Cài đặt CloudWatch Agent và thực thi scripts tùy chỉnh
  * Kiểm tra Session Manager: Kết nối không cần SSH keys hoặc bastion hosts
  * Thời gian vận hành giảm 80%, bảo mật cải thiện với đầy đủ audit trail

