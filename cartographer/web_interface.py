#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

def run():
    app.run(debug=True)

@app.route("/")
def index():
    return "Hello, Cartographer"
