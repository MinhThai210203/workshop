---
title: "Nhật ký công việc Tuần 10"
date: 2024-01-01
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---
### Mục tiêu tuần 10:

* Triển khai AWS WAF để bảo vệ ứng dụng web khỏi các tấn công phổ biến (SQL injection, XSS).
* Thành thạo chiến lược resource tagging và Resource Groups để tổ chức tài nguyên hiệu quả.
* Triển khai chính sách IAM dựa trên tags (ABAC) để kiểm soát truy cập dựa trên resource tags.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Nghiên cứu khái niệm và kiến trúc AWS WAF<br>- Tìm hiểu về OWASP Top 10 vulnerabilities<br>- Tạo S3 bucket và deploy ứng dụng web mẫu (OWASP Juice Shop)<br>- Test chức năng và xác định lỗ hổng bảo mật | 22/06/2026 | 22/06/2026 | <https://000026.awsstudygroup.com/> |
| 3 | - Tạo Web ACL từ WAF console<br>- Associate Web ACL với CloudFront hoặc ALB<br>- Implement managed rules từ AWS<br>- Configure rate-based rules và test | 23/06/2026 | 23/06/2026 | <https://000026.awsstudygroup.com/> |
| 4 | - Tạo custom rules cho SQL injection protection<br>- Configure XSS (Cross-Site Scripting) rules<br>- Test custom rules với attack simulations<br>- Implement IP set rules | 24/06/2026 | 24/06/2026 | <https://000026.awsstudygroup.com/> |
| 5 | - Enable WAF logging tới S3 hoặc CloudWatch Logs<br>- Analyze WAF logs và fine-tune rules<br>- Configure CloudWatch alarms cho WAF<br>- Document WAF configuration | 25/06/2026 | 25/06/2026 | <https://000026.awsstudygroup.com/> |
| 6 | - Nghiên cứu resource tagging strategies và best practices<br>- Chuẩn bị EC2 resources cho tagging<br>- Tag EC2 instances và EBS volumes sử dụng Console<br>- Filter và organize tagged resources | 26/06/2026 | 28/06/2026 | <https://000027.awsstudygroup.com/><br><https://000028.awsstudygroup.com/> |

### Kết quả đạt được tuần 10:

* Thành thạo AWS WAF cho web application security:
  * Hiểu rõ khái niệm và kiến trúc AWS WAF
  * Nắm vững các lỗ hổng web phổ biến (OWASP Top 10): SQL Injection, XSS, CSRF, etc.
  * Hiểu về Web ACL, Rules và Rule Groups
  * Tạo S3 bucket và deploy ứng dụng web mẫu có lỗ hổng (OWASP Juice Shop)
  * Test và xác định các security vulnerabilities trong application
  * Tạo Web ACL từ WAF console và associate với CloudFront/ALB thành công
  * Configure Web ACL settings đúng
  * Implement managed rules từ AWS Managed Rules
  * Configure rate-based rules để chống DDoS
  * Test rules chống lại sample attacks và verify blocking

* Nắm vững custom WAF rules và advanced configuration:
  * Tạo custom rules cho specific threats
  * Implement SQL injection protection rules
  * Configure XSS (Cross-Site Scripting) prevention rules
  * Test custom rules với attack simulations và penetration testing
  * Tạo advanced custom rules với complex conditions
  * Configure rule priority và actions (Allow, Block, Count)
  * Implement IP set rules cho blacklist/whitelist
  * Test comprehensive rule set với real-world scenarios
  * Custom rules bảo vệ chống SQL injection và XSS attacks thành công
  * Rule priority được tối ưu cho performance

* Triển khai WAF logging và monitoring:
  * Enable WAF logging tới S3 bucket và CloudWatch Logs
  * Configure request sampling để analyze traffic patterns
  * Analyze WAF logs để identify attack patterns
  * Review blocked và allowed requests
  * Fine-tune rules dựa trên actual traffic và logs
  * Configure CloudWatch alarms cho WAF metrics (blocked requests, rate limits)
  * Monitor WAF effectiveness và adjust rules
  * Document complete WAF configuration, rules và testing results
  * WAF protection hoạt động hiệu quả chống lại common web attacks

* Thành thạo Resource Tagging và Resource Groups:
  * Nghiên cứu và design comprehensive resource tagging strategy
  * Hiểu tagging best practices và naming conventions
  * Tag categories: Environment (Dev/Test/Prod), CostCenter, Project, Owner, Schedule
  * Hiểu về tag-based cost allocation và billing
  * Chuẩn bị EC2 instances, EBS volumes và other resources cho tagging
  * Tag resources sử dụng AWS Console (point-and-click)
  * Tag resources sử dụng AWS CLI (bulk operations)
  * Write scripts cho automated tagging
  * Update và delete tags via Console và CLI
  * Filter resources theo tags trong AWS Console
  * Search và organize tagged resources efficiently
  * AWS CLI tagging operations thành thạo

* Sử dụng Resource Groups cho resource management:
  * Tạo Resource Groups dựa trên tag queries
  * Configure Resource Groups với complex tag filters
  * Sử dụng Resource Groups để group related resources
  * Test Resource Groups functionality cho bulk operations
  * Monitor resources trong groups
  * Resource Groups giúp organize và manage resources hiệu quả
  * Efficient resource organization đạt được

* Implement IAM tag-based access control (ABAC):
  * Nghiên cứu về IAM attribute-based access control (ABAC)
  * Hiểu tag-based IAM policies
  * Tạo IAM users cho testing scenarios
  * Design IAM policies dựa trên resource tags
  * Tạo IAM policy cho phép access chỉ tới resources với specific tags
  * Implement tag-based permissions cho EC2 operations (Start, Stop, Terminate)
  * Test IAM policies với different users và scenarios
  * Verify access control: users chỉ access được tagged resources
  * Enforce tagging requirements qua IAM policies
  * Tag-based IAM policies working correctly
  * Document tag-based security model và best practices
  * Hiểu rõ cách scale security với tags trong large environments
