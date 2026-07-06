---
title: "Nhật ký công việc Tuần 8"
date: 2024-01-01
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---
### Mục tiêu tuần 8:

* Triển khai AWS Transit Gateway để kết nối nhiều VPCs trong kiến trúc hub-and-spoke.
* Tối ưu hóa chi phí EC2 với Lambda automation để bật/tắt instances theo lịch trình.
* Triển khai chiến lược resource tagging và lập lịch với EventBridge.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Nghiên cứu AWS Transit Gateway architecture và use cases<br>- So sánh Transit Gateway vs VPC Peering<br>- Tạo Transit Gateway và configure settings<br>- Attach VPCs vào Transit Gateway | 08/06/2026 | 08/06/2026 | <https://000020.awsstudygroup.com/> |
| 3 | - Cấu hình Transit Gateway route tables<br>- Test connectivity giữa multiple VPCs<br>- Launch EC2 instances và test inter-VPC communication<br>- Monitor Transit Gateway metrics trên CloudWatch | 09/06/2026 | 09/06/2026 | <https://000020.awsstudygroup.com/> |
| 4 | - Nghiên cứu EC2 cost optimization strategies<br>- Tìm hiểu về Lambda functions cho automation<br>- Tạo IAM roles cho Lambda execution<br>- Viết Lambda function để stop EC2 instances | 10/06/2026 | 10/06/2026 | <https://000022.awsstudygroup.com/> |
| 5 | - Viết Lambda function để start EC2 instances<br>- Implement resource tagging strategy<br>- Configure EventBridge rules cho scheduled execution<br>- Test automated start/stop schedule | 11/06/2026 | 11/06/2026 | <https://000022.awsstudygroup.com/> |
| 6 | - Implement SNS notifications cho Lambda executions<br>- Configure CloudWatch alarms cho cost monitoring<br>- Create CloudWatch dashboard cho cost tracking<br>- Document toàn bộ solution architecture | 12/06/2026 | 12/06/2026 | <https://000022.awsstudygroup.com/> |

### Kết quả đạt được tuần 8:

* Thành thạo AWS Transit Gateway cho multi-VPC networking:
  * Hiểu rõ AWS Transit Gateway architecture và so sánh với VPC Peering
  * Nắm vững route table propagation và associations
  * Tạo Transit Gateway thành công và configure settings
  * Attach 3 VPCs vào Transit Gateway
  * Cấu hình Transit Gateway route tables cho inter-VPC routing
  * Set up route propagation tự động
  * Launch EC2 instances trong các VPCs và test connectivity
  * Tất cả VPCs có thể communicate qua Transit Gateway
  * Monitor Transit Gateway metrics và traffic trên CloudWatch
  * Implement Transit Gateway Network Manager (optional)
  * Nắm vững kiến trúc networking phức tạp với Transit Gateway

* Tối ưu hóa chi phí EC2 với Lambda automation:
  * Hiểu rõ các phương pháp tối ưu chi phí EC2 (right-sizing, scheduling, Savings Plans)
  * Tìm hiểu về Lambda functions cho infrastructure automation
  * Nắm vững resource tagging best practices (Environment, Schedule, CostCenter)
  * Tạo IAM roles với permissions phù hợp cho Lambda execution
  * Viết Lambda function để stop EC2 instances dựa trên tags
  * Viết Lambda function để start EC2 instances theo schedule
  * Implement resource tagging strategy cho EC2 instances
  * Configure EventBridge (CloudWatch Events) rules cho scheduled execution
  * Set up cron expressions cho business hours (weekdays only)
  * Test automated start/stop schedule hoạt động đúng
  * Lambda functions filtering instances based on tags
  * Monitor Lambda execution logs và troubleshooting

* Monitoring và Notifications cho cost optimization:
  * Implement SNS notifications cho Lambda execution results
  * Subscribe email endpoints cho alerts
  * Configure CloudWatch alarms cho cost monitoring
  * Create CloudWatch dashboard hiển thị cost metrics và instance states
  * Email notifications hoạt động khi instances start/stop
  * Calculate cost savings từ automation solution
  * Document toàn bộ solution architecture và ROI
  * Hoàn thành giải pháp tối ưu chi phí tự động và scalable
