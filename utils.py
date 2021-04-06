import re


def get_secret_key():
    f = open("secret_key.txt", "r")
    return f.read()


def email_check(email):
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if EMAIL_REGEX.match(email):
        return True
    else:
        return False
