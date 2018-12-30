import os
from flask import Flask, render_template, send_from_directory
import json

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",
                           title="Ivan Galakhov")


@app.route("/contact")
def contact():
    return render_template("contact.html",
                           title="Contact Me")


@app.route("/projects")
def projects():
    NUM_PER_ROW = 3  # number of projects per row (no point in changing this)

    # open project json file and read it
    with open("website/static/projects.json") as project_file:
        project_dict_all = json.loads(project_file.read())

    # projects
    project_dict = project_dict_all["projects"]

    # fill groups with nulls (so it is 0 mod NUM_PER_ROW)
    project_groups = project_dict_all["groups"]

    for group in project_groups:
        while not len(group["members"]) % NUM_PER_ROW == 0:
            group["members"].append(None)

    print(project_groups)

    return render_template("projects.html",
                           title="My Projects",
                           projects=project_dict,
                           groups=project_groups)


@app.route("/resume")
def resume():
    return render_template("resume.html",
                           title="Online Resume")


# favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')
