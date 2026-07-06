---
title: "Proposal"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# ITCoach – AI-Powered IT Interview Practice Platform
## AWS Serverless Solution for IT Students' Interview Skills Training

## 1. Executive Summary

ITCoach is a web platform that helps IT students and entry-level professionals practice technical knowledge, develop interview response skills, and simulate real interview environments with AI support. The goal is to help students increase their chances of passing Internship, Fresher, and Junior recruitment rounds at technology companies.

The platform supports diverse practice formats: single or multiple-choice quizzes with Spaced Repetition (SM-2) mechanism, essay-style text or voice recording answers, and simulated real interview sessions where AI asks questions using voice. AI provides detailed evaluation for each answer, points out gaps, suggests improvements, and responds with voice feedback via Amazon Polly. A Gamification system with XP, levels, streaks, and leaderboards helps increase learning motivation.

The system is built entirely on Amazon Web Services using Serverless Architecture. The frontend uses ReactJS distributed via Amazon CloudFront, backend processing by AWS Lambda, data storage on Amazon DynamoDB, and integrates OpenAI API for answer evaluation and Amazon Polly for voice generation.

## 2. Problem Statement

### Current Issues

IT students and entry-level professionals often lack realistic interview practice environments:

- Traditional quiz websites only test theory, do not evaluate articulation ability
- No tools evaluate essay or voice answers with detailed AI feedback
- No environment simulates real interviews by specialty and level
- Difficult to identify personal weaknesses to focus practice efforts properly
- Foreign platforms have language barriers, high costs, inadequate fit for Vietnamese IT market

### Solution

ITCoach addresses these issues with core features:

- **Multi-specialty Question Bank:** 11 IT specialties, each divided into multiple topics
- **Smart Quizzes:** Single or multiple-choice quizzes applying Spaced Repetition SM-2 for optimal review timing
- **Multi-format Essays:** Text input or voice recording, AI evaluates and provides detailed feedback
- **Real Interview Simulation:** Select specialty, level, duration – AI conducts voice-guided interview
- **Personal Dashboard:** Track progress, analyze weaknesses, recommend priority review content
- **Gamification:** XP, level, badges, streaks, leaderboards to increase learning motivation

### AWS Infrastructure

- **Amazon CloudFront + S3** distributes ReactJS globally at high speed
- **Amazon Cognito** secures user authentication
- **Amazon API Gateway + AWS Lambda** processes all serverless business logic
- **Amazon DynamoDB** stores all system data (8 tables)
- **Amazon S3 (Audio)** stores audio recordings and Polly audio via Presigned URL
- **Amazon SQS** asynchronously processes heavy AI tasks
- **OpenAI API** Speech-to-Text + answer quality evaluation
- **Amazon Polly** reads questions and responds with voice feedback
- **Amazon CloudWatch + SNS** monitors system and sends automatic alerts
- **Amazon Route 53 + ACM** manages DNS and SSL certificate for domain `itcoach24h.xyz`

### Benefits and ROI

- Students have realistic IT interview practice environment with instant AI feedback like a mentor
- Spaced Repetition enables effective memorization, system automatically identifies individual weaknesses
- No server management needed, automatically scales to demand thanks to Serverless architecture
- Low operational costs, easy to add new specialties and questions in the future

## 3. Solution Architecture

The platform applies AWS Serverless architecture with AWS Lambda as the business logic processing center.

### Main Processing Flow

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
    ├──→ Amazon DynamoDB (8 tables)
    ├──→ Amazon S3 Audio (Presigned URL Upload)
    ├──→ Amazon SQS (Async Processing)
    │         ↓
    │    itcoach-ai-processor
    │         ├──→ OpenAI API (STT + AI Evaluation)
    │         └──→ Amazon Polly (Text-to-Speech)
    └──→ Amazon CloudWatch → Amazon SNS (Alerts)
```

### AWS Services Used

| Service | Purpose |
|---------|---------|
| Amazon CloudFront | CDN distributes ReactJS globally via HTTPS |
| Amazon S3 (Static) | Stores ReactJS build files |
| Amazon S3 (Audio) | Stores audio recordings and Polly audio files |
| Amazon API Gateway | 8 endpoints, integrates Cognito Authorizer, Throttling (100 req/s) |
| Amazon Cognito | Registration, login, user session management |
| AWS Lambda | 8 functions process all backend business logic |
| Amazon DynamoDB | 8 tables store all system data |
| Amazon SQS | Queue for asynchronous AI and audio processing |
| Amazon Polly | Reads questions and responds with voice feedback |
| OpenAI API | Speech-to-Text + answer quality evaluation |
| Amazon CloudWatch | Monitors logs, metrics, system performance |
| Amazon SNS | Sends email alerts when system errors occur |
| Amazon Route 53 | Manages DNS for domain `itcoach24h.xyz` |
| AWS ACM | Free SSL certificate for HTTPS |

## 4. Detailed Features

### 4.1. Target Users

- IT students in year 2, 3, or final year
- Students preparing for Internship/Fresher applications
- Career changers wanting to practice technical interviews
- Working professionals reviewing knowledge before interviews

### 4.2. Supported Specialties

| # | Specialty |
|---|-----------|
| 1 | Front-end Developer |
| 2 | Back-end Developer |
| 3 | Full-stack Developer |
| 4 | DevOps Engineer |
| 5 | Mobile Developer |
| 6 | QA/QC Engineer |
| 7 | Data Engineer |
| 8 | Data Analyst |
| 9 | AI/Machine Learning Engineer |
| 10 | Cyber Security |
| 11 | General IT Foundation Knowledge |

### 4.3. Practice Formats

**Quiz (Multiple Choice):**
- Single or multiple correct answers
- Spaced Repetition SM-2 algorithm automatically calculates `nextReviewDate` for optimal review timing
- Earn XP after each correct answer

**Essay:**
- Text input or voice recording
- OpenAI STT converts voice to text
- AI scores, points out missing ideas, suggests improvements, provides sample answers
- Polly reads feedback with voice

### 4.4. Mock Interview Module

- Select specialty, level (Intern/Fresher/Junior), duration (15/30/60 minutes)
- AI reads questions with voice (Polly)
- User responds with text or voice
- Overall evaluation after session: score per skill, areas to improve, sample answers

### 4.5. Dashboard & Gamification

- Learning progress by topic, completion rate, average score
- Weakness analysis, recommended priority review content
- Daily study streak, daily history
- XP, Level, Badge achievement system
- Weekly/monthly leaderboard

## 5. Technical Implementation

### Lambda Functions – 8 functions

| Function | Task |
|----------|------|
| `itcoach-auth-handler` | Registration, login, profile management |
| `itcoach-question-handler` | Retrieve essay questions + topic lists by specialty |
| `itcoach-session-handler` | Create and manage Mock Interview sessions |
| `itcoach-answer-handler` | Receive essay answers, create Presigned URL for audio upload |
| `itcoach-ai-processor` | OpenAI STT + evaluation + Polly TTS (async from SQS) |
| `itcoach-result-handler` | Return results, scores, history, dashboard statistics |
| `itcoach-quiz-handler` | Quiz multiple choice, SM-2, add XP to gamification |
| `itcoach-gamification-handler` | XP, level, streak, leaderboard management |

### DynamoDB – 8 tables

| Table | Partition Key | Sort Key | Index | Used For |
|-------|--------------|----------|-------|----------|
| `itcoach-users` | `userId` | - | - | User information |
| `itcoach-questions` | `questionId` | - | `category-index` | Quiz + Essay shared |
| `itcoach-sessions` | `sessionId` | - | `userId-index` | Mock Interview sessions |
| `itcoach-answers` | `answerId` | - | `sessionId-index` | Answers + AI feedback |
| `itcoach-history` | `userId` | `timestamp` | - | Learning history |
| `itcoach-topics` | `specialty` | `topicId` | - | Topics by specialty |
| `itcoach-quiz-attempts` | `userId` | `questionId` | - | Spaced Repetition SM-2 |
| `itcoach-gamification` | `userId` | - | `xp-index` | XP, level, streak, badge |

### API Gateway – 8 endpoints

| Endpoint | Method | Used For |
|----------|--------|----------|
| `/auth` | POST | Login/registration (public) |
| `/questions` | GET | Retrieve essay questions |
| `/topics` | GET | Retrieve topics by specialty |
| `/sessions` | POST | Create Mock Interview session |
| `/answers` | POST | Submit essay answer |
| `/results` | GET | View results + history |
| `/quiz` | POST | Submit quiz + Spaced Repetition |
| `/leaderboard` | GET | XP leaderboard |

## 6. Timeline & Milestones

### Phase 1 – Infrastructure & Backend
Build entire AWS infrastructure, write 8 Lambda functions, integrate OpenAI and Polly.

### Phase 2 – Frontend & Integration
Build ReactJS interface: auth, quiz, essay, recording, Mock Interview, dashboard, gamification.

### Phase 3 – Data & Finalization
Import question bank (prioritize Frontend, Backend, Foundation Knowledge), test entire flow, fix bugs, official deployment.

| Phase | Timeline | Content |
|-------|----------|---------|
| Preparation | Pre-internship | Design architecture, team assignment |
| Month 1 – Week 1–2 | Internship | Build AWS infrastructure |
| Month 1 – Week 3–4 | Internship | Backend dev: 8 Lambda + OpenAI + Polly |
| Month 2 – Week 1–2 | Internship | Frontend dev: auth, quiz, essay, recording |
| Month 2 – Week 3–4 | Internship | Frontend dev: Mock Interview, dashboard, gamification |
| Month 3 – Week 1–2 | Internship | Integration, testing, bug fixes |
| Month 3 – Week 3–4 | Internship | Import question data, deploy, demo |

## 7. Budget Estimation

### AWS Costs/month

| Service | Estimate | Notes |
|---------|---------|-------|
| AWS Lambda | ~$0.00 | Free tier 1M requests |
| Amazon DynamoDB | ~$0.00 | On-demand, free tier 25GB |
| Amazon S3 | ~$0.05 | Static + audio files |
| Amazon API Gateway | ~$0.01 | ~1,000 requests |
| Amazon CloudFront | $0.00 | Free plan |
| Amazon Cognito | $0.00 | Free tier 50,000 MAU |
| Amazon SQS | ~$0.00 | Free tier 1M requests |
| Amazon Polly | ~$0.04 | ~100,000 characters |
| Amazon SNS | ~$0.00 | Free tier |
| Amazon Route 53 | ~$0.50 | Hosted Zone $0.50/month |
| AWS ACM | $0.00 | Completely free |
| OpenAI API | ~$1–$5 | Depends on evaluation volume |
| **Total AWS** | **~$0.60/month** | |
| **Total with OpenAI** | **~$1.60–$5.60/month** | |

### One-time Costs

| Item | Cost |
|------|------|
| Domain `itcoach24h.xyz` (Namecheap) | ~$2–3/year |
| **First Year Total** | **~$22–70/year** |

### Cost Summary

- **Startup cost:** ~$2–3 (domain)
- **Monthly operational cost:** ~$1.60–$5.60
- **First year total:** ~$22–70 (including domain + 12 months operation)
- **From 2nd year onwards:** ~$20–$70/year (domain renewal + operation)

## 8. Risk Assessment

### Risk Matrix

| Risk | Impact | Probability | Solution |
|------|--------|------------|----------|
| OpenAI API rate limit / outage | High | Low | Cache results in DynamoDB |
| Question bank quality insufficient | High | Medium | Import data parallel to development |
| Lambda cold start slow | Medium | Medium | Optimize package size |
| OpenAI costs exceed budget | Medium | Medium | Set budget limits, optimize prompts |
| CORS or Cognito auth errors | Medium | Low | Test thoroughly in dev environment |

## 9. Expected Results

### Success Criteria
- ✅ Registration, login, quiz and essay practice work fully
- ✅ Recording, STT, AI evaluation and voice feedback work stably
- ✅ Spaced Repetition SM-2 automatically calculates review schedule correctly
- ✅ Mock Interview module runs complete flow from start to finish
- ✅ Dashboard, gamification, leaderboard display completely
- ✅ System stable, CloudWatch has no critical alarms

### Long-term Value
- Question bank accumulates, easy to add new specialties
- Personalized practice data, AI evaluation becomes increasingly accurate
- Serverless architecture easy to expand, reusable for future projects
- Team accumulates practical experience with AWS Serverless, AI integration, full-stack

*ITCoach – AI-Powered IT Interview Practice Platform on AWS*

*Serverless | ReactJS | 8 Lambda | 8 DynamoDB | 8 API Endpoints | OpenAI | Polly | Spaced Repetition SM-2*
