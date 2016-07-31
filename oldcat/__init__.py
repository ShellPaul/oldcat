# -*- coding: utf-8 -*-

import flask
from .views.index import app as index
from .views.news import app as news
from .ocutils.regexconvert import set_app_regex_convert

app = flask.Flask(__name__)
set_app_regex_convert(app)
app.register_blueprint(index)
app.register_blueprint(news)
