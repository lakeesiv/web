import re
import smtplib
import os
from dotenv import load_dotenv
import json

load_dotenv()


def env(var):
    return os.environ.get(var)


def email_check(email):
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if EMAIL_REGEX.match(email):
        return True
    else:
        return False


def get_json(path):
    with open(path) as json_file:
        data = json.load(json_file)
        return data
