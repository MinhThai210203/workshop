---
title: "Week 11 Work Log"
date: 2024-01-01
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---
### Week 11 Objectives:

* Limit user permissions with IAM Permission Boundary to prevent privilege escalation.
* Manage patches and run commands on multiple EC2 instances with AWS Systems Manager.
* Centralized management and automation for server fleet operations.

### Tasks to be implemented this week:
| Day | Tasks | Start Date | Completion Date | Reference Documents |
| --- | --- | --- | --- | --- |
| Mon | - Study IAM Permission Boundary concepts<br>- Understand effective permissions calculation<br>- Learn about privilege escalation vulnerabilities<br>- Design Permission Boundary policy for EC2 admin | 06/29/2026 | 06/29/2026 | <https://000030.awsstudygroup.com/> |
| Tue | - Create IAM Permission Boundary policy<br>- Create IAM User with AdministratorAccess policy<br>- Apply Permission Boundary to IAM User<br>- Verify effective permissions | 06/30/2026 | 06/30/2026 | <https://000030.awsstudygroup.com/> |
| Wed | - Test IAM User with Permission Boundary<br>- Verify EC2 operations allowed<br>- Verify other services denied<br>- Test privilege escalation scenarios<br>- Document findings and best practices | 07/01/2026 | 07/01/2026 | <https://000030.awsstudygroup.com/> |
| Thu | - Study AWS Systems Manager architecture<br>- Learn about Session Manager, Patch Manager, Run Command<br>- Create IAM Role for Systems Manager<br>- Launch EC2 instances and attach IAM Role<br>- Configure Patch Manager with Maintenance Window | 07/02/2026 | 07/02/2026 | <https://000031.awsstudygroup.com/> |
| Fri | - Configure Run Command to execute scripts<br>- Install CloudWatch Agent on multiple instances<br>- Run Patch Manager scan and update<br>- Test Session Manager connections<br>- Monitor operations in Systems Manager console | 07/03/2026 | 07/03/2026 | <https://000031.awsstudygroup.com/> |

### Week 11 Achievements:

* Mastered IAM Permission Boundary:
  * Understand IAM Permission Boundary is an advanced feature that limits maximum permissions
  * Effective permissions = Identity-based policy ∩ Permission Boundary
  * Use case: Prevent privilege escalation when users create new IAM entities
  * Created Permission Boundary policy limiting permissions to EC2 service only
  * Created IAM User `EC2Admin` with AdministratorAccess but applied Permission Boundary
  * Successfully tested: User only has permissions on EC2, cannot access S3, RDS, Lambda
  * Cannot create new IAM users or modify permissions (prevent privilege escalation)
  * Simplified permission management for multiple users with changing roles

* Mastered AWS Systems Manager:
  * Understand features: Session Manager, Patch Manager, Run Command, Fleet Manager
  * Created IAM Role `SSMInstanceRole` and launched 3 EC2 instances (Amazon Linux 2)
  * Configured Patch Manager with Maintenance Window (Every Sunday, 2:00 AM)
  * Ran Patch Manager scan: detected 15 missing security patches
  * Patch installation successful: 100% instances compliant
  * Configured Run Command: Installed CloudWatch Agent and executed custom scripts
  * Tested Session Manager: Connected without SSH keys or bastion hosts
  * Operations time reduced 80%, security improved with full audit trail

