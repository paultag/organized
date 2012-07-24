# Copyright (c) Paul Tagliamonte <paultag@debian.org>, 2012 under the terms
# and conditions of the Expat license, a copy of which should be given to you
# with the source of this application.

from flask import Flask, render_template, request, url_for, redirect
from organized.db import db
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', **{})


@app.route('/project/<project>/')
def project(project=None):
    probj = db.projects.find_one({"_id": project})
    if probj is None:
        return redirect(url_for('index'))

    bugs = db.bugs.find({
        "_project": project
    }).sort("updated_at", -1)

    open_bugs = db.bugs.find({
        "_project": project,
        "state": "open"
    }).sort("updated_at", -1)

    closed_bugs = db.bugs.find({
        "_project": project,
        "state": "closed"
    }).sort("updated_at", -1)

    milestones = db.milestones.find({
        "project": project
    }).sort("target_date", 1)

    return render_template('project.html', **{
        "project": probj,
        "bugs": bugs,
        "open_bugs": open_bugs,
        "closed_bugs": closed_bugs,
        "milestones": milestones,
        "count": 10
    })


if __name__ == "__main__":
    app.debug = True
    app.run()
