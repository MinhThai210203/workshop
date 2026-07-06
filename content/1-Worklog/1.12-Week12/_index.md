---
title: "Week 12 Work Log"
date: 2024-01-01
weight: 12
chapter: false
pre: " <b> 1.12. </b> "
---
### Week 12 Objectives:

* Choose the right EC2 size with CloudWatch Agent and AWS Compute Optimizer.
* Encrypt data at rest with AWS KMS and S3.
* Set up audit logging with CloudTrail and query with Athena.

### Tasks to be implemented this week:
| Day | Tasks | Start Date | Completion Date | Reference Documents |
| --- | --- | --- | --- | --- |
| Mon | - Study CloudWatch and CloudWatch Agent<br>- Learn about EC2 Right Sizing and cost optimization<br>- Create IAM Role for CloudWatch Agent<br>- Launch EC2 instance to test monitoring | 07/06/2026 | 07/06/2026 | <https://000032.awsstudygroup.com/> |
| Tue | - Install CloudWatch Agent on EC2 instance<br>- Configure memory and disk metrics collection<br>- Generate workload to collect data<br>- Verify metrics in CloudWatch console | 07/07/2026 | 07/07/2026 | <https://000032.awsstudygroup.com/> |
| Wed | - Analyze CloudWatch metrics data<br>- Enable AWS Compute Optimizer<br>- Review right-sizing recommendations<br>- Apply best practices for EC2 sizing | 07/08/2026 | 07/08/2026 | <https://000032.awsstudygroup.com/> |
| Thu | - Study AWS KMS and encryption concepts<br>- Create IAM Users for testing<br>- Create Customer Managed Key (CMK)<br>- Configure key policies and permissions<br>- Create S3 bucket with KMS encryption | 07/09/2026 | 07/09/2026 | <https://000033.awsstudygroup.com/> |
| Fri | - Enable CloudTrail logging for KMS operations<br>- Setup Amazon Athena for log queries<br>- Test encryption and decryption operations<br>- Query audit logs with Athena<br>- Complete and summarize the program | 07/10/2026 | 07/10/2026 | <https://000033.awsstudygroup.com/> |

### Week 12 Achievements:

* Mastered Amazon CloudWatch and EC2 Right Sizing:
  * Understand CloudWatch architecture: Basic monitoring vs Detailed monitoring
  * CloudWatch Agent required to collect memory and disk utilization metrics
  * Created IAM Role `CloudWatchAgentRole` and launched EC2 instance t3.large for testing
  * Installed CloudWatch Agent, configured metrics: `mem_used_percent`, `disk_used_percent`
  * Generated test workload with stress tool: CPU spike 15% → 85%, Memory spike 35% → 60%
  * Created CloudWatch Dashboard to visualize metrics in real-time

* Analyzed and optimized costs with AWS Compute Optimizer:
  * Enabled AWS Compute Optimizer (free service)
  * Instance analysis: t3.large with CPU average 15%, Memory average 35%
  * Recommended instance: t3.medium - Cost savings: 50% (~$30/month per instance)
  * Current: $0.0832/hour, Recommended: $0.0416/hour
  * Right-sizing best practices: Start small, monitor continuously, review quarterly

* Mastered AWS Key Management Service (KMS):
  * Understand KMS fundamentals: Customer Master Keys (CMK), encryption at rest
  * Pricing: $1/month per CMK + $0.03 per 10,000 requests
  * Created IAM Users: `UserA` (owner), `UserB` (receiver), `UserC` (no permissions)
  * Created Customer Managed Key with symmetric encryption, enabled automatic rotation
  * Created S3 bucket with KMS encryption (SSE-KMS with custom CMK)
  * Enabled Bucket Key to reduce KMS API calls (cost optimization)

* Implemented audit logging and compliance:
  * Created CloudTrail trail to capture KMS API calls and S3 data events
  * Set up Amazon Athena with database `cloudtrail_logs`
  * Tested encryption workflow: UserA upload → auto-encrypted, UserA and UserB download successful
  * UserC attempted download: Access Denied (access control working correctly)
  * Queried audit logs with Athena SQL: tracked Encrypt, Decrypt, GenerateDataKey operations
  * S3 Bucket Key optimization: reduced KMS calls by 99%, cost from $2.80 → $1.05/month
  * Compliance: Encryption at rest meets GDPR, HIPAA, PCI-DSS requirements

* Completed AWS Workforce Bootcamp:
  * Completed 33 labs in 12 weeks (04/17/2026 - 07/10/2026)
  * Mastered 15+ AWS services: IAM, EC2, S3, Lambda, DynamoDB, API Gateway, CloudWatch, Systems Manager, KMS, CloudTrail, Athena
  * Gained hands-on experience with cost optimization, security best practices, monitoring and compliance
  * Ready for AWS Certifications: Cloud Practitioner (Ready), Solutions Architect Associate (80% Ready)
  * Received certificate of completion, ready for AWS career opportunities

