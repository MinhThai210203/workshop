---
title: "Nhật ký công việc Tuần 1"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---
### Mục tiêu tuần 1:

* Quản lý kiểm soát truy cập với AWS IAM (Identity and Access Management).
* Tìm hiểu và thực hành tạo Users, Groups, Roles và chuyển đổi Role.
* Áp dụng nguyên tắc đặc quyền tối thiểu trong mô hình bảo mật IAM.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Làm quen với các thành viên FCAJ<br>- Đọc và lưu ý các nội quy, quy định tại đơn vị thực tập<br>- Tìm hiểu AWS và các loại dịch vụ (Compute, Storage, Networking, Database) | 20/04/2026 | 20/04/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - Tạo tài khoản AWS Free Tier<br>- Hoàn thành 5 nhiệm vụ để nhận 100$ AWS Credit<br>- Thiết lập MFA (Multi-Factor Authentication)<br>- Tìm hiểu AWS Budgets để quản lý chi phí | 21/04/2026 | 21/04/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - Tìm hiểu IAM Users và Groups<br>- Tạo IAM Admin User và Admin Group<br>- Gắn policy AdministratorAccess cho Admin Group<br>- Đăng nhập bằng IAM Admin User | 22/04/2026 | 22/04/2026 | <https://000002.awsstudygroup.com/> |
| 5 | - Tìm hiểu IAM Roles và cách sử dụng<br>- Tạo IAM Role (AdminRole, S3Role)<br>- Tạo Operator User và gắn policy cho phép chuyển đổi role | 23/04/2026 | 23/04/2026 | <https://000002.awsstudygroup.com/> |
| 6 | - Thực hành chuyển đổi Role từ Operator User sang Admin Role<br>- Kiểm tra quyền truy cập S3 với S3Role<br>- Áp dụng nguyên tắc đặc quyền tối thiểu | 24/04/2026 | 24/04/2026 | <https://000002.awsstudygroup.com/> |

### Kết quả đạt được tuần 1:

* Hòa nhập thành công với nhóm First Cloud AI Journey và nắm rõ nội quy, quy định tại đơn vị thực tập.

* Hiểu AWS là gì và nắm được các nhóm dịch vụ cơ bản:
  * Compute (EC2, Lambda, ECS, EKS)
  * Storage (S3, EBS, EFS, Glacier)
  * Networking (VPC, Route53, CloudFront, Direct Connect)
  * Database (RDS, DynamoDB, Aurora, Redshift)
  * Security & Identity (IAM, KMS, WAF, Shield)

* Đã tạo và cấu hình tài khoản AWS Free Tier thành công:
  * Hoàn thành 5 nhiệm vụ để nhận 100$ AWS Credit
  * Thiết lập MFA (Multi-Factor Authentication) cho root account
  * Cấu hình AWS Budgets với ngưỡng cảnh báo chi phí

* Nắm vững quản lý truy cập với AWS IAM (Identity and Access Management):
  * Hiểu sự khác biệt giữa IAM Users (thông tin xác thực dài hạn) và IAM Roles (quyền tạm thời)
  * Tạo Admin Group với policy AdministratorAccess
  * Tạo IAM Admin User và thêm vào Admin Group
  * Tạo AdminRole với quyền quản trị đầy đủ và S3Role với quyền Read/Write S3
  * Tạo Operator User và cấu hình policy cho phép chuyển đổi role
  * Thực hành chuyển đổi Role thành công từ Operator User sang Admin Role
  * Đăng nhập AWS Console bằng IAM User thay vì root account

* Áp dụng các thực tiễn tốt nhất của IAM:
  * Nguyên tắc đặc quyền tối thiểu
  * Sử dụng Roles cho quyền truy cập tạm thời thay vì chia sẻ thông tin xác thực
  * Bật MFA cho các IAM Users quan trọng
  * Giám sát hoạt động truy cập qua AWS CloudTrail
  * Không sử dụng root account cho các tác vụ hàng ngày


