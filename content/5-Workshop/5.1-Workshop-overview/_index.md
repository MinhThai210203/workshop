---
title: "Introduction"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 5.1. </b> "
---

#### Introduction to ITCoach

ITCoach is an AI-powered intelligent IT interview practice platform that helps IT students and entry-level professionals develop real interview skills. The platform is built entirely on AWS Serverless architecture, ensuring:

- **No server management**: Lambda automatically processes and scales
- **Low cost**: Pay-per-use, only pay when used
- **High performance**: CloudFront global distribution
- **Strong security**: Cognito and IAM access management

#### Key Features

**1. Diverse practice formats:**
- Multiple-choice quizzes with Spaced Repetition SM-2
- Essay text input or voice recording
- Real interview simulation with AI

**2. Smart AI evaluation:**
- OpenAI API converts speech to text
- AI scores and provides detailed feedback
- Amazon Polly reads feedback with voice

**3. Gamification:**
- XP, level, badge system
- Continuous learning streaks
- Competitive leaderboard

**4. Personal dashboard:**
- Track learning progress
- Analyze weaknesses
- Recommend priority review content

#### System Architecture

In this workshop, you will build a system with the following components:

- **Frontend**: ReactJS on S3 + CloudFront
- **Backend**: 8 Lambda functions
- **Database**: 8 DynamoDB tables
- **Authentication**: Amazon Cognito
- **Message Queue**: Amazon SQS
- **DNS & SSL**: Route 53 + ACM
- **Monitoring**: CloudWatch + SNS

![ITCoach Architecture](/images/5-Workshop/5.1-overview/architecture.png)

#### Main Processing Flow

```
User (Browser)
    ↓ HTTPS – itcoach24h.xyz
Amazon Route 53 (DNS)
    ↓
Amazon CloudFront (CDN) ←→ S3 Static (ReactJS)
    ↓
Amazon API Gateway (8 endpoints, Throttling: 100 req/s)
    ↓ Cognito Authorizer
AWS Lambda (8 functions)
    ├──→ DynamoDB (8 tables)
    ├──→ S3 Audio (Presigned URL)
    ├──→ SQS (Async Processing)
    │      ↓
    │   itcoach-ai-processor
    │      ├──→ OpenAI API (STT + Evaluation)
    │      └──→ Amazon Polly (Text-to-Speech)
    └──→ CloudWatch → SNS (Alerts)
```

#### Estimated Time

- **AWS infrastructure setup**: 1-2 hours
- **Code deployment (after development)**: 30 minutes
- **Testing and verification**: 30 minutes

**Total time**: 2-3 hours

