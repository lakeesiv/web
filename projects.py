from flask import Blueprint, render_template, url_for
from utils import projects_json

projects = Blueprint(
    'projects',
    __name__,
    url_prefix="projects",
    template_folder='projects/templates',
    static_folder='projects/static',
)

projects_data = projects_json("projects/projects.json")


@projects.route("/")
def projects_home():
    return render_template(
        "projects.html",
        title="Projects",
        active_page="projects",
        projects=projects_data)


@projects.route("/<string:project_link>")
def projects_page(project_link):
    links = [d["link"] for d in projects_data]
    if project_link in links:
        for d in projects_data:
            if project_link == d["link"]:
                title = d["title"]
                github = d["github"]
        return render_template(
            f"projects/{project_link}.html",
            title=f"{title}",
            active_page="projects",
            github = github)
    else:
        return render_template("404.html"), 404
