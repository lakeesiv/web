import os
from flask import Flask, render_template, send_from_directory, request, redirect, url_for, flash
from flask_mail import Mail, Message
from utils import get_secret_key, email_check, get_api_key, get_sender, get_reciever
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = get_secret_key()
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = get_api_key()
app.config['MAIL_DEFAULT_SENDER'] = get_sender()
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
    return render_template("home.html", title="Home", active_page="home")


@app.route("/about")
def about():

    return render_template("about.html", title="About", active_page="about")


@app.route("/projects")
def projects():
    return render_template(
        "projects.html",
        title="Projects",
        active_page="projects")


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

        if name and email_check(email) and subject and message:
            flash("Sent!", "success")
            msg = Message(
                f'Email from {name}',
                recipients=[
                    get_reciever()])

            msg.html = (f'<h1>{subject}</h1>'
                        f'<h2>Message</h2>'
                        f"<p>{message}</p>"
                        f'From: {name} | {email}'
                        )
            mail.send(msg)
            return redirect(url_for("contact"))
        else:
            if not email_check(email):
                flash("Make sure the email is valid", "danger")
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


# @app.route("/<tst>")
# def test(tst):
#     return f"<h1>{tst}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
