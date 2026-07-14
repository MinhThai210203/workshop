---
title: "Demo Dự án"
date: 2024-01-01
weight: 8
chapter: false
pre: " <b> 8. </b> "
---

### Demo Các Trang Chức Năng Ứng Dụng ITCoach

> **Website chính thức của dự án:** [https://itcoach24h.xyz/](https://itcoach24h.xyz/)

Dưới đây là hình ảnh thực tế và mô tả chi tiết của các trang chức năng cốt lõi trên nền tảng luyện thi phỏng vấn ITCoach:

---

#### 1. Trang Chủ (Landing Page)
Trang giới thiệu chung về nền tảng ITCoach, các chủ đề ôn tập (Frontend, Backend, DevOps) và các tính năng chính nổi bật.

![Trang Chủ](/images/Trangchu.jpg)

*   **Tính năng:**
    *   Giới thiệu tổng quan về ứng dụng ôn luyện phỏng vấn IT.
    *   Hiển thị các danh mục ôn tập chính (Frontend, Backend, DevOps).
    *   Trực quan hóa lộ trình học tập và các lợi ích nổi bật của nền tảng.

---

#### 2. Đăng Nhập / Đăng Ký (Login/Register)
Trang quản lý truy cập bảo mật cho học viên.

![Trang Đăng Nhập](/images/Login.jpg)
![Trang Đăng Ký](/images/Register.jpg)

*   **Tính năng:**
    *   Đăng nhập và đăng ký tài khoản thông qua AWS Cognito bảo mật.
    *   Hỗ trợ gửi mã xác minh OTP qua Email để kích hoạt tài khoản.
    *   Tích hợp đăng nhập nhanh bằng tài khoản Google OIDC.

---

#### 3. Bảng Điều Khiển (Dashboard)
Trang trung tâm quản lý học tập cá nhân sau khi đăng nhập thành công.

![Bảng Điều Khiển](/images/Dashboard.jpg)

*   **Tính năng:**
    *   Hiển thị cấp độ (Level), điểm kinh nghiệm (XP), chuỗi ngày học tập liên tục (Streak).
    *   Theo dõi tiến trình học tập qua lịch sử và biểu đồ hoạt động.
    *   Cung cấp các phím tắt truy cập nhanh vào các chủ đề bài học và đề trắc nghiệm đề xuất.

---

#### 4. Bảng Xếp Hạng (Leaderboard)
Trang vinh danh các học viên có thành tích học tập tốt nhất trên nền tảng.

![Bảng Xếp Hạng](/images/Leaderboard.jpg)

*   **Tính năng:**
    *   Hiển thị thứ hạng của học viên dựa trên XP và Streak.
    *   Thúc đẩy động lực thi đua học tập thông qua cơ chế trò chơi hóa (Gamification).

---

#### 5. Đề Trắc Nghiệm (Quiz Selection)
Giao diện lựa chọn chủ đề trắc nghiệm nhanh.

![Đề Trắc Nghiệm](/images/Quiz%20Selection.jpg)

*   **Tính năng:**
    *   Cho phép lọc bộ đề trắc nghiệm theo các chủ đề chuyên môn (Frontend, Backend, DevOps, v.v.).
    *   Tùy chọn độ khó (Easy, Medium, Hard) và số lượng câu hỏi để bắt đầu bài kiểm tra lý thuyết nhanh.

---

#### 6. Làm Bài Trắc Nghiệm (Quiz Taking)
Trang làm bài trắc nghiệm tương tác trực quan.

![Làm Bài Trắc Nghiệm](/images/Quiz%20Taking.jpg)

*   **Tính năng:**
    *   Hiển thị câu hỏi dưới dạng trắc nghiệm 1 đáp án hoặc nhiều đáp án.
    *   Tích hợp thanh tiến trình làm bài và đồng hồ đếm ngược thời gian thực.

---

#### 7. Kết Quả Trắc Nghiệm (Quiz Results)
Trang hiển thị điểm số và đáp án chi tiết sau khi nộp bài.

![Kết Quả Trắc Nghiệm](/images/Quiz%20Result.jpg)
![Chi Tiết Câu Trả Lời](/images/Quiz%20Result%20(2).jpg)

*   **Tính năng:**
    *   Thống kê số câu đúng/sai, số XP tích lũy nhận được.
    *   Hiển thị đáp án đúng cùng phần giải thích đáp án chi tiết cho từng câu hỏi giúp học viên tự ôn luyện.

---

#### 8. Phòng Học Lý Thuyết Tự Luận (Study Room)
Thư viện câu hỏi phỏng vấn tự luận theo chủ đề kỹ thuật.

![Phòng Học Lý Thuyết Tự Luận](/images/Study%20Room.jpg)

*   **Tính năng:**
    *   Xem danh sách câu hỏi phỏng vấn tự luận thường gặp theo từng danh mục.
    *   Xem câu trả lời mẫu chuẩn (Sample Answer) và phần phân tích chi tiết.
    *   Khởi chạy nhanh phiên phỏng vấn thoại (Mock Interview) liên quan trực tiếp đến câu hỏi.

---

#### 9. Phòng Phỏng Vấn Giọng Nói (Voice Interview Room)
Giao diện thực hiện bài phỏng vấn thoại trực tiếp với AI.

![Phòng Phỏng Vấn Giọng Nói](/images/Interview%20Room.jpg)
![Trạng Thái Phỏng Vấn](/images/Interview%20Room%20(2).jpg)

*   **Tính năng:**
    *   AI đóng vai trò người phỏng vấn đọc câu hỏi bằng giọng nói thoại tự nhiên.
    *   Ghi âm câu trả lời trực tiếp từ micro của học viên.
    *   Tự động tải và lưu trữ file ghi âm lên AWS S3 qua Presigned URL an toàn.
    *   Hiển thị đồng hồ đếm ngược cho mỗi câu hỏi để kiểm soát thời gian.

---

#### 10. Báo Cáo Đánh Giá Phỏng Vấn AI (AI Interview Evaluation Report)
Báo cáo phân tích chuyên sâu cho bài phỏng vấn thoại.

![Báo Cáo Đánh Giá Phỏng Vấn AI](/images/Interview%20Evaluation%20Report.jpg)

*   **Tính năng:**
    *   Chuyển đổi câu trả lời giọng nói của học viên thành văn bản (Speech-to-Text).
    *   Chấm điểm câu trả lời trên thang điểm 10, phân tích điểm mạnh/yếu và đưa ra nhận xét chuyên môn từ AI.
    *   Cung cấp audio câu trả lời chuẩn bằng giọng nói nhân tạo AWS Polly chất lượng cao để học viên luyện tập theo.
