---
title: "Week 4 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.4. </b> "
---
### Week 4 Objectives:

* Learn and build exercises for Amazon RDS managed database service.
* Deploy Auto Scaling to automatically scale EC2 instances based on demand.
* Monitor resources and set up CloudWatch alarms for performance metrics.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| Mon | - Learn Amazon RDS fundamentals<br>- RDS engine types (MySQL, PostgreSQL, Oracle...)<br>- Create RDS database instance<br>- Configure DB subnet groups and security groups | 05/11/2026 | 05/11/2026 | <https://000005.awsstudygroup.com/> |
| Tue | - Connect EC2 with RDS database<br>- Deploy application with RDS backend<br>- Deploy application using RDS<br>- Backup and restore data | 05/12/2026 | 05/12/2026 | <https://000005.awsstudygroup.com/> |
| Wed | - Learn Auto Scaling with Elastic Load Balancing<br>- Prepare multi-AZ environment setup<br>- Create Launch Template for EC2<br>- Set up Load Balancer and Target Groups | 05/13/2026 | 05/13/2026 | <https://000006.awsstudygroup.com/> |
| Thu | - Create Auto Scaling Group<br>- Configure scaling policies<br>- Test Auto Scaling results<br>- Test health checks and failover | 05/14/2026 | 05/14/2026 | <https://000006.awsstudygroup.com/> |
| Fri | - Research Amazon CloudWatch<br>- Learn CloudWatch Metrics, Logs, Alarms<br>- Create custom metrics and dashboards<br>- Setup monitoring for EC2 and RDS | 05/15/2026 | 05/15/2026 | <https://000008.awsstudygroup.com/> |

### Week 4 Achievements:

* Understood Amazon RDS (Relational Database Service) - managed database service:
  * Engine types: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server
  * Multi-AZ deployments for high availability
  * Read Replicas for read scaling
  * Automated backups and retention periods
  * Manual snapshots
  * Point-in-time recovery

* Successfully deployed RDS MySQL instance:
  * Created VPC and subnets for RDS
  * Configured DB subnet groups
  * Created security groups for database access
  * Launched RDS MySQL instance
  * Configured parameter groups
  * Connected EC2 instance with RDS
  * Deployed AWS FCJ Management application with RDS backend
  * Configured connection strings and environment variables
  * Tested CRUD operations with database
  * Restored database from snapshot

**Screenshots from Amazon RDS Workshop:**

![RDS Setup](/images/khong5.png)

![RDS Configuration](/images/khong51.png)

![RDS Database Instance](/images/khong52.png)

![RDS Application Integration](/images/khong53.png)

* Deployed Auto Scaling and Elastic Load Balancing:
  * Application Load Balancer (ALB) fundamentals
  * Target Groups and health checks
  * Listener rules and routing
  * Cross-zone load balancing
  * Created Launch Template with AMI, instance type, security groups
  * User data scripts for bootstrapping
  * Template versioning
  * Created Auto Scaling Group with launch template
  * Configured desired, minimum, maximum capacity
  * Health check types (EC2, ELB)
  * Instance warm-up time
  * Target tracking scaling (CPU utilization)
  * Step scaling policies and Simple scaling policies
  * Scaling cooldowns

**Screenshots from Auto Scaling & ELB Workshop:**

![Auto Scaling Setup](/images/khongsau.png)

![Load Balancer Configuration](/images/khongsau1.png)

![Auto Scaling Group](/images/khongsau2.png)

![Scaling Policy Testing](/images/khongsau3.png)

* Mastered Amazon CloudWatch monitoring and alerting:
  * Built-in metrics for EC2, RDS, ALB
  * Custom metrics with PutMetricData
  * Metric math and statistics
  * Metric filters for logs
  * Log groups and log streams
  * CloudWatch Logs Agent installation
  * Log retention policies
  * Log insights queries
  * Created alarms based on metrics
  * Alarm states (OK, ALARM, INSUFFICIENT_DATA)
  * SNS notifications
  * Alarm actions (Auto Scaling, EC2, SNS)
  * Created custom dashboards
  * Widget types (line, stacked area, number)
  * Cross-region dashboards
  * Dashboard sharing
