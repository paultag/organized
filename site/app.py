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
    })

    open_bugs = db.bugs.find({
        "_project": project,
        "state": "open"
    })

    closed_bugs = db.bugs.find({
        "_project": project,
        "state": "closed"
    })

    return render_template('project.html', **{
        "project": probj,
        "bugs": bugs,
        "open_bugs": open_bugs,
        "closed_bugs": closed_bugs
    })


if __name__ == "__main__":
    app.debug = True
    app.run()
