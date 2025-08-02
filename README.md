
# 🧠 WhatsApp Health Assistant Bot

This is a smart WhatsApp bot built using **Flask**, **Twilio Sandbox**, and **OpenAI**, designed to help users achieve health goals like **weight loss**. It interacts via WhatsApp, collects user data, sends personalized AI-generated plans, and checks in daily to keep users on track.

---

## ✨ Features

- ✅ WhatsApp integration via **Twilio Sandbox**
- ✅ Collects user profile (age, height, weight, diet, etc.)
- ✅ Stores user data in **PostgreSQL**
- ✅ Sends **real-time WhatsApp replies** using Twilio API
- 🧠 (Coming soon) OpenAI-powered plan generation
- ⏰ (Coming soon) Daily reminder system

---

## 📦 Tech Stack

| Layer        | Technology              |
|--------------|-------------------------|
| Messaging    | Twilio WhatsApp Sandbox |
| Backend API  | Python + Flask          |
| Database     | PostgreSQL (SQLAlchemy) |
| AI Assistant | OpenAI GPT (optional)   |
| Scheduling   | APScheduler or Celery   |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/whatsapp-health-assistant.git
cd whatsapp-health-assistant
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
# PostgreSQL
SQLALCHEMY_DATABASE_URI=postgresql://<username>:<password>@localhost:5432/whatsapp_assistant

# Twilio
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886

# OpenAI (for future AI plan generation)
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 🧪 Run Locally

### Start PostgreSQL and create the database:

```bash
# Inside PostgreSQL CLI
CREATE DATABASE whatsapp_assistant;
```

### Then run:

```bash
python app.py
```

---

## 🌐 Expose Flask App via Ngrok

```bash
ngrok http 5000
```

Copy the forwarding URL (e.g. `https://abc123.ngrok-free.app`) and add it to Twilio:

> 🔗 Twilio Console → Messaging → Try It Out → WhatsApp Sandbox →  
> 📩 "When a message comes in" = `https://abc123.ngrok-free.app/webhook`  
> Method = `POST`

---

## 📲 Test the Bot on WhatsApp

1. Open WhatsApp and message the join code (e.g., `join dot-fairly`) to:

   ```
   +1 415 523 8886
   ```

2. Then send:

   ```
   Hi
   ```

3. The bot will respond and begin collecting your info!

---

## 📌 Coming Soon

- 🧠 OpenAI integration for personalized plans
- ⏰ Daily check-in and motivational follow-ups
- 📈 Admin dashboard for progress tracking

---

## 🛡 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

- [Twilio WhatsApp API](https://www.twilio.com/whatsapp)
- [OpenAI Platform](https://platform.openai.com/)
- [Flask Framework](https://flask.palletsprojects.com/)
- [Ngrok](https://ngrok.com/)
