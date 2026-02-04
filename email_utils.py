import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465


def send_day_mail(session, day_number):
    base_url = os.getenv("BASE_URL", "http://127.0.0.1:5000")

    link = f"{base_url}/unlock/{session.id}/{day_number}"
    unsubscribe_link = f"{base_url}/unsubscribe/{session.id}"

    body = f"""
Hi {session.partner_name} 💖,

Someone who loves you has planned something special for you today ✨  
A small surprise… a secret… and a story you don’t know yet.

To unlock today’s Valentine surprise,
answer a simple question prepared just for you 💌

👉 Open today’s surprise:
{link}

Every day, a new message will arrive —
and on **Valentine’s Day (Feb 14)**,
their name will finally be revealed 💝

This message was sent with love via ❤️ hilove.in

────────────────────────
If you no longer wish to receive these emails,
you can unsubscribe anytime below:
{unsubscribe_link}

An interactive project by  
Nexston Corporations Pvt Ltd
"""

    msg = MIMEMultipart()
    msg["Subject"] = "💌 A Valentine Surprise Awaits You"
    msg["From"] = os.getenv("EMAIL_ADDRESS")
    msg["To"] = session.partner_email
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=15)
        server.login(
            os.getenv("EMAIL_ADDRESS"),
            os.getenv("EMAIL_PASSWORD")
        )
        server.send_message(msg)
        server.quit()
        print(f"📧 Day {day_number} mail sent to {session.partner_email}")
    except Exception as e:
        print("❌ SMTP send_day_mail error:", e)


def send_finale_mail(session):
    base_url = os.getenv("BASE_URL", "http://127.0.0.1:5000")

    link = f"{base_url}/finale/{session.id}"
    unsubscribe_link = f"{base_url}/unsubscribe/{session.id}"

    body = f"""
Hi {session.partner_name} 💖,

Today is Valentine’s Day ❤️  
No questions.  
No locks.  
No waiting.

Just one final message —
from the person who has been thinking about you every single day.

👉 Open your Valentine message:
{link}

This message was sent with love via ❤️ hilove.in

────────────────────────
If you no longer wish to receive messages like this,
you may unsubscribe below:
{unsubscribe_link}

An interactive project by  
Nexston Corporations Pvt Ltd
"""

    msg = MIMEMultipart()
    msg["Subject"] = "💖 Your Valentine’s Day Surprise"
    msg["From"] = os.getenv("EMAIL_ADDRESS")
    msg["To"] = session.partner_email
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=15)
        server.login(
            os.getenv("EMAIL_ADDRESS"),
            os.getenv("EMAIL_PASSWORD")
        )
        server.send_message(msg)
        server.quit()
        print(f"💖 Finale mail sent to {session.partner_email}")
    except Exception as e:
        print("❌ SMTP send_finale_mail error:", e)