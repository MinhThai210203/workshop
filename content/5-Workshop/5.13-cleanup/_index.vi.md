---
title: "Dọn dẹp tài nguyên"
date: 2024-01-01
weight: 13
chapter: false
pre: " <b> 5.13. </b> "
---

#### Tại sao cần dọn dẹp?

Sau khi hoàn thành workshop, bạn nên dọn dẹp tài nguyên để:
- Tránh phí không mong muốn
- Giữ AWS account sạch sẽ
- Học cách quản lý lifecycle resources


#### Thứ tự dọn dẹp

### 1. Xóa CloudFront Distribution

- CloudFront → Distributions
- Chọn `itcoach-distribution`
- **Disable** distribution trước (chờ 5-10 phút)
- Sau khi disabled → **Delete**


### 2. Xóa API Gateway

- API Gateway → APIs
- Chọn `itcoach-api`
- **Actions** → **Delete API**
- Xác nhận xóa


### 3. Xóa Lambda Functions (8 functions)

- Lambda → Functions
- Chọn từng function → **Actions** → **Delete**
- Lặp lại cho 8 functions


### 4. Xóa SQS Queues (2 queues)

- SQS → Queues
- Chọn `itcoach-processing-queue` → **Delete**
- Chọn `itcoach-dlq` → **Delete**


### 5. Xóa Cognito User Pool

- Cognito → User pools
- Chọn user pool → **Delete**
- Nhập tên pool để xác nhận


### 6. Xóa DynamoDB Tables (8 tables)

- DynamoDB → Tables
- Chọn từng table → **Delete**
- Lặp lại cho 8 tables



### 7. Xóa S3 Buckets (2 buckets)

**Quan trọng:** Phải **empty bucket trước** khi xóa

- S3 → Buckets
- Chọn `itcoach-static-assets`
- **Empty** bucket (xóa tất cả objects)
- Sau khi empty → **Delete** bucket
- Lặp lại cho `itcoach-audio-upload`



### 8. Xóa IAM Role

- IAM → Roles
- Tìm `itcoach-lambda-role`
- **Delete** role


### 9. Xóa SNS Topic và Subscription

- SNS → Topics
- Chọn `itcoach-alerts` → **Delete**
- Subscriptions sẽ tự động bị xóa


### 10. Xóa CloudWatch Alarms (nếu đã tạo)

- CloudWatch → Alarms
- Chọn tất cả alarms liên quan → **Delete**

#### Checklist Cleanup

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

#### Xác nhận đã dọn dẹp xong

Kiểm tra lại từng service để đảm bảo không còn resources:

```
✅ CloudFront: 0 distributions
✅ API Gateway: 0 APIs
✅ Lambda: 0 functions (trừ functions khác của bạn)
✅ SQS: 0 queues liên quan
✅ Cognito: 0 user pools liên quan
✅ DynamoDB: 0 tables liên quan
✅ S3: 0 buckets liên quan
✅ IAM: Role itcoach-lambda-role đã xóa
✅ SNS: Topic itcoach-alerts đã xóa
```

#### Kết luận

Chúc mừng! Bạn đã hoàn thành workshop ITCoach trên AWS Serverless! 🎉

Những gì bạn đã học:
- ✅ Thiết lập IAM roles và permissions
- ✅ Cấu hình S3 cho static hosting và private storage
- ✅ Tạo và quản lý 8 bảng DynamoDB
- ✅ Xác thực người dùng với Cognito
- ✅ Xử lý bất đồng bộ với SQS
- ✅ Xây dựng 8 Lambda functions serverless
- ✅ Tạo REST API với API Gateway
- ✅ Phân phối CDN toàn cầu với CloudFront
- ✅ Monitoring với CloudWatch và SNS
- ✅ Clean up resources đúng cách

**Kiến thức này có thể áp dụng cho nhiều dự án Serverless khác!**

