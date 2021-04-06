import re
import smtplib


def get_secret_key():
    f = open("secret_key.txt", "r")
    return f.read()


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


def send_email(name, email, subject, message):

    mess = f"""\
	New Email! from {name}

	Topic:
	{subject}


	Message:
	{message}


	From:
	{email}
	{name}
	"""

    sender, pasw, reciever = email_details()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, pasw)
    print(mess)
    server.sendmail(sender, reciever, mess)
