from flask import Flask, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
