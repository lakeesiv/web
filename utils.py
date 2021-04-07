import re
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


def env(var):
    return os.environ.get(var)


def get_secret_key():
    return env("SECRET_KEY")


def get_api_key():
    return env("SENDGRID_API_KEY")


def get_sender():
    return env("SENDER")


def get_reciever():
    return env("RECIEVER")


def email_check(email):
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if EMAIL_REGEX.match(email):
        return True
    else:
        return False
