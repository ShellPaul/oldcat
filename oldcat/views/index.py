# -*- coding: utf-8 -*-

import flask

app = flask.Blueprint('index', __name__, url_prefix='/index')


@app.route("/")
def index():
    return flask.render_template("index/index.html")