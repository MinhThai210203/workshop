---
title: "Giới thiệu"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 5.1. </b> "
---

#### Giới thiệu về ITCoach

ITCoach là nền tảng luyện phỏng vấn IT thông minh ứng dụng AI, giúp sinh viên IT và người mới đi làm rèn luyện kỹ năng phỏng vấn thực tế. Nền tảng được xây dựng hoàn toàn trên kiến trúc AWS Serverless, đảm bảo:

- **Không cần quản lý server**: Lambda tự động xử lý và mở rộng
- **Chi phí thấp**: Pay-per-use, chỉ trả tiền khi sử dụng
- **Hiệu năng cao**: CloudFront phân phối toàn cầu
- **Bảo mật tốt**: Cognito và IAM quản lý truy cập

#### Tính năng chính

**1. Đa dạng hình thức luyện tập:**
- Quiz trắc nghiệm với Spaced Repetition SM-2
- Tự luận nhập văn bản hoặc ghi âm giọng nói
- Mô phỏng phỏng vấn thực tế với AI

**2. AI đánh giá thông minh:**
- OpenAI API chuyển giọng nói thành text
- AI chấm điểm và đưa feedback chi tiết
- Amazon Polly đọc phản hồi bằng giọng nói

**3. Gamification:**
- Hệ thống XP, level, badge
- Streak học liên tục
- Bảng xếp hạng cạnh tranh

**4. Dashboard cá nhân:**
- Theo dõi tiến độ học tập
- Phân tích điểm yếu
- Đề xuất nội dung ưu tiên ôn

#### Kiến trúc hệ thống

Trong workshop này, bạn sẽ xây dựng hệ thống với các thành phần:

- **Frontend**: ReactJS trên S3 + CloudFront
- **Backend**: 8 Lambda functions
- **Database**: 8 bảng DynamoDB
- **Authentication**: Amazon Cognito
- **Message Queue**: Amazon SQS
- **DNS & SSL**: Route 53 + ACM
- **Monitoring**: CloudWatch + SNS

![ITCoach Architecture](/images/5-Workshop/5.1-overview/architecture.png)

#### Luồng xử lý chính

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

#### Thời gian ước tính

- **Thiết lập hạ tầng AWS**: 1-2 giờ
- **Deploy code (sau khi dev xong)**: 30 phút
- **Testing và kiểm tra**: 30 phút

**Tổng thời gian**: 2-3 giờ

