# -*- coding: utf-8 -*-

import os
import time
import urlparse

import flask

from .views.index import app as index
from .views.news import app as news
from .models.news import all_news
from .ocutils.regexconvert import set_app_regex_convert
from .ocutils.dirs import cache_dir

app = flask.Flask(__name__)
set_app_regex_convert(app)
app.register_blueprint(index)
app.register_blueprint(news)


@app.route("/")
def redirect_index():
    return flask.redirect(index.url_prefix)


@app.route("/sitemap.xml")
def sitemap_xml():
    cache_sitemap_xml = os.path.join(cache_dir, "sitemap.xml")
    if os.path.exists(cache_sitemap_xml) \
            and time.time() - os.stat(cache_sitemap_xml).st_mtime < 3600:
        with open(cache_sitemap_xml) as f:
            sitemap_xml = f.read()
    else:
        news = all_news()
        pages = [(urlparse.urljoin(
            flask.request.url_root,
            "/news/%d/%d/%d/%d.html" % (one.update_time.year, one.update_time.month, one.update_time.day, one.id)
        ), one.update_time) for one in news]
        sitemap_xml = flask.render_template("sitemap.xml", pages=pages)
        with open(cache_sitemap_xml, "w") as f:
            f.write(sitemap_xml)
    response = flask.make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response
