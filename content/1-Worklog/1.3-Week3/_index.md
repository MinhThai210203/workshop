---
title: "Week 3 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.3. </b> "
---
### Week 3 Objectives:

* Introduction to Amazon EC2 and its fundamental concepts.
* Learn about instance types, AMI, EBS volumes, and Elastic IP.
* Practice launching, connecting to, and managing EC2 instances.
* Learn and practice deploying Node.js applications on EC2.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| Mon | - Learn Amazon EC2 fundamentals<br>- Instance Types (T2, T3, M5, C5...)<br>- AMI (Amazon Machine Images)<br>- EBS volumes and storage options | 05/05/2026 | 05/05/2026 | <https://000004.awsstudygroup.com/> |
| Tue | - Create Linux EC2 instance (Amazon Linux 2023)<br>- SSH connection with key pair<br>- Configure Security Groups<br>- Install and configure Node.js on Linux | 05/06/2026 | 05/06/2026 | <https://000004.awsstudygroup.com/> |
| Wed | - Deploy Node.js application on Linux<br>- Install MySQL database<br>- Setup PM2 for process management<br>- Configure Nginx as reverse proxy | 05/07/2026 | 05/07/2026 | <https://000004.awsstudygroup.com/> |
| Thu | - Create Windows Server 2025 EC2 instance<br>- RDP connection (Remote Desktop)<br>- Install Git, VS Code, Node.js on Windows<br>- Configure Windows Firewall | 05/08/2026 | 05/08/2026 | <https://000004.awsstudygroup.com/> |
| Fri | - Deploy Node.js application on Windows<br>- Install MySQL on Windows Server<br>- Test CRUD operations<br>- Compare Linux vs Windows deployment | 05/09/2026 | 05/09/2026 | <https://000004.awsstudygroup.com/> |

### Week 3 Achievements:

* Understood Amazon EC2 fundamentals and instance types:
  * General Purpose (T2, T3, M5) - balanced compute, memory, networking
  * Compute Optimized (C5, C6) - high-performance processors
  * Memory Optimized (R5, X1) - fast performance for large datasets
  * Storage Optimized (I3, D2) - high sequential I/O

* Mastered EC2 Pricing Models for cost optimization:
  * On-Demand - pay per hour/second, no commitment
  * Reserved Instances - 1 or 3 year commitment, up to 75% discount
  * Spot Instances - up to 90% discount, can be interrupted
  * Savings Plans - flexible pricing model

* Proficient with AMI (Amazon Machine Images):
  * Pre-configured instance templates
  * Custom AMI creation for reusability
  * AMI sharing and marketplace
  * AMI lifecycle management

* Successfully deployed Node.js application on Linux EC2:
  * Launched Amazon Linux 2023 instance
  * Configured Security Groups (SSH port 22, HTTP port 80, custom app port)
  * Connected via SSH using PEM key pair
  * Set up Elastic IP for static public IP
  * Installed Node.js, npm, and Git
  * Cloned AWS FCJ User Management application (Node.js + Express)
  * Configured MySQL database connection
  * Set up Express-Handlebars for templating
  * Implemented CRUD operations (Create, Read, Update, Delete users)
  * Installed PM2 for process management and auto-restart
  * Configured PM2 startup script for system boot
  * Set up Nginx as reverse proxy
  * Implemented logging and monitoring

* Successfully deployed Node.js application on Windows EC2:
  * Launched Windows Server 2025 instance
  * Connected via RDP (Remote Desktop Protocol)
  * Configured Windows Firewall rules and Security Groups for RDP port 3389
  * Installed Git for Windows, Visual Studio Code, Node.js runtime
  * Configured PATH environment variables
  * Cloned application repository and installed npm packages
  * Configured MySQL database on Windows
  * Deployed Node.js application with PM2-Windows or node-windows
  * Tested application functionality

* Compared Linux vs Windows deployment:
  * Linux: Lightweight, better performance, lower cost, suitable for production workloads
  * Windows: Familiar GUI, .NET integration, enterprise tools
  * Both: Full Node.js support, production-ready
  * Best practices: Choose based on team expertise and workload requirements
