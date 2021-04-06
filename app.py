import os
from flask import Flask, render_template, send_from_directory, request, redirect, url_for, flash
from utils import get_secret_key

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = get_secret_key()


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(
            app.root_path,
            'static'),
        'favicon.ico',
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

        if name and email and subject and message:
            res = name + email + subject + message
            return redirect(url_for("test", tst=res))
        else:
            flash("Make sure there is no empty fields")

        return render_template(
            "contact.html",
            title="Contact",
            active_page="contact")

    else:
        return render_template(
            "contact.html",
            title="Contact",
            active_page="contact")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/<tst>")
def test(tst):
    return f"<h1>{tst}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
