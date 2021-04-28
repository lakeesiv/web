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


def projects_modified(data, colors):
    for project in data:
        tags = project["tags"]
        temp = []
        for i in range(len(tags)):
            tag = tags[i]

            if tag in colors:
                tag = {"tag": tag, "color": colors[tag]}
            else:
                tag = {"tag": tag, "color": "white"}
            temp.append(tag)
        project["tags"] = temp
    return data
