---
title: "Nhật ký công việc Tuần 9"
date: 2024-01-01
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---
### Mục tiêu tuần 9:

* Triển khai hoàn chỉnh CI/CD pipeline với AWS CodePipeline, CodeBuild và CodeDeploy.
* Cấu hình tích hợp Git với AWS CodeCommit và triển khai tự động.
* Triển khai giải pháp hybrid storage với AWS Storage Gateway cho tích hợp on-premises.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Nghiên cứu AWS CI/CD services ecosystem<br>- Chuẩn bị infrastructure: VPC, Security Groups, S3 bucket<br>- Tạo IAM roles cho CI/CD services<br>- Install và configure CodeDeploy Agent trên EC2 | 15/06/2026 | 15/06/2026 | <https://000023.awsstudygroup.com/> |
| 3 | - Tạo AWS CodeCommit repository<br>- Configure Git credentials cho HTTPS connections<br>- Clone repository và push sample application code<br>- Configure service roles cho CodePipeline | 16/06/2026 | 16/06/2026 | <https://000023.awsstudygroup.com/> |
| 4 | - Tạo CodeBuild project với buildspec.yml<br>- Write buildspec.yml cho Node.js application<br>- Tạo CodeDeploy application và deployment groups<br>- Configure appspec.yml và test manual deployment | 17/06/2026 | 17/06/2026 | <https://000023.awsstudygroup.com/> |
| 5 | - Tạo CodePipeline với 3 stages: Source, Build, Deploy<br>- Test end-to-end CI/CD pipeline<br>- Commit code changes và watch automatic deployment<br>- Monitor pipeline execution và troubleshoot | 18/06/2026 | 18/06/2026 | <https://000023.awsstudygroup.com/> |
| 6 | - Tìm hiểu AWS Storage Gateway types và use cases<br>- Tạo S3 bucket cho File Gateway storage<br>- Launch EC2 instance với AMI Storage Gateway<br>- Configure Storage Gateway và create file shares | 19/06/2026 | 20/06/2026 | <https://000024.awsstudygroup.com/> |

### Kết quả đạt được tuần 9:

* Thành thạo AWS CI/CD services cho application deployment:
  * Hiểu rõ AWS CI/CD services ecosystem: CodePipeline, CodeBuild, CodeDeploy, CodeCommit
  * So sánh AWS CodeCommit vs GitHub vs GitLab
  * Chuẩn bị infrastructure đầy đủ: VPC, Security Groups, S3 bucket for artifacts
  * Tạo IAM roles và policies cho tất cả CI/CD services
  * Set up EC2 instances với appropriate IAM instance profile
  * Install và configure CodeDeploy Agent thành công trên EC2
  * CodeDeploy Agent hoạt động và có thể nhận deployments

* Nắm vững AWS CodeCommit và Git integration:
  * Tạo AWS CodeCommit repository thành công
  * Configure Git credentials cho HTTPS connections
  * Clone repository và push sample Node.js application code
  * Set up Git connection từ local machine
  * Create branches và test Git workflow
  * Migrate repository sang GitLab/GitHub (optional practice)
  * Configure service roles cho CodePipeline để access CodeCommit
  * Set up IAM users với appropriate Git permissions

* Triển khai CodeBuild và CodeDeploy:
  * Tạo CodeBuild project với build environment configuration
  * Write buildspec.yml cho Node.js application (install, build, artifacts)
  * Test CodeBuild manually và review build logs
  * Troubleshoot build failures
  * Tạo CodeDeploy application và deployment groups
  * Configure appspec.yml file với deployment hooks
  * Set up deployment configuration (AllAtOnce, HalfAtATime, OneAtATime)
  * Test manual deployment với CodeDeploy thành công
  * CodeBuild và CodeDeploy hoạt động độc lập

* Hoàn thành CI/CD Pipeline với CodePipeline:
  * Tạo CodePipeline với 3 stages: Source (CodeCommit), Build (CodeBuild), Deploy (CodeDeploy)
  * Configure pipeline settings và service role
  * Link tất cả services together trong pipeline
  * Test end-to-end CI/CD pipeline thành công
  * Commit code changes và watch automatic deployment
  * Monitor pipeline execution từ source đến production
  * Troubleshoot failed deployments và implement rollback strategies
  * Complete CI/CD pipeline hoạt động tự động, code changes được deploy automatically
  * Hiểu rõ best practices cho CI/CD trên AWS

* Triển khai AWS Storage Gateway cho hybrid storage:
  * Nghiên cứu về AWS Storage Gateway types (File Gateway, Volume Gateway, Tape Gateway)
  * Hiểu File Gateway architecture và use cases
  * Hybrid cloud storage strategies
  * Tạo S3 bucket cho File Gateway storage backend
  * Launch EC2 instance với AMI Storage Gateway provided by AWS
  * Configure Storage Gateway và activate
  * Create File Gateway thành công
  * Set up SMB/NFS file shares
  * Configure guest access settings và permissions
  * Mount file share trên on-premises machine (Windows/Linux)
  * Test file operations: upload, download, modify
  * Verify files được sync tự động lên S3
  * Files hoạt động seamlessly giữa on-premises và cloud storage
  * Monitor Storage Gateway metrics trên CloudWatch
  * Hoàn thành hybrid storage solution
