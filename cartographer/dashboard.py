#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, send_file, url_for
from flask.ext.basicauth import BasicAuth
from ConfigParser import SafeConfigParser
from os import path

conf = SafeConfigParser()
conf.read("config.ini")

app = Flask(__name__)
static_dir = path.join(app.root_path, "..", "static")

if conf.getboolean("dashboard", "use_basic_auth"):
    app.config["BASIC_AUTH_USERNAME"] = conf.get("dashboard", "username")
    app.config["BASIC_AUTH_PASSWORD"] = conf.get("dashboard", "password")

basic_auth = BasicAuth(app)

def run():
    app.run(debug=True)

@app.route("/", methods=["GET"])
@basic_auth.required
def index():
    return send_file(path.join(static_dir, "index.html"), mimetype="text/html")

@app.route('/favicon.ico', methods=["GET"])
def favicon():
    return send_file(path.join(static_dir, "favicon.ico"), mimetype="image/vnd.microsoft.icon")
