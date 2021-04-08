from flask import Blueprint, render_template

projects = Blueprint('projects', __name__,
                     template_folder='projects',
                     static_folder="static")


@projects.route("/")
def projects_home():
    return render_template(
        "projects.html",
        title="Projects",
        active_page="projects",
        projects=[{"title": "test1", "text": "text1"}, {"title": "test2", "text": "text2"}])
