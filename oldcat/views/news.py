# -*- coding: utf-8 -*-

import json

import flask
from flask import current_app

from ..models.news import News
from ..ocutils.parse_type import parse_int

app = flask.Blueprint('news', __name__, url_prefix='/news')


@app.route(r"/<regex('\d{4}'):year>/<regex('\d{1,2}'):month>/<regex('\d{1,2}'):day>/<int:nid>.html")
def index(year, month, day, nid):
    year, month, day, nid = parse_int(year, month, day, nid)
    if all([v is not None for v in (year, month, day, nid)]):
        news = News.select().where(News.id == int(nid))
        if len(news) > 0:
            news = news[0]
            date = news.update_time
            if date.year == year and date.month == month and date.day == day:
                data = {
                    "title": news.title,
                    "content": json.loads(news.article),
                    "frm": news.frm,
                    "update_time": news.update_time,
                }
                return flask.render_template("news/show.html", data=data)
    return flask.abort(404)
