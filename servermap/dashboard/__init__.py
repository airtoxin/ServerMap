#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, time
from itertools import groupby
from flask import (Flask, render_template,
                   send_from_directory, url_for)
from dao import Dao

app = Flask(__name__, static_url_path="/static")
dao = Dao()

base = {
    "servers": dao.get_servers(),
    "colors": [
        '#4183c4', '#6cc644', '#bd2c00', '#FF9933', '#6e5494',
        '#56aef4', '#8fff55', '#fb3a00', '#ffcb3f', '#926fb8',
        '#2a5679', '#47822a', '#7c1d00', '#a8641f', '#48375b'
    ]
}

@app.route("/static/<path:p>")
def get_static_file(p):
    return send_from_directory("static", p)

@app.route("/")
def route_servers():
    return render_template(
        "index.html",
        base=base
    )

@app.route("/server/<host>")
def route_server(host):
    server_name = dao.get_server_name_by_host(host)
    raw = dao.get_metrics_data(host, 0, 1000000000000000)
    dimensions = {
        d[0]: {
            "metrics": {
                m[0][0]: {
                    "unit": m[0][1],
                    "points": [
                        {
                            "value": d["value"],
                            "timestamp": d["timestamp"]
                        }
                    for d in m[1]]
                }
            for m in groupby(d[1], key=lambda x: (x["metric_name"], x["unit"]))}
        }
    for d in groupby(raw, key=lambda x: x["dimension_name"])}

    return render_template(
        "server.html",
        base=base,
        server_name=server_name,
        dimensions=dimensions
    )

@app.route("/all")
def route_all():
    raw = dao.get_all_metrics_data(0, 10000000000000)
    servers = {
        s[0]: {
            "dimensions": {
                d[0]: {
                    "metrics": {
                        m[0][0]: {
                            "unit": m[0][1],
                            "points": [
                                {
                                    "value": d["value"],
                                    "timestamp": d["timestamp"]
                                }
                            for d in m[1]]
                        }
                    for m in groupby(d[1], key=lambda x: (x["metric_name"], x["unit"]))}
                }
            for d in groupby(s[1], key=lambda x: x["dimension_name"])}
        }
    for s in groupby(raw, key=lambda x: (x["host"], x["server_name"]))}

    return render_template(
        "all.html",
        base=base,
        servers=servers
    )

def run():
    app.run(debug=True)
