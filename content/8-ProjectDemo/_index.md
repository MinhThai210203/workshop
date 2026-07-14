---
title: "Project Demo"
date: 2024-01-01
weight: 8
chapter: false
pre: " <b> 8. </b> "
---

### ITCoach Core Feature Demo

> **Official Project Website:** [https://itcoach24h.xyz/](https://itcoach24h.xyz/)

Below are the actual screenshots and detailed descriptions of the key functional pages on the ITCoach technical interview preparation platform:

---

#### 1. Home / Landing Page
The entry point of ITCoach introducing the platform, track specialties (Frontend, Backend, DevOps), and core value propositions.

![Landing Page](/images/Trangchu.jpg)

*   **Key Features:**
    *   High-level overview of the IT interview preparation platform.
    *   Display core learning tracks (Frontend, Backend, DevOps).
    *   Visual roadmap and key benefits for students.

---

#### 2. Authentication (Login/Register Page)
Secure access management portal for students.

![Login Page](/images/Login.jpg)
![Register Page](/images/Register.jpg)

*   **Key Features:**
    *   User sign-in and sign-up powered by AWS Cognito.
    *   Safe registration with email-based OTP verification.
    *   OAuth2/OIDC integration for quick sign-in using Google accounts.

---

#### 3. Student Dashboard
The post-login personal hub for tracking learning progress.

![Student Dashboard](/images/Dashboard.jpg)

*   **Key Features:**
    *   Real-time display of user level, Experience Points (XP), and daily study streaks.
    *   Interactive charts to visualize progress and history.
    *   Direct shortcuts to resume recent courses or jump into practice modes.

---

#### 4. Leaderboard
A global scoreboard showing top-performing users.

![Leaderboard](/images/Leaderboard.jpg)

*   **Key Features:**
    *   Ranks users based on accrued XP and ongoing daily study streaks.
    *   Enhances motivation and engagement through gamified competition (Gamification).

---

#### 5. Quiz Select Room
Topic selection interface for establishing quiz parameters and picking quiz topics.

![Quiz Select Room](/images/Quiz%20Selection.jpg)

*   **Key Features:**
    *   Filter and search quiz banks by specific sub-topics (Frontend, Backend, DevOps, etc.).
    *   Customize difficulty levels (Easy, Medium, Hard) and question counts to tailor the training session.

---

#### 6. Quiz Taking Room
Interactive interface for taking multiple choice tests.

![Quiz Taking Room](/images/Quiz%20Taking.jpg)

*   **Key Features:**
    *   Clear, user-friendly forms supporting both single-choice and multi-choice questions.
    *   Integrated progress bars and countdown timers to simulate real exam pressure.

---

#### 7. Quiz Results
Score summary and breakdown page after submission.

![Quiz Results](/images/Quiz%20Result.jpg)
![Quiz Answers Explanation](/images/Quiz%20Result%20(2).jpg)

*   **Key Features:**
    *   Displays key metrics including correct/incorrect ratio and XP earned.
    *   Shows detailed answer keys with thorough explanations for self-correction.

---

#### 8. Technical Study Room
A listing of essay-based technical interview questions.

![Technical Study Room](/images/Study%20Room.jpg)

*   **Key Features:**
    *   Browse and search curated lists of real-world technical interview questions.
    *   Review comprehensive sample answers and reference explanations.
    *   Launch voice-based simulated mock interviews directly from any question.

---

#### 9. Voice-Based Interview Room
An immersive simulated voice interview experience.

![Voice Interview Room](/images/Interview%20Room.jpg)
![Voice Interview Active Session](/images/Interview%20Room%20(2).jpg)

*   **Key Features:**
    *   AI interviewer speaks the questions dynamically.
    *   Captures candidate response via real-time microphone recording.
    *   Securely uploads recorded audio files directly to AWS S3 using S3 Presigned URLs.
    *   Tracks response limits with active countdown timers.

---

#### 10. AI-Generated Interview Evaluation Report
A detailed evaluation feedback page post-interview.

![AI Interview Evaluation Report](/images/Interview%20Evaluation%20Report.jpg)

*   **Key Features:**
    *   Audio Speech-to-Text transcription of candidate responses.
    *   Scores responses and provides granular, constructive AI feedback.
    *   Streams synthesized audio of model answers using high-quality AWS Polly TTS.
