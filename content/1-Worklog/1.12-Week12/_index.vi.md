---
title: "Nhật ký công việc Tuần 12"
date: 2024-01-01
weight: 12
chapter: false
pre: " <b> 1.12. </b> "
---
### Mục tiêu tuần 12:

* Lựa chọn kích thước EC2 phù hợp với CloudWatch Agent và AWS Compute Optimizer.
* Mã hóa dữ liệu lưu trữ (encryption at rest) với AWS KMS và S3.
* Thiết lập audit logging với CloudTrail và query với Athena.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Nghiên cứu CloudWatch và CloudWatch Agent<br>- Tìm hiểu EC2 Right Sizing và cost optimization<br>- Tạo IAM Role cho CloudWatch Agent<br>- Launch EC2 instance để test monitoring | 06/07/2026 | 06/07/2026 | <https://000032.awsstudygroup.com/> |
| 3 | - Install CloudWatch Agent trên EC2 instance<br>- Configure memory và disk metrics collection<br>- Generate workload để collect data<br>- Verify metrics trong CloudWatch console | 07/07/2026 | 07/07/2026 | <https://000032.awsstudygroup.com/> |
| 4 | - Analyze CloudWatch metrics data<br>- Enable AWS Compute Optimizer<br>- Review right-sizing recommendations<br>- Apply best practices cho EC2 sizing | 08/07/2026 | 08/07/2026 | <https://000032.awsstudygroup.com/> |
| 5 | - Nghiên cứu AWS KMS và encryption concepts<br>- Tạo IAM Users cho testing<br>- Tạo Customer Managed Key (CMK)<br>- Configure key policies và permissions<br>- Create S3 bucket với KMS encryption | 09/07/2026 | 09/07/2026 | <https://000033.awsstudygroup.com/> |
| 6 | - Enable CloudTrail logging cho KMS operations<br>- Setup Amazon Athena cho log queries<br>- Test encryption và decryption operations<br>- Query audit logs với Athena<br>- Hoàn thành và tổng kết chương trình | 10/07/2026 | 10/07/2026 | <https://000033.awsstudygroup.com/> |

### Kết quả đạt được tuần 12:

* Thành thạo Amazon CloudWatch và EC2 Right Sizing:
  * Hiểu kiến trúc CloudWatch: Basic monitoring so với Detailed monitoring
  * CloudWatch Agent bắt buộc để thu thập memory và disk utilization metrics
  * Tạo IAM Role `CloudWatchAgentRole` và khởi chạy EC2 instance t3.large để kiểm tra
  * Cài đặt CloudWatch Agent, cấu hình metrics: `mem_used_percent`, `disk_used_percent`
  * Tạo test workload với công cụ stress: CPU tăng 15% → 85%, Memory tăng 35% → 60%
  * Tạo CloudWatch Dashboard để trực quan hóa metrics theo thời gian thực

* Phân tích và tối ưu chi phí với AWS Compute Optimizer:
  * Bật AWS Compute Optimizer (dịch vụ miễn phí)
  * Phân tích instance: t3.large với CPU trung bình 15%, Memory trung bình 35%
  * Instance được đề xuất: t3.medium - Tiết kiệm chi phí: 50% (~$30/tháng mỗi instance)
  * Hiện tại: $0.0832/giờ, Đề xuất: $0.0416/giờ
  * Thực tiễn tốt nhất cho right-sizing: Bắt đầu nhỏ, giám sát liên tục, xem xét hàng quý

* Thành thạo AWS Key Management Service (KMS):
  * Hiểu các khái niệm cơ bản KMS: Customer Master Keys (CMK), encryption at rest
  * Giá: $1/tháng mỗi CMK + $0.03 cho mỗi 10,000 requests
  * Tạo IAM Users: `UserA` (chủ sở hữu), `UserB` (người nhận), `UserC` (không có quyền)
  * Tạo Customer Managed Key với symmetric encryption, bật automatic rotation
  * Tạo S3 bucket với KMS encryption (SSE-KMS với custom CMK)
  * Bật Bucket Key để giảm KMS API calls (tối ưu chi phí)

* Triển khai audit logging và tuân thủ:
  * Tạo CloudTrail trail để ghi lại KMS API calls và S3 data events
  * Thiết lập Amazon Athena với cơ sở dữ liệu `cloudtrail_logs`
  * Kiểm tra quy trình mã hóa: UserA upload → tự động mã hóa, UserA và UserB download thành công
  * UserC thử download: Truy cập bị từ chối (kiểm soát truy cập hoạt động đúng)
  * Truy vấn audit logs với Athena SQL: theo dõi các hoạt động Encrypt, Decrypt, GenerateDataKey
  * Tối ưu S3 Bucket Key: giảm 99% KMS calls, chi phí từ $2.80 → $1.05/tháng
  * Tuân thủ: Encryption at rest đáp ứng yêu cầu GDPR, HIPAA, PCI-DSS

* Tổng kết hoàn thành AWS Workforce Bootcamp:
  * Hoàn thành 33 labs trong 12 tuần (17/04/2026 - 10/07/2026)
  * Nắm vững hơn 15 dịch vụ AWS: IAM, EC2, S3, Lambda, DynamoDB, API Gateway, CloudWatch, Systems Manager, KMS, CloudTrail, Athena
  * Có kinh nghiệm thực tế với tối ưu chi phí, thực tiễn bảo mật tốt nhất, giám sát và tuân thủ
  * Sẵn sàng cho các chứng chỉ AWS: Cloud Practitioner (Sẵn sàng), Solutions Architect Associate (80% Sẵn sàng)
  * Nhận được chứng chỉ hoàn thành, sẵn sàng cho cơ hội nghề nghiệp AWS

