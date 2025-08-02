from flask import Flask, request
from models import db, User
from config import Config
from dotenv import load_dotenv
from twilio.rest import Client
import os

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.form
    phone = data.get("From", "").replace("whatsapp:", "")
    msg = data.get("Body", "").strip()

    user = User.query.filter_by(phone=phone).first()
    if not user:
        user = User(phone=phone, current_step="collect_name")
        db.session.add(user)
        db.session.commit()
        return send_whatsapp_msg(phone, "👋 Hi! What's your name?")

    return handle_user_input(user, msg)

def handle_user_input(user, msg):
    step = user.current_step

    if step == "collect_name":
        user.name = msg
        user.current_step = "collect_age"
        db.session.commit()
        return send_whatsapp_msg(user.phone, f"Nice to meet you {user.name}! What's your age?")

    elif step == "collect_age":
        if not msg.isdigit():
            return send_whatsapp_msg(user.phone, "Please enter a valid age.")
        user.age = int(msg)
        user.current_step = "collect_gender"
        db.session.commit()
        return send_whatsapp_msg(user.phone, "What's your gender? (Male/Female/Other)")

    elif step == "collect_gender":
        user.gender = msg
        user.current_step = "collect_height"
        db.session.commit()
        return send_whatsapp_msg(user.phone, "Enter your height in cm:")

    elif step == "collect_height":
        try:
            user.height_cm = float(msg)
            user.current_step = "collect_weight"
            db.session.commit()
            return send_whatsapp_msg(user.phone, "Enter your current weight in kg:")
        except:
            return send_whatsapp_msg(user.phone, "Please enter a valid height in numbers.")

    elif step == "collect_weight":
        try:
            user.weight_kg = float(msg)
            user.current_step = "collect_goal"
            db.session.commit()
            return send_whatsapp_msg(user.phone, "What is your goal weight in kg?")
        except:
            return send_whatsapp_msg(user.phone, "Please enter a valid weight.")

    elif step == "collect_goal":
        try:
            user.goal_weight_kg = float(msg)
            user.current_step = "collect_activity"
            db.session.commit()
            return send_whatsapp_msg(user.phone, "What's your activity level? (Sedentary/Active/Very Active)")
        except:
            return send_whatsapp_msg(user.phone, "Please enter a valid number.")

    elif step == "collect_activity":
        user.activity_level = msg
        user.current_step = "collect_diet"
        db.session.commit()
        return send_whatsapp_msg(user.phone, "What's your diet type? (Veg/Non-Veg/Vegan/Keto)")

    elif step == "collect_diet":
        user.diet_type = msg
        user.current_step = "collect_medical"
        db.session.commit()
        return send_whatsapp_msg(user.phone, "Any medical conditions to consider? (If none, reply 'No')")

    elif step == "collect_medical":
        user.medical_issues = msg
        user.current_step = "collect_reminder"
        db.session.commit()
        return send_whatsapp_msg(user.phone, "At what time should I send daily reminders? (e.g., 08:00)")

    elif step == "collect_reminder":
        user.reminder_time = msg
        user.current_step = "profile_complete"
        db.session.commit()
        return send_whatsapp_msg(user.phone, "✅ All set! I'm generating your plan now...")

    elif step == "profile_complete":
        return send_whatsapp_msg(user.phone, "✅ You've already completed your profile. Plan generation coming soon!")

    return send_whatsapp_msg(user.phone, "Hmm, I didn't understand that. Let's start again.")

def send_whatsapp_msg(to, message):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_whatsapp = os.getenv("TWILIO_WHATSAPP_FROM", "whatsapp:+14155238886")
    to_whatsapp = f"whatsapp:{to}"

    client = Client(account_sid, auth_token)

    client.messages.create(
        body=message,
        from_=from_whatsapp,
        to=to_whatsapp
    )

    print(f"✅ Sent to WhatsApp: {to}")
    return "✅ WhatsApp message sent"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
