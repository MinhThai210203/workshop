---
title: "Nhật ký công việc Tuần 7"
date: 2024-01-01
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---
### Mục tiêu tuần 7:

* Xây dựng CI/CD pipeline cho triển khai container với GitLab và AWS ECS.
* Triển khai giám sát bảo mật với AWS Security Hub.
* Triển khai VPC Peering với CloudFormation để kết nối kiến trúc nhiều VPCs.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Nghiên cứu kiến trúc CI/CD trên Amazon ECS<br>- Tìm hiểu Docker containerization và ECS Task Definitions<br>- Chuẩn bị môi trường: tạo ECS Cluster, ECR repository<br>- Cấu hình GitLab repository và tạo Dockerfile | 01/06/2026 | 01/06/2026 | <https://000017.awsstudygroup.com/> |
| 3 | - Viết GitLab CI/CD configuration file (.gitlab-ci.yml)<br>- Tích hợp GitHub Actions với AWS CodeBuild<br>- Configure automated build và push Docker image<br>- Deploy ứng dụng lên ECS thông qua CI/CD | 02/06/2026 | 02/06/2026 | <https://000017.awsstudygroup.com/> |
| 4 | - Tìm hiểu AWS Security Hub và security standards<br>- Enable AWS Security Hub trong account<br>- Cấu hình security standards (CIS AWS Foundations, PCI DSS)<br>- Phân tích security findings và tạo custom insights | 03/06/2026 | 03/06/2026 | <https://000018.awsstudygroup.com/> |
| 5 | - Nghiên cứu VPC Peering architecture và use cases<br>- Tạo CloudFormation template cho multi-VPC architecture<br>- Cấu hình VPC Peering connection và update route tables<br>- Launch EC2 instances trong cả 2 VPCs | 04/06/2026 | 04/06/2026 | <https://000019.awsstudygroup.com/> |
| 6 | - Cấu hình Security Groups cho peered VPCs<br>- Test connectivity giữa instances qua private IPs<br>- Implement security best practices cho VPC Peering<br>- Cấu hình Network ACLs và document kiến trúc | 05/06/2026 | 05/06/2026 | <https://000019.awsstudygroup.com/> |

### Kết quả đạt được tuần 7:

* Nắm vững CI/CD pipeline cho container deployment:
  * Hiểu rõ workflow của CI/CD pipeline trên Amazon ECS
  * Thành thạo Docker containerization và ECS Task Definitions
  * Tích hợp thành công GitLab CI/CD với AWS services
  * Viết GitLab CI/CD configuration file (.gitlab-ci.yml) và GitHub Actions workflow
  * Tạo thành công ECS cluster, ECR repository để lưu trữ Docker images
  * Thiết lập IAM roles cho ECS Task execution
  * CI/CD pipeline hoạt động end-to-end, ứng dụng được deploy tự động khi có code changes
  * Logs và monitoring được thiết lập đầy đủ

* Triển khai AWS Security Hub để giám sát bảo mật:
  * Hiểu rõ về AWS Security Hub và AWS Foundational Security Best Practices
  * Enable AWS Security Hub và cấu hình security standards (CIS AWS Foundations, PCI DSS)
  * Phân tích security findings và compliance status
  * Thiết lập automated remediation với AWS Config
  * Tạo custom insights và security dashboards để giám sát bảo mật
  * Security Hub giúp phát hiện và khắc phục các lỗ hổng bảo mật

* Thành thạo VPC Peering với Infrastructure as Code:
  * Nghiên cứu VPC Peering architecture, use cases và routing
  * Tạo CloudFormation template cho multi-VPC architecture
  * Deploy 2 VPCs thành công qua CloudFormation stack
  * Thiết lập VPC Peering connection và update route tables cho peering traffic
  * Launch EC2 instances trong cả 2 VPCs
  * Cấu hình Security Groups cho peered VPCs
  * Test và verify connectivity giữa instances qua private IPs (ICMP ping, SSH connection)
  * Implement security best practices: Network ACLs, least privilege principle
  * Connectivity giữa VPCs hoạt động hoàn hảo qua private network
