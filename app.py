from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title = "Test")

@app.route("/about")
def about():
    return "about"

@app.route("/projects")
def projects():
    return "projects"

@app.route("/blog")
def blog():
    return "blog"





if __name__ == "__main__":
    app.run(debug=True)
