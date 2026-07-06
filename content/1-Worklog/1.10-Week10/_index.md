---
title: "Week 10 Worklog"
date: 2024-01-01
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---
### Week 10 Objectives:

* Implement AWS WAF to protect web applications from common attacks (SQL injection, XSS).
* Master resource tagging strategy and Resource Groups for efficient resource organization.
* Implement tag-based IAM policies (ABAC) to control access based on resource tags.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Research AWS WAF concepts and architecture<br>- Learn about OWASP Top 10 vulnerabilities<br>- Create S3 bucket and deploy sample web app (OWASP Juice Shop)<br>- Test functionality and identify security vulnerabilities | 06/22/2026 | 06/22/2026 | <https://000026.awsstudygroup.com/> |
| 3 | - Create Web ACL from WAF console<br>- Associate Web ACL with CloudFront or ALB<br>- Implement managed rules from AWS<br>- Configure rate-based rules and test | 06/23/2026 | 06/23/2026 | <https://000026.awsstudygroup.com/> |
| 4 | - Create custom rules for SQL injection protection<br>- Configure XSS (Cross-Site Scripting) rules<br>- Test custom rules with attack simulations<br>- Implement IP set rules | 06/24/2026 | 06/24/2026 | <https://000026.awsstudygroup.com/> |
| 5 | - Enable WAF logging to S3 or CloudWatch Logs<br>- Analyze WAF logs and fine-tune rules<br>- Configure CloudWatch alarms for WAF<br>- Document WAF configuration | 06/25/2026 | 06/25/2026 | <https://000026.awsstudygroup.com/> |
| 6 | - Research resource tagging strategies and best practices<br>- Prepare EC2 resources for tagging<br>- Tag EC2 instances and EBS volumes using Console<br>- Filter and organize tagged resources | 06/26/2026 | 06/28/2026 | <https://000027.awsstudygroup.com/><br><https://000028.awsstudygroup.com/> |

### Week 10 Achievements:

* Mastered AWS WAF for web application security:
  * Understand AWS WAF concepts and architecture
  * Master common web vulnerabilities (OWASP Top 10): SQL Injection, XSS, CSRF, etc.
  * Understand Web ACL, Rules, and Rule Groups
  * Created S3 bucket and deployed sample vulnerable web app (OWASP Juice Shop)
  * Tested and identified security vulnerabilities in application
  * Successfully created Web ACL from WAF console and associated with CloudFront/ALB
  * Properly configured Web ACL settings
  * Implemented managed rules from AWS Managed Rules
  * Configured rate-based rules for DDoS protection
  * Tested rules against sample attacks and verified blocking

* Mastered custom WAF rules and advanced configuration:
  * Created custom rules for specific threats
  * Implemented SQL injection protection rules
  * Configured XSS (Cross-Site Scripting) prevention rules
  * Tested custom rules with attack simulations and penetration testing
  * Created advanced custom rules with complex conditions
  * Configured rule priority and actions (Allow, Block, Count)
  * Implemented IP set rules for blacklist/whitelist
  * Tested comprehensive rule set with real-world scenarios
  * Custom rules successfully protecting against SQL injection and XSS attacks
  * Rule priority optimized for performance

* Implemented WAF logging and monitoring:
  * Enabled WAF logging to S3 bucket and CloudWatch Logs
  * Configured request sampling to analyze traffic patterns
  * Analyzed WAF logs to identify attack patterns
  * Reviewed blocked and allowed requests
  * Fine-tuned rules based on actual traffic and logs
  * Configured CloudWatch alarms for WAF metrics (blocked requests, rate limits)
  * Monitored WAF effectiveness and adjusted rules
  * Documented complete WAF configuration, rules, and testing results
  * WAF protection working effectively against common web attacks

* Mastered Resource Tagging and Resource Groups:
  * Researched and designed comprehensive resource tagging strategy
  * Understand tagging best practices and naming conventions
  * Tag categories: Environment (Dev/Test/Prod), CostCenter, Project, Owner, Schedule
  * Understand tag-based cost allocation and billing
  * Prepared EC2 instances, EBS volumes, and other resources for tagging
  * Tagged resources using AWS Console (point-and-click)
  * Tagged resources using AWS CLI (bulk operations)
  * Wrote scripts for automated tagging
  * Updated and deleted tags via Console and CLI
  * Filtered resources by tags in AWS Console
  * Searched and organized tagged resources efficiently
  * Mastered AWS CLI tagging operations

* Used Resource Groups for resource management:
  * Created Resource Groups based on tag queries
  * Configured Resource Groups with complex tag filters
  * Used Resource Groups to group related resources
  * Tested Resource Groups functionality for bulk operations
  * Monitored resources in groups
  * Resource Groups help organize and manage resources efficiently
  * Achieved efficient resource organization

* Implemented IAM tag-based access control (ABAC):
  * Researched IAM attribute-based access control (ABAC)
  * Understand tag-based IAM policies
  * Created IAM users for testing scenarios
  * Designed IAM policies based on resource tags
  * Created IAM policy allowing access only to resources with specific tags
  * Implemented tag-based permissions for EC2 operations (Start, Stop, Terminate)
  * Tested IAM policies with different users and scenarios
  * Verified access control: users can only access tagged resources
  * Enforced tagging requirements via IAM policies
  * Tag-based IAM policies working correctly
  * Documented tag-based security model and best practices
  * Understand how to scale security with tags in large environments
