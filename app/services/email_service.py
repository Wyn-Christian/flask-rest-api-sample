# app/services/email_service.py

from flask_mail import Message

from app.extensions import mail


def send_notification_email(subject, to, html, body):
    msg = Message(subject=subject, recipients=[to], body=body, html=html)
    mail.send(msg)
