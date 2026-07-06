---
title: "Workshop"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Building ITCoach Platform with AWS Serverless

#### Overview

**ITCoach** is an intelligent IT interview practice platform powered by AI, built entirely on AWS Serverless architecture. In this workshop, you will learn how to set up each component of the system from scratch using AWS Console.

The system includes:
- **Frontend**: ReactJS distributed via CloudFront and S3
- **Backend**: 8 Lambda functions for business logic
- **Database**: 8 DynamoDB tables for data storage
- **Authentication**: Amazon Cognito for user management
- **AI Integration**: OpenAI API and Amazon Polly
- **Async Processing**: SQS for heavy task processing
- **Monitoring**: CloudWatch and SNS

#### Content

1. [Workshop Overview](5.1-Workshop-overview/)
2. [Prerequisites](5.2-Prerequiste/)
3. [Setting up IAM Role](5.3-iam-role/)
4. [Creating S3 Buckets](5.4-s3-buckets/)
5. [Creating DynamoDB Tables](5.5-dynamodb/)
6. [Configuring Amazon Cognito](5.6-cognito/)
7. [Setting up Amazon SQS](5.7-sqs/)
8. [Creating Lambda Functions](5.8-lambda/)
9. [Configuring API Gateway](5.9-api-gateway/)
10. [Setting up CloudFront](5.10-cloudfront/)
11. [Configuring Route 53 and SSL](5.11-route53-ssl/)
12. [Monitoring with CloudWatch](5.12-monitoring/)
13. [Cleaning up Resources](5.13-cleanup/)
