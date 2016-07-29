# -*- coding: utf-8 -*-

import flask

app = flask.Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
