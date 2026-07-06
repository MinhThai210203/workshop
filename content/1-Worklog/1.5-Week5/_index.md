---
title: "Week 5 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.5. </b> "
---
### Week 5 Objectives:

* Research and master AWS Command Line Interface (AWS CLI).
* Implement AWS IAM Identity Center for centralized identity management.
* Configure AWS Backup for automated backup and disaster recovery strategy.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| Mon | - Research AWS CLI fundamentals<br>- Install and configure AWS CLI<br>- Check resources with CLI<br>- Use CLI with S3, SNS, IAM, VPC, EC2 | 05/18/2026 | 05/18/2026 | <https://000011.awsstudygroup.com/> |
| Tue | - Troubleshoot errors and CLI issues<br>- Best practices for AWS CLI<br>- CLI profiles and credential management<br>- Automation scripts with AWS CLI | 05/19/2026 | 05/19/2026 | <https://000011.awsstudygroup.com/> |
| Wed | - Practice using AWS IAM Identity Center<br>- Manage robust identity prepare AWS Account in Organizations<br>- Navigate IAM Identity Center features<br>- Create users and groups in Identity Center | 05/20/2026 | 05/20/2026 | <https://000012.awsstudygroup.com/> |
| Thu | - Create and provide Permission Sets<br>- Access and use Time-based access control<br>- Customer Managed Policies<br>- IAM Identity Center Identity Store APIs | 05/21/2026 | 05/21/2026 | <https://000012.awsstudygroup.com/> |
| Fri | - Learn and deploy AWS Backup<br>- Create S3 Bucket and Backup plan<br>- Deploy infrastructure for notification setup<br>- Check operation<br>- Export EC2 instance and on-premises VM to AWS | 05/22/2026 | 05/22/2026 | <https://000013.awsstudygroup.com/> |

### Week 5 Achievements:

* Mastered AWS Command Line Interface (AWS CLI):
  * Installed AWS CLI version 2
  * Configured credentials with aws configure
  * AWS CLI profiles for multiple accounts
  * Output formats (JSON, text, table, YAML)
  * Created and managed IAM Groups, Users
  * Generated Access Keys
  * Attached policies to users/groups
  * Listed and described IAM resources
  * S3: Created buckets, uploaded/downloaded files, synced folders
  * SNS: Created topics, subscriptions, published messages
  * VPC: Described VPCs, subnets, security groups
  * EC2: Launched instances, stopped/started, described instances, created key pairs
  * Query filters with --query parameter (JMESPath)
  * Pagination with --max-items and --page-size
  * Bash scripting for automation
  * Error handling and troubleshooting

* Deployed AWS IAM Identity Center for multi-account management:
  * Enabled IAM Identity Center in AWS Organizations
  * Configured Identity source (Identity Center directory or external IdP)
  * Multi-account access management
  * Centralized user and group management
  * Created users in Identity Center directory
  * Organized users into groups
  * User attributes and profile information
  * Password policies and MFA enforcement
  * Created permission sets with AWS managed policies
  * Custom permission sets with inline policies
  * Session duration configuration
  * Permission set assignments for accounts
  * Time-based access control with session limits
  * Customer Managed Policies integration
  * Identity Store APIs for programmatic access
  * AWS CLI configuration with SSO
  * Federated access from corporate directory
  * Principle of least privilege
  * Regular access reviews
  * Audit logging with CloudTrail
  * Attribute-based access control (ABAC)

* Deployed AWS Backup solution for disaster recovery:
  * Backups for S3 buckets
  * EC2 instance backups
  * RDS database snapshots
  * Cross-region backup copies
  * Created backup plans with schedules
  * Retention policies
  * Lifecycle rules
  * Backup vault configuration
  * SNS topics for backup notifications
  * CloudWatch Events for monitoring
  * IAM roles for AWS Backup service
  * Exported EC2 instances as OVA/VHD
  * Imported on-premises VMs to AWS
  * VMware integration
  * Created instance on on-premises virtualization environment with Ubuntu for VMware
  * Backup testing and restore procedures
