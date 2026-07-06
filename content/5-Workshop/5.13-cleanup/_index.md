---
title: "Cleaning up Resources"
date: 2024-01-01
weight: 13
chapter: false
pre: " <b> 5.13. </b> "
---

#### Why cleanup?

After completing the workshop, you should clean up resources to:
- Avoid unexpected charges
- Keep AWS account clean
- Learn how to manage resource lifecycle


#### Cleanup Order

### 1. Delete CloudFront Distribution

- CloudFront → Distributions
- Select `itcoach-distribution`
- **Disable** distribution first (wait 5-10 minutes)
- After disabled → **Delete**


### 2. Delete API Gateway

- API Gateway → APIs
- Select `itcoach-api`
- **Actions** → **Delete API**
- Confirm deletion


### 3. Delete Lambda Functions (8 functions)

- Lambda → Functions
- Select each function → **Actions** → **Delete**
- Repeat for all 8 functions


### 4. Delete SQS Queues (2 queues)

- SQS → Queues
- Select `itcoach-processing-queue` → **Delete**
- Select `itcoach-dlq` → **Delete**


### 5. Delete Cognito User Pool

- Cognito → User pools
- Select user pool → **Delete**
- Enter pool name to confirm


### 6. Delete DynamoDB Tables (8 tables)

- DynamoDB → Tables
- Select each table → **Delete**
- Repeat for all 8 tables



### 7. Delete S3 Buckets (2 buckets)

**Important:** Must **empty bucket first** before deleting

- S3 → Buckets
- Select `itcoach-static-assets`
- **Empty** bucket (delete all objects)
- After empty → **Delete** bucket
- Repeat for `itcoach-audio-upload`



### 8. Delete IAM Role

- IAM → Roles
- Find `itcoach-lambda-role`
- **Delete** role


### 9. Delete SNS Topic and Subscription

- SNS → Topics
- Select `itcoach-alerts` → **Delete**
- Subscriptions will be automatically deleted


### 10. Delete CloudWatch Alarms (if created)

- CloudWatch → Alarms
- Select all related alarms → **Delete**

#### Cleanup Checklist

| # | Resource | Status |
|---|----------|--------|
| 1 | CloudFront Distribution | ⬜ |
| 2 | API Gateway | ⬜ |
| 3 | Lambda Functions (8) | ⬜ |
| 4 | SQS Queues (2) | ⬜ |
| 5 | Cognito User Pool | ⬜ |
| 6 | DynamoDB Tables (8) | ⬜ |
| 7 | S3 Buckets (2) | ⬜ |
| 8 | IAM Role | ⬜ |
| 9 | SNS Topic | ⬜ |
| 10 | CloudWatch Alarms | ⬜ |

#### Verify Cleanup Complete

Check each service to ensure no remaining resources:

```
✅ CloudFront: 0 distributions
✅ API Gateway: 0 APIs
✅ Lambda: 0 functions (except your other functions)
✅ SQS: 0 related queues
✅ Cognito: 0 related user pools
✅ DynamoDB: 0 related tables
✅ S3: 0 related buckets
✅ IAM: Role itcoach-lambda-role deleted
✅ SNS: Topic itcoach-alerts deleted
```

#### Conclusion

Congratulations! You have completed the ITCoach workshop on AWS Serverless! 🎉

What you have learned:
- ✅ Set up IAM roles and permissions
- ✅ Configure S3 for static hosting and private storage
- ✅ Create and manage 8 DynamoDB tables
- ✅ User authentication with Cognito
- ✅ Asynchronous processing with SQS
- ✅ Build 8 serverless Lambda functions
- ✅ Create REST API with API Gateway
- ✅ Global CDN distribution with CloudFront
- ✅ Monitoring with CloudWatch and SNS
- ✅ Proper resource cleanup

**This knowledge can be applied to many other Serverless projects!**
