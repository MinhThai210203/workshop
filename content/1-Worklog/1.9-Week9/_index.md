---
title: "Week 9 Worklog"
date: 2024-01-01
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---
### Week 9 Objectives:

* Deploy complete CI/CD pipeline with AWS CodePipeline, CodeBuild, and CodeDeploy.
* Configure Git integration with AWS CodeCommit and automated deployment workflows.
* Implement hybrid storage solution with AWS Storage Gateway for on-premises integration.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Research AWS CI/CD services ecosystem<br>- Prepare infrastructure: VPC, Security Groups, S3 bucket<br>- Create IAM roles for CI/CD services<br>- Install and configure CodeDeploy Agent on EC2 | 06/15/2026 | 06/15/2026 | <https://000023.awsstudygroup.com/> |
| 3 | - Create AWS CodeCommit repository<br>- Configure Git credentials for HTTPS connections<br>- Clone repository and push sample application code<br>- Configure service roles for CodePipeline | 06/16/2026 | 06/16/2026 | <https://000023.awsstudygroup.com/> |
| 4 | - Create CodeBuild project with buildspec.yml<br>- Write buildspec.yml for Node.js application<br>- Create CodeDeploy application and deployment groups<br>- Configure appspec.yml and test manual deployment | 06/17/2026 | 06/17/2026 | <https://000023.awsstudygroup.com/> |
| 5 | - Create CodePipeline with 3 stages: Source, Build, Deploy<br>- Test end-to-end CI/CD pipeline<br>- Commit code changes and watch automatic deployment<br>- Monitor pipeline execution and troubleshoot | 06/18/2026 | 06/18/2026 | <https://000023.awsstudygroup.com/> |
| 6 | - Learn AWS Storage Gateway types and use cases<br>- Create S3 bucket for File Gateway storage<br>- Launch EC2 instance with AMI Storage Gateway<br>- Configure Storage Gateway and create file shares | 06/19/2026 | 06/20/2026 | <https://000024.awsstudygroup.com/> |

### Week 9 Achievements:

* Mastered AWS CI/CD services for application deployment:
  * Understand AWS CI/CD services ecosystem: CodePipeline, CodeBuild, CodeDeploy, CodeCommit
  * Compared AWS CodeCommit vs GitHub vs GitLab
  * Fully prepared infrastructure: VPC, Security Groups, S3 bucket for artifacts
  * Created IAM roles and policies for all CI/CD services
  * Set up EC2 instances with appropriate IAM instance profile
  * Successfully installed and configured CodeDeploy Agent on EC2
  * CodeDeploy Agent working and can receive deployments

* Mastered AWS CodeCommit and Git integration:
  * Successfully created AWS CodeCommit repository
  * Configured Git credentials for HTTPS connections
  * Cloned repository and pushed sample Node.js application code
  * Set up Git connection from local machine
  * Created branches and tested Git workflow
  * Migrated repository to GitLab/GitHub (optional practice)
  * Configured service roles for CodePipeline to access CodeCommit
  * Set up IAM users with appropriate Git permissions

* Deployed CodeBuild and CodeDeploy:
  * Created CodeBuild project with build environment configuration
  * Wrote buildspec.yml for Node.js application (install, build, artifacts)
  * Tested CodeBuild manually and reviewed build logs
  * Troubleshooted build failures
  * Created CodeDeploy application and deployment groups
  * Configured appspec.yml file with deployment hooks
  * Set up deployment configuration (AllAtOnce, HalfAtATime, OneAtATime)
  * Successfully tested manual deployment with CodeDeploy
  * CodeBuild and CodeDeploy working independently

* Completed CI/CD Pipeline with CodePipeline:
  * Created CodePipeline with 3 stages: Source (CodeCommit), Build (CodeBuild), Deploy (CodeDeploy)
  * Configured pipeline settings and service role
  * Linked all services together in pipeline
  * Successfully tested end-to-end CI/CD pipeline
  * Committed code changes and watched automatic deployment
  * Monitored pipeline execution from source to production
  * Troubleshooted failed deployments and implemented rollback strategies
  * Complete CI/CD pipeline working automatically, code changes deployed automatically
  * Understand best practices for CI/CD on AWS

* Deployed AWS Storage Gateway for hybrid storage:
  * Researched AWS Storage Gateway types (File Gateway, Volume Gateway, Tape Gateway)
  * Understand File Gateway architecture and use cases
  * Hybrid cloud storage strategies
  * Created S3 bucket for File Gateway storage backend
  * Launched EC2 instance with AMI Storage Gateway provided by AWS
  * Configured Storage Gateway and activated
  * Successfully created File Gateway
  * Set up SMB/NFS file shares
  * Configured guest access settings and permissions
  * Mounted file share on on-premises machine (Windows/Linux)
  * Tested file operations: upload, download, modify
  * Verified files automatically synced to S3
  * Files working seamlessly between on-premises and cloud storage
  * Monitored Storage Gateway metrics on CloudWatch
  * Completed hybrid storage solution
