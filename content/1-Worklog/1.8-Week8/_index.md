---
title: "Week 8 Worklog"
date: 2024-01-01
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---
### Week 8 Objectives:

* Deploy AWS Transit Gateway to connect multiple VPCs in hub-and-spoke architecture.
* Optimize EC2 costs with Lambda automation for scheduled instance start/stop.
* Implement resource tagging strategy and EventBridge scheduling.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Research AWS Transit Gateway architecture and use cases<br>- Compare Transit Gateway vs VPC Peering<br>- Create Transit Gateway and configure settings<br>- Attach VPCs to Transit Gateway | 06/08/2026 | 06/08/2026 | <https://000020.awsstudygroup.com/> |
| 3 | - Configure Transit Gateway route tables<br>- Test connectivity between multiple VPCs<br>- Launch EC2 instances and test inter-VPC communication<br>- Monitor Transit Gateway metrics on CloudWatch | 06/09/2026 | 06/09/2026 | <https://000020.awsstudygroup.com/> |
| 4 | - Research EC2 cost optimization strategies<br>- Learn about Lambda functions for automation<br>- Create IAM roles for Lambda execution<br>- Write Lambda function to stop EC2 instances | 06/10/2026 | 06/10/2026 | <https://000022.awsstudygroup.com/> |
| 5 | - Write Lambda function to start EC2 instances<br>- Implement resource tagging strategy<br>- Configure EventBridge rules for scheduled execution<br>- Test automated start/stop schedule | 06/11/2026 | 06/11/2026 | <https://000022.awsstudygroup.com/> |
| 6 | - Implement SNS notifications for Lambda executions<br>- Configure CloudWatch alarms for cost monitoring<br>- Create CloudWatch dashboard for cost tracking<br>- Document complete solution architecture | 06/12/2026 | 06/12/2026 | <https://000022.awsstudygroup.com/> |

### Week 8 Achievements:

* Mastered AWS Transit Gateway for multi-VPC networking:
  * Understand AWS Transit Gateway architecture and comparison with VPC Peering
  * Master route table propagation and associations
  * Successfully created Transit Gateway and configured settings
  * Attached 3 VPCs to Transit Gateway
  * Configured Transit Gateway route tables for inter-VPC routing
  * Set up automatic route propagation
  * Launched EC2 instances in VPCs and tested connectivity
  * All VPCs can communicate via Transit Gateway
  * Monitored Transit Gateway metrics and traffic on CloudWatch
  * Implemented Transit Gateway Network Manager (optional)
  * Mastered complex networking architecture with Transit Gateway

* Optimized EC2 costs with Lambda automation:
  * Understand EC2 cost optimization methods (right-sizing, scheduling, Savings Plans)
  * Learn about Lambda functions for infrastructure automation
  * Master resource tagging best practices (Environment, Schedule, CostCenter)
  * Created IAM roles with appropriate permissions for Lambda execution
  * Wrote Lambda function to stop EC2 instances based on tags
  * Wrote Lambda function to start EC2 instances on schedule
  * Implemented resource tagging strategy for EC2 instances
  * Configured EventBridge (CloudWatch Events) rules for scheduled execution
  * Set up cron expressions for business hours (weekdays only)
  * Tested automated start/stop schedule working correctly
  * Lambda functions filtering instances based on tags
  * Monitored Lambda execution logs and troubleshooting

* Monitoring and Notifications for cost optimization:
  * Implemented SNS notifications for Lambda execution results
  * Subscribed email endpoints for alerts
  * Configured CloudWatch alarms for cost monitoring
  * Created CloudWatch dashboard displaying cost metrics and instance states
  * Email notifications working when instances start/stop
  * Calculated cost savings from automation solution
  * Documented complete solution architecture and ROI
  * Completed automated and scalable cost optimization solution
