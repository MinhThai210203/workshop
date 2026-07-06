---
title: "Week 6 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.6. </b> "
---
### Week 6 Objectives:

* Learn and deploy applications on Docker containers with AWS.
* Research and work with Amazon Elastic Container Service (ECS).
* Configure ECS clusters, task definitions, services, and load balancing.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| Mon | - Learn Docker fundamentals<br>- Understand Docker images, containers, Dockerfile<br>- Prepare VPC, Security Group, IAM for ECR access<br>- Login to Docker Hub | 05/25/2026 | 05/25/2026 | <https://000015.awsstudygroup.com/> |
| Tue | - Create and launch EC2 instance<br>- Install Docker on EC2<br>- Configure EC2 on instance<br>- Install libraries and dependencies | 05/26/2026 | 05/26/2026 | <https://000015.awsstudygroup.com/> |
| Wed | - Create and launch RDS database instance<br>- Deploy Docker Image, Docker Compose<br>- Push Image using Docker Hub and Amazon ECR<br>- Clean up resources | 05/27/2026 | 05/27/2026 | <https://000015.awsstudygroup.com/> |
| Thu | - Research Amazon Elastic Container Service (ECS)<br>- Learn ECS concepts: Clusters, Tasks, Services<br>- Prepare infrastructure configuration<br>- Role CodeDeploy, NAT gateway, Route Table, Security Group | 05/28/2026 | 05/28/2026 | <https://000016.awsstudygroup.com/> |
| Fri | - Add Subnet, prepare to deploy Docker image to ECR and Dockerhub<br>- Register namespace in Cloud Map<br>- Create ECS Cluster, Task Definition<br>- Configure Application Load Balancer, Target Group<br>- Create ECS Service, Blue/Green deployment, Rolling update | 05/29/2026 | 05/29/2026 | <https://000016.awsstudygroup.com/> |

### Week 6 Achievements:

* Understood Docker containerization and benefits vs VMs:
  * Docker architecture: Docker Engine, Docker Client, Docker Daemon
  * Images vs Containers
  * Docker Hub registry
  * Dockerfile syntax and best practices
  * Installed Docker on Amazon Linux 2023
  * Docker commands: pull, run, build, push, ps, stop, rm
  * Docker networking modes
  * Volume mounting for persistent data
  * Multi-stage builds for optimization
  * Environment variables in Docker
  * COPY vs ADD commands
  * ENTRYPOINT vs CMD
  * Docker layer caching

* Deployed multi-container application with Docker Compose:
  * Created VPC with public/private subnets
  * Configured Security Groups for Docker containers
  * IAM roles for ECR access
  * EC2 instance with Docker installed
  * docker-compose.yml configuration
  * Multi-container applications
  * Service dependencies
  * Networks and volumes in Compose
  * Environment variables management
  * Pushed/pulled images from Docker Hub (Public vs private repositories)
  * Image tagging strategies
  * Created ECR repositories
  * ECR authentication with Docker
  * Pushed images to ECR
  * Image scanning for vulnerabilities
  * Lifecycle policies

* Deployed Amazon Elastic Container Service (ECS):
  * ECS Clusters (EC2 vs Fargate launch types)
  * Task Definitions (container specifications)
  * ECS Tasks (running instances of Task Definitions)
  * ECS Services (maintaining desired task count)
  * Service Discovery with AWS Cloud Map
  * Created ECS Cluster with EC2 launch type
  * Container instances registration
  * Capacity providers configuration
  * Cluster auto-scaling
  * Container definitions (image, CPU, memory)
  * Port mappings
  * Environment variables
  * IAM task roles vs execution roles
  * Task networking modes (bridge, awsvpc, host)
  * Volume mounts (EFS, bind mounts)
  * Service creation with desired count
  * Load balancer integration (ALB/NLB)
  * Target Group configuration
  * Health check settings
  * Service auto-scaling policies

* Mastered ECS Deployment Strategies:
  * Rolling Update - Minimum healthy percent, Maximum percent, Deployment circuit breaker
  * Blue/Green Deployment - AWS CodeDeploy integration
  * Traffic shifting strategies (Linear, Canary, All-at-once)
  * Automatic rollback capabilities
  * CloudWatch alarms for deployment monitoring
  * Service Discovery with Cloud Map
  * ECS Exec for container debugging
  * Container Insights monitoring
  * Task placement strategies
  * Secrets management with AWS Secrets Manager
