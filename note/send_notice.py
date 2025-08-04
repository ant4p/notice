import os
import requests
import smtplib
from smsaero import SmsAero

# Данные сервисов Google, необходимые для отправки уведомлений по почте.
MAIL_LOGIN = os.getenv("MAIL_LOGIN")
APP_PASSWORD_MAIL = os.getenv("APP_PASSWORD_MAIL")


def send_email(email, text):
    mail_smtp = smtplib.SMTP("smtp.gmail.com", 587)
    mail_smtp.starttls()
    mail_smtp.login(MAIL_LOGIN, APP_PASSWORD_MAIL)
    mail_smtp.sendmail(MAIL_LOGIN, email, text)
    mail_smtp.quit()


# Данные бота Telegaram, необходимые для отправки уведомлений в ТГ.
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


def send_telegram_message(chat_id, message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    response = requests.post(url, params=params)
    return response.json()


# Данные SMS гейта, необходимые для отправки уведомлений по SMS.
SMSAERO_EMAIL = os.getenv("SMSAERO_EMAIL")
SMSAERO_API_KEY = os.getenv("SMSAERO_API_KEY")


def send_sms(phone: int, message: str) -> dict:
    api = SmsAero(SMSAERO_EMAIL, SMSAERO_API_KEY)
    return api.send_sms(phone, message)
