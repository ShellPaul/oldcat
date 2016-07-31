# -*- coding: utf-8 -*-

import flask
from ..models.news import hot_news

app = flask.Blueprint('index', __name__, url_prefix='/index')


@app.route("/")
def index():
    news = hot_news()
    hnews = [{
        "href": "/news/%d/%d/%d/%d.html" %
                (one.update_time.year, one.update_time.month, one.update_time.day, one.id),
        "title": one.title,
    } for one in news]
    return flask.render_template("index/index.html", hot_news=hnews)
