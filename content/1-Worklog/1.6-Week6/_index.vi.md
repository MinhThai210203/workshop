---
title: "Nhật ký công việc Tuần 6"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.6. </b> "
---
### Mục tiêu tuần 6:

* Học tập và triển khai ứng dụng trên các Docker containers với AWS.
* Nghiên cứu và làm việc với Amazon Elastic Container Service (ECS).
* Cấu hình các ECS clusters, task definitions, services và load balancing.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Học tập các khái niệm cơ bản Docker<br>- Tìm hiểu Docker images, containers, Dockerfile<br>- Chuẩn bị VPC, Security Group, IAM truy cập ECR<br>- Đăng nhập vào Docker Hub | 25/05/2026 | 25/05/2026 | <https://000015.awsstudygroup.com/> |
| 3 | - Tạo và khởi chạy EC2 instance<br>- Cài đặt Docker trên EC2<br>- Cấu hình EC2 trên instance<br>- Cài đặt các thư viện và dependencies | 26/05/2026 | 26/05/2026 | <https://000015.awsstudygroup.com/> |
| 4 | - Tạo và khởi chạy RDS database instance<br>- Triển khai Docker Image, Docker Compose<br>- Đẩy Image sử dụng Docker Hub và Amazon ECR<br>- Dọn dẹp tài nguyên | 27/05/2026 | 27/05/2026 | <https://000015.awsstudygroup.com/> |
| 5 | - Nghiên cứu Amazon Elastic Container Service (ECS)<br>- Tìm hiểu các khái niệm ECS: Clusters, Tasks, Services<br>- Chuẩn bị cấu hình hạ tầng<br>- Role CodeDeploy, NAT gateway, Route Table, Security Group | 28/05/2026 | 28/05/2026 | <https://000016.awsstudygroup.com/> |
| 6 | - Thêm Subnet, chuẩn bị triển khai Docker image lên ECR và Dockerhub<br>- Đăng ký namespace trong Cloud Map<br>- Tạo ECS Cluster, Task Definition<br>- Cấu hình Application Load Balancer, Target Group<br>- Tạo ECS Service, triển khai Blue/Green, cập nhật Rolling | 29/05/2026 | 29/05/2026 | <https://000016.awsstudygroup.com/> |

### Kết quả đạt được tuần 6:

* Hiểu Docker containerization và lợi ích so với VMs:
  * Docker architecture: Docker Engine, Docker Client, Docker Daemon
  * Images vs Containers
  * Docker Hub registry
  * Dockerfile syntax và best practices
  * Cài đặt Docker trên Amazon Linux 2023
  * Docker commands: pull, run, build, push, ps, stop, rm
  * Docker networking modes
  * Volume mounting cho persistent data
  * Multi-stage builds cho optimization
  * Environment variables trong Docker
  * COPY vs ADD commands
  * ENTRYPOINT vs CMD
  * Docker layer caching

* Deploy multi-container application với Docker Compose:
  * Tạo VPC với public/private subnets
  * Cấu hình Security Groups cho Docker containers
  * IAM roles cho ECR access
  * EC2 instance với Docker installed
  * docker-compose.yml configuration
  * Multi-container applications
  * Service dependencies
  * Networks và volumes trong Compose
  * Environment variables management
  * Push/pull images từ Docker Hub (Public vs private repositories)
  * Image tagging strategies
  * Tạo ECR repositories
  * ECR authentication với Docker
  * Push images lên ECR
  * Image scanning cho vulnerabilities
  * Lifecycle policies

* Triển khai Amazon Elastic Container Service (ECS):
  * ECS Clusters (EC2 vs Fargate launch types)
  * Task Definitions (container specifications)
  * ECS Tasks (running instances của Task Definitions)
  * ECS Services (maintaining desired task count)
  * Service Discovery với AWS Cloud Map
  * Tạo ECS Cluster với EC2 launch type
  * Container instances registration
  * Capacity providers configuration
  * Cluster auto-scaling
  * Container definitions (image, CPU, memory)
  * Port mappings
  * Environment variables
  * IAM task roles vs execution roles
  * Task networking modes (bridge, awsvpc, host)
  * Volume mounts (EFS, bind mounts)
  * Service creation với desired count
  * Load balancer integration (ALB/NLB)
  * Target Group configuration
  * Health check settings
  * Service auto-scaling policies

* Nắm vững ECS Deployment Strategies:
  * Rolling Update - Minimum healthy percent, Maximum percent, Deployment circuit breaker
  * Blue/Green Deployment - AWS CodeDeploy integration
  * Traffic shifting strategies (Linear, Canary, All-at-once)
  * Automatic rollback capabilities
  * CloudWatch alarms for deployment monitoring
  * Service Discovery với Cloud Map
  * ECS Exec cho container debugging
  * Container Insights monitoring
  * Task placement strategies
  * Secrets management với AWS Secrets Manager


