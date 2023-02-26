import os
from flask import (Flask, render_template, send_from_directory,
                   request, redirect, url_for, flash)
from flask_mail import Mail, Message
from utils import email_check, get_json, env
from dotenv import load_dotenv
from projects import projects
from flask_recaptcha import ReCaptcha

load_dotenv()

app = Flask(__name__)

app.register_blueprint(projects, url_prefix="/projects")

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = env("SECRET_KEY")
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = env("SENDGRID_API_KEY")
app.config['MAIL_DEFAULT_SENDER'] = env("SENDER")
app.config["RECAPTCHA_ENABLED"] = True
app.config["RECAPTCHA_SITE_KEY"] = env("RECAPTCHA_SITE")
app.config["RECAPTCHA_SECRET_KEY"] = env("RECAPTCHA_SECRET")
app.config["RECAPTCHA_THEME"] = "dark"


recaptcha = ReCaptcha()
recaptcha.init_app(app)


if env("STATUS") == "dev":
    app.debug = True
else:
    app.debug = False

mail = Mail(app)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(
            app.root_path,
            'static'),
        'imgs/icons/favicon.ico',
        mimetype='image/vnd.microsoft.icon')


@app.route("/")
@app.route("/home")
def home():
    return render_template(
        "home.html",
        title="Home",
        active_page="home",
        nofooter=True)


timeline_data = get_json("static/timeline.json")


@app.route("/about")
def about():

    return render_template(
        "about.html",
        title="About",
        active_page="about",
        timelinedata=timeline_data)


@app.route("/cv")
def cv():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ?autoplay=1")


@app.route("/blog")
def blog():
    return render_template("blog.html", title="Blog", active_page="blog")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        if name and email_check(
                email) and subject and message and recaptcha.verify():
            flash("Sent!", "success")
            msg = Message(
                f'Email from {name}',
                recipients=[
                    env("RECIEVER")])

            msg.html = (f'<h1>{subject}</h1>'
                        f"<p style = 'white-space: pre-wrap'>{message}</p>"
                        f'From: {name} | {email}'
                        )
            print(msg.as_string())
            mail.send(msg)
            return redirect(url_for("contact"))
        else:
            if not email_check(email):
                flash("Make sure the email is valid", "danger")
            elif not recaptcha.verify():
                flash("Verify the ReCaptcha", "danger")
            else:
                flash("Make sure there is no empty fields", "danger")
            return render_template(
                "contact.html",
                title="Contact",
                active_page="contact",
                _name=name,
                _email=email,
                _subject=subject,
                _message=message)

    else:
        return render_template(
            "contact.html",
            title="Contact",
            active_page="contact")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/personal-statement")
def personal_statement():
    # return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ?autoplay=1")
    return render_template("personal-statement.html", title="Personal Statement", active_page="about")


if __name__ == "__main__":
    app.run()
