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


def email_details():
    f = open("email_details.txt", "r")
    res = []
    for i in range(3):
        line = f.readline()
        res.append(line.strip("\n"))

    return res[0], res[1], res[2]
