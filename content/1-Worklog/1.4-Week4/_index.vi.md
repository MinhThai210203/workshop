---
title: "Nhật ký công việc Tuần 4"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.4. </b> "
---
### Mục tiêu tuần 4:

* Tìm hiểu và xây dựng bài tập cho dịch vụ cơ sở dữ liệu quản lý Amazon RDS.
* Triển khai Auto Scaling để tự động mở rộng các EC2 instances dựa trên nhu cầu.
* Giám sát tài nguyên và thiết lập cảnh báo CloudWatch cho các chỉ số hiệu năng.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu các khái niệm cơ bản Amazon RDS<br>- Các loại công cụ RDS (MySQL, PostgreSQL, Oracle...)<br>- Tạo RDS database instance<br>- Cấu hình nhóm subnet DB và security groups | 11/05/2026 | 11/05/2026 | <https://000005.awsstudygroup.com/> |
| 3 | - Kết nối EC2 với cơ sở dữ liệu RDS<br>- Triển khai ứng dụng với backend RDS<br>- Triển khai ứng dụng sử dụng RDS<br>- Sao lưu và khôi phục dữ liệu | 12/05/2026 | 12/05/2026 | <https://000005.awsstudygroup.com/> |
| 4 | - Tìm hiểu Auto Scaling với Elastic Load Balancing<br>- Chuẩn bị thiết lập môi trường multi-AZ<br>- Tạo Launch Template cho EC2<br>- Thiết lập Load Balancer và Target Groups | 13/05/2026 | 13/05/2026 | <https://000006.awsstudygroup.com/> |
| 5 | - Tạo Auto Scaling Group<br>- Cấu hình chính sách mở rộng<br>- Kiểm tra kết quả Auto Scaling<br>- Kiểm tra health checks và failover | 14/05/2026 | 14/05/2026 | <https://000006.awsstudygroup.com/> |
| 6 | - Nghiên cứu Amazon CloudWatch<br>- Tìm hiểu CloudWatch Metrics, Logs, Alarms<br>- Tạo số liệu tùy chỉnh và bảng điều khiển<br>- Thiết lập giám sát cho EC2 và RDS | 15/05/2026 | 15/05/2026 | <https://000008.awsstudygroup.com/> |

### Kết quả đạt được tuần 4:

* Hiểu Amazon RDS (Relational Database Service) - dịch vụ cơ sở dữ liệu được quản lý:
  * Các loại công cụ: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server
  * Triển khai Multi-AZ cho tính khả dụng cao
  * Read Replicas để mở rộng đọc
  * Sao lưu tự động và thời gian lưu giữ
  * Snapshot thủ công
  * Khôi phục theo thời điểm

* Triển khai thành công RDS MySQL instance:
  * Tạo VPC và subnets cho RDS
  * Cấu hình nhóm subnet DB
  * Tạo security groups để truy cập cơ sở dữ liệu
  * Khởi chạy RDS MySQL instance
  * Cấu hình nhóm tham số
  * Kết nối EC2 instance với RDS
  * Triển khai ứng dụng AWS FCJ Management với backend RDS
  * Cấu hình chuỗi kết nối và biến môi trường
  * Kiểm tra các thao tác CRUD với cơ sở dữ liệu
  * Khôi phục cơ sở dữ liệu từ snapshot

**Ảnh chụp màn hình từ bài thực hành Amazon RDS:**

![Thiết lập RDS](/images/khong5.png)

![Cấu hình RDS](/images/khong51.png)

![RDS Database Instance](/images/khong52.png)

![Tích hợp ứng dụng RDS](/images/khong53.png)

* Triển khai Auto Scaling và Elastic Load Balancing:
  * Các khái niệm cơ bản Application Load Balancer (ALB)
  * Target Groups và health checks
  * Quy tắc listener và định tuyến
  * Cân bằng tải xuyên vùng
  * Tạo Launch Template với AMI, loại instance, security groups
  * Scripts user data cho bootstrapping
  * Phiên bản template
  * Tạo Auto Scaling Group với launch template
  * Cấu hình dung lượng mong muốn, tối thiểu, tối đa
  * Các loại health check (EC2, ELB)
  * Thời gian khởi động instance
  * Target tracking scaling (sử dụng CPU)
  * Chính sách Step scaling và Simple scaling
  * Thời gian cooldown mở rộng

**Ảnh chụp màn hình từ bài thực hành Auto Scaling & ELB:**

![Thiết lập Auto Scaling](/images/khongsau.png)

![Cấu hình Load Balancer](/images/khongsau1.png)

![Auto Scaling Group](/images/khongsau2.png)

![Kiểm tra Scaling Policy](/images/khongsau3.png)

* Nắm vững giám sát và cảnh báo Amazon CloudWatch:
  * Số liệu tích hợp cho EC2, RDS, ALB
  * Số liệu tùy chỉnh với PutMetricData
  * Metric math và thống kê
  * Bộ lọc số liệu cho logs
  * Nhóm log và luồng log
  * Cài đặt CloudWatch Logs Agent
  * Chính sách lưu giữ log
  * Truy vấn log insights
  * Tạo cảnh báo dựa trên số liệu
  * Trạng thái cảnh báo (OK, ALARM, INSUFFICIENT_DATA)
  * Thông báo SNS
  * Hành động cảnh báo (Auto Scaling, EC2, SNS)
  * Tạo bảng điều khiển tùy chỉnh
  * Các loại widget (đường, vùng xếp chồng, số)
  * Bảng điều khiển xuyên vùng
  * Chia sẻ bảng điều khiển


