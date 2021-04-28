from flask import Blueprint, render_template, url_for
from utils import get_json, projects_modified

projects = Blueprint(
    'projects',
    __name__,
    url_prefix="projects",
    template_folder='projects/templates',
    static_folder='projects/static',
)

projects_data = get_json("projects/projects.json")
tag_colors = get_json("projects/tag-colors.json")

projects_data = projects_modified(projects_data, tag_colors)


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
                tech = d["tech"]
                website = d["website"]

                if "devpost" in d:
                    devpost = d["devpost"]
                else:
                    devpost = ""

        return render_template(
            f"projects/{project_link}/{project_link}.html",
            title=f"{title}",
            active_page="projects",
            github=github,
            tech=tech,
            website=website,
            devpost=devpost)
    else:
        return render_template("404.html"), 404
