# -*- coding: utf-8 -*-

from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


def set_app_regex_convert(app):
    app.url_map.converters['regex'] = RegexConverter
