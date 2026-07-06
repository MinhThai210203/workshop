---
title: "Nhật ký công việc Tuần 5"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.5. </b> "
---
### Mục tiêu tuần 5:

* Nghiên cứu và thành thạo AWS Command Line Interface (AWS CLI).
* Triển khai AWS IAM Identity Center để quản lý danh tính tập trung.
* Cấu hình AWS Backup để tự động sao lưu và chiến lược khôi phục thảm họa.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Nghiên cứu các khái niệm cơ bản AWS CLI<br>- Cài đặt và cấu hình AWS CLI<br>- Kiểm tra tài nguyên với CLI<br>- Sử dụng CLI với S3, SNS, IAM, VPC, EC2 | 18/05/2026 | 18/05/2026 | <https://000011.awsstudygroup.com/> |
| 3 | - Khắc phục các lỗi và khắc phục sự cố CLI<br>- Thực tiễn tốt nhất cho AWS CLI<br>- CLI profiles và quản lý thông tin xác thực<br>- Tự động hóa scripts với AWS CLI | 19/05/2026 | 19/05/2026 | <https://000011.awsstudygroup.com/> |
| 4 | - Thực hành sử dụng AWS IAM Identity Center<br>- Quản lý định danh mạnh mẽ chuẩn bị AWS Account trong Organizations<br>- Khám phá tính năng IAM Identity Center<br>- Tạo users và groups trong Identity Center | 20/05/2026 | 20/05/2026 | <https://000012.awsstudygroup.com/> |
| 5 | - Tạo và cung cấp Permission Sets<br>- Truy cập và sử dụng kiểm soát truy cập theo thời gian<br>- Customer Managed Policies<br>- IAM Identity Center Identity Store APIs | 21/05/2026 | 21/05/2026 | <https://000012.awsstudygroup.com/> |
| 6 | - Học tập và triển khai AWS Backup<br>- Tạo S3 Bucket và kế hoạch Backup<br>- Triển khai hạ tầng cho thiết lập thông báo<br>- Kiểm tra hoạt động<br>- Xuất EC2 instance và on-premises VM vào AWS | 22/05/2026 | 22/05/2026 | <https://000013.awsstudygroup.com/> |

### Kết quả đạt được tuần 5:

* Thành thạo AWS Command Line Interface (AWS CLI):
  * Cài đặt AWS CLI version 2
  * Configure credentials với aws configure
  * AWS CLI profiles cho multiple accounts
  * Output formats (JSON, text, table, YAML)
  * Tạo và quản lý IAM Groups, Users
  * Generate Access Keys
  * Attach policies cho users/groups
  * List và describe IAM resources
  * S3: Create buckets, upload/download files, sync folders
  * SNS: Create topics, subscriptions, publish messages
  * VPC: Describe VPCs, subnets, security groups
  * EC2: Launch instances, stop/start, describe instances, create key pairs
  * Query filters với --query parameter (JMESPath)
  * Pagination với --max-items và --page-size
  * Bash scripting cho automation
  * Error handling và troubleshooting

* Triển khai AWS IAM Identity Center cho multi-account management:
  * Enable IAM Identity Center trong AWS Organizations
  * Configure Identity source (Identity Center directory hoặc external IdP)
  * Multi-account access management
  * Centralized user và group management
  * Tạo users trong Identity Center directory
  * Organize users into groups
  * User attributes và profile information
  * Password policies và MFA enforcement
  * Tạo permission sets với AWS managed policies
  * Custom permission sets với inline policies
  * Session duration configuration
  * Permission set assignments cho accounts
  * Time-based access control với session limits
  * Customer Managed Policies integration
  * Identity Store APIs cho programmatic access
  * AWS CLI configuration với SSO
  * Federated access từ corporate directory
  * Principle of least privilege
  * Regular access reviews
  * Audit logging với CloudTrail
  * Attribute-based access control (ABAC)

* Deploy AWS Backup solution cho disaster recovery:
  * Backup cho S3 buckets
  * EC2 instance backups
  * RDS database snapshots
  * Cross-region backup copies
  * Tạo backup plans với schedules
  * Retention policies
  * Lifecycle rules
  * Backup vault configuration
  * SNS topics cho backup notifications
  * CloudWatch Events cho monitoring
  * IAM roles cho AWS Backup service
  * Export EC2 instances as OVA/VHD
  * Import on-premises VMs vào AWS
  * VMware integration
  * Tạo instance trên môi trường ảo hóa on-premises với Ubuntu cho VMware
  * Backup testing và restore procedures


