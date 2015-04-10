#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from flask import Flask, send_file, url_for
from os import path

app = Flask(__name__)
static_dir = path.join(app.root_path, "..", "static")

def run():
    app.run(debug=True)

@app.route("/", methods=["GET"])
def index():
    return send_file(path.join(static_dir, "index.html"), mimetype="text/html")

@app.route('/favicon.ico', methods=["GET"])
def favicon():
    return send_file(path.join(static_dir, "favicon.ico"), mimetype="image/vnd.microsoft.icon")
