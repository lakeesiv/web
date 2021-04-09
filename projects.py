from flask import Blueprint, render_template, url_for
from utils import projects_json

projects = Blueprint(
    'projects',
    __name__,
    url_prefix="projects",
    template_folder='projects/templates',
    static_folder='projects/static',
)


@projects.route("/")
def projects_home():
    return render_template(
        "projects.html",
        title="Projects",
        active_page="projects",
        projects=projects_json("projects/projects.json"))


# @projects.route("/test")
# def projects_test():
#     a = projects_json("projects/projects.json")
#     return f"<h1>{a}</h1>"
