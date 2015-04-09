#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, send_file
from os import path

sites_dir = path.join("..", "sites")

app = Flask(__name__)

def run():
    app.run(debug=True)

@app.route("/", methods=["GET"])
def index():
    return send_file(path.join(sites_dir, "index.html"), mimetype="text/html")
