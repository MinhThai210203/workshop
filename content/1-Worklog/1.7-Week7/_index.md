---
title: "Week 7 Worklog"
date: 2024-01-01
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---
### Week 7 Objectives:

* Build CI/CD pipeline for container deployment with GitLab and AWS ECS.
* Implement security monitoring with AWS Security Hub.
* Deploy VPC Peering with CloudFormation for multi-VPC architecture connectivity.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Research CI/CD architecture on Amazon ECS<br>- Learn Docker containerization and ECS Task Definitions<br>- Environment preparation: create ECS Cluster, ECR repository<br>- Configure GitLab repository and create Dockerfile | 06/01/2026 | 06/01/2026 | <https://000017.awsstudygroup.com/> |
| 3 | - Write GitLab CI/CD configuration file (.gitlab-ci.yml)<br>- Integrate GitHub Actions with AWS CodeBuild<br>- Configure automated build and push Docker image<br>- Deploy application to ECS through CI/CD | 06/02/2026 | 06/02/2026 | <https://000017.awsstudygroup.com/> |
| 4 | - Learn AWS Security Hub and security standards<br>- Enable AWS Security Hub in account<br>- Configure security standards (CIS AWS Foundations, PCI DSS)<br>- Analyze security findings and create custom insights | 06/03/2026 | 06/03/2026 | <https://000018.awsstudygroup.com/> |
| 5 | - Research VPC Peering architecture and use cases<br>- Create CloudFormation template for multi-VPC architecture<br>- Configure VPC Peering connection and update route tables<br>- Launch EC2 instances in both VPCs | 06/04/2026 | 06/04/2026 | <https://000019.awsstudygroup.com/> |
| 6 | - Configure Security Groups for peered VPCs<br>- Test connectivity between instances via private IPs<br>- Implement security best practices for VPC Peering<br>- Configure Network ACLs and document architecture | 06/05/2026 | 06/05/2026 | <https://000019.awsstudygroup.com/> |

### Week 7 Achievements:

* Mastered CI/CD pipeline for container deployment:
  * Understand CI/CD pipeline workflow on Amazon ECS
  * Proficient in Docker containerization and ECS Task Definitions
  * Successfully integrated GitLab CI/CD with AWS services
  * Wrote GitLab CI/CD configuration file (.gitlab-ci.yml) and GitHub Actions workflow
  * Successfully created ECS cluster, ECR repository for Docker image storage
  * Set up IAM roles for ECS Task execution
  * CI/CD pipeline working end-to-end, application deployed automatically on code changes
  * Logs and monitoring fully configured

* Implemented AWS Security Hub for security monitoring:
  * Understand AWS Security Hub and AWS Foundational Security Best Practices
  * Enabled AWS Security Hub and configured security standards (CIS AWS Foundations, PCI DSS)
  * Analyzed security findings and compliance status
  * Set up automated remediation with AWS Config
  * Created custom insights and security dashboards for security monitoring
  * Security Hub helps detect and remediate security vulnerabilities

* Mastered VPC Peering with Infrastructure as Code:
  * Researched VPC Peering architecture, use cases, and routing
  * Created CloudFormation template for multi-VPC architecture
  * Successfully deployed 2 VPCs via CloudFormation stack
  * Established VPC Peering connection and updated route tables for peering traffic
  * Launched EC2 instances in both VPCs
  * Configured Security Groups for peered VPCs
  * Tested and verified connectivity between instances via private IPs (ICMP ping, SSH connection)
  * Implemented security best practices: Network ACLs, least privilege principle
  * Cross-VPC connectivity working perfectly via private network
