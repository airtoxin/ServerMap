#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, time
from flask import (Flask, render_template,
                   send_from_directory, url_for)
app = Flask(__name__, static_url_path="/static")

base = {
    "servernames": ["dev01", "log01"],
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

@app.route("/server/<server_name>")
def route_server(server_name):
    return render_template(
        "server.html",
        base=base,
        server_name=server_name,
        dimensions={
            "Memory": {
                "metrics": {
                    "Total": {
                        "unit": "count",
                        "points": [
                            { "value": 100, "timestamp": time.mktime(time.strptime("2015 04 01 00 00", "%Y %m %d %H %M")) },
                            { "value": 200, "timestamp": time.mktime(time.strptime("2015 04 01 00 05", "%Y %m %d %H %M")) },
                            { "value": 300, "timestamp": time.mktime(time.strptime("2015 04 01 00 10", "%Y %m %d %H %M")) },
                            { "value": 600, "timestamp": time.mktime(time.strptime("2015 04 01 00 15", "%Y %m %d %H %M")) },
                            { "value": 500, "timestamp": time.mktime(time.strptime("2015 04 01 00 20", "%Y %m %d %H %M")) },
                            { "value": 600, "timestamp": time.mktime(time.strptime("2015 04 01 00 25", "%Y %m %d %H %M")) },
                            { "value": 400, "timestamp": time.mktime(time.strptime("2015 04 01 00 30", "%Y %m %d %H %M")) },
                            { "value": 800, "timestamp": time.mktime(time.strptime("2015 04 01 00 35", "%Y %m %d %H %M")) },
                            { "value": 900, "timestamp": time.mktime(time.strptime("2015 04 01 00 40", "%Y %m %d %H %M")) }
                        ]
                    },
                    "Free": {
                        "unit": "count",
                        "points": [
                            { "value": 682, "timestamp": time.mktime(time.strptime("2015 04 01 00 00", "%Y %m %d %H %M")) },
                            { "value": 745, "timestamp": time.mktime(time.strptime("2015 04 01 00 05", "%Y %m %d %H %M")) },
                            { "value": 742, "timestamp": time.mktime(time.strptime("2015 04 01 00 10", "%Y %m %d %H %M")) },
                            { "value": 985, "timestamp": time.mktime(time.strptime("2015 04 01 00 15", "%Y %m %d %H %M")) },
                            { "value": 278, "timestamp": time.mktime(time.strptime("2015 04 01 00 20", "%Y %m %d %H %M")) },
                            { "value": 554, "timestamp": time.mktime(time.strptime("2015 04 01 00 25", "%Y %m %d %H %M")) },
                            { "value": 845, "timestamp": time.mktime(time.strptime("2015 04 01 00 30", "%Y %m %d %H %M")) },
                            { "value": 945, "timestamp": time.mktime(time.strptime("2015 04 01 00 35", "%Y %m %d %H %M")) },
                            { "value": 374, "timestamp": time.mktime(time.strptime("2015 04 01 00 40", "%Y %m %d %H %M")) }
                        ]
                    }
                }
            },
            "DiscIO": {
                "metrics": {
                    "Wait": {
                        "unit": "count",
                        "points": [
                            { "value": 900, "timestamp": time.mktime(time.strptime("2015 04 01 00 00", "%Y %m %d %H %M")) },
                            { "value": 800, "timestamp": time.mktime(time.strptime("2015 04 01 00 05", "%Y %m %d %H %M")) },
                            { "value": 700, "timestamp": time.mktime(time.strptime("2015 04 01 00 10", "%Y %m %d %H %M")) },
                            { "value": 600, "timestamp": time.mktime(time.strptime("2015 04 01 00 15", "%Y %m %d %H %M")) },
                            { "value": 500, "timestamp": time.mktime(time.strptime("2015 04 01 00 20", "%Y %m %d %H %M")) },
                            { "value": 400, "timestamp": time.mktime(time.strptime("2015 04 01 00 25", "%Y %m %d %H %M")) },
                            { "value": 300, "timestamp": time.mktime(time.strptime("2015 04 01 00 30", "%Y %m %d %H %M")) },
                            { "value": 200, "timestamp": time.mktime(time.strptime("2015 04 01 00 35", "%Y %m %d %H %M")) },
                            { "value": 100, "timestamp": time.mktime(time.strptime("2015 04 01 00 40", "%Y %m %d %H %M")) }
                        ]
                    },
                    "Read kBps": {
                        "unit": "count",
                        "points": [
                            { "value": 100, "timestamp": time.mktime(time.strptime("2015 04 01 00 00", "%Y %m %d %H %M")) },
                            { "value": 200, "timestamp": time.mktime(time.strptime("2015 04 01 00 05", "%Y %m %d %H %M")) },
                            { "value": 300, "timestamp": time.mktime(time.strptime("2015 04 01 00 10", "%Y %m %d %H %M")) },
                            { "value": 600, "timestamp": time.mktime(time.strptime("2015 04 01 00 15", "%Y %m %d %H %M")) },
                            { "value": 500, "timestamp": time.mktime(time.strptime("2015 04 01 00 20", "%Y %m %d %H %M")) },
                            { "value": 600, "timestamp": time.mktime(time.strptime("2015 04 01 00 25", "%Y %m %d %H %M")) },
                            { "value": 400, "timestamp": time.mktime(time.strptime("2015 04 01 00 30", "%Y %m %d %H %M")) },
                            { "value": 800, "timestamp": time.mktime(time.strptime("2015 04 01 00 35", "%Y %m %d %H %M")) },
                            { "value": 900, "timestamp": time.mktime(time.strptime("2015 04 01 00 40", "%Y %m %d %H %M")) }
                        ]
                    },
                    "Write kBps": {
                        "unit": "count",
                        "points": [
                            { "value": 100, "timestamp": time.mktime(time.strptime("2015 04 01 00 00", "%Y %m %d %H %M")) },
                            { "value": 200, "timestamp": time.mktime(time.strptime("2015 04 01 00 05", "%Y %m %d %H %M")) },
                            { "value": 300, "timestamp": time.mktime(time.strptime("2015 04 01 00 10", "%Y %m %d %H %M")) },
                            { "value": 400, "timestamp": time.mktime(time.strptime("2015 04 01 00 15", "%Y %m %d %H %M")) },
                            { "value": 500, "timestamp": time.mktime(time.strptime("2015 04 01 00 20", "%Y %m %d %H %M")) },
                            { "value": 600, "timestamp": time.mktime(time.strptime("2015 04 01 00 25", "%Y %m %d %H %M")) },
                            { "value": 700, "timestamp": time.mktime(time.strptime("2015 04 01 00 30", "%Y %m %d %H %M")) },
                            { "value": 800, "timestamp": time.mktime(time.strptime("2015 04 01 00 35", "%Y %m %d %H %M")) },
                            { "value": 900, "timestamp": time.mktime(time.strptime("2015 04 01 00 40", "%Y %m %d %H %M")) }
                        ]
                    }
                }
            }
        }
    )

@app.route("/all")
def route_all():
    return render_template(
        "all.html",
        base=base,
        servers={
            "dev01": {
                "dimensions": {
                    "Memory": {
                        "metrics": {
                            "Total": {
                                "unit": "count",
                                "points": [
                                    { "value": 100, "timestamp": time.mktime(time.strptime("2015 04 01 00 00", "%Y %m %d %H %M")) },
                                    { "value": 200, "timestamp": time.mktime(time.strptime("2015 04 01 00 05", "%Y %m %d %H %M")) },
                                    { "value": 300, "timestamp": time.mktime(time.strptime("2015 04 01 00 10", "%Y %m %d %H %M")) },
                                    { "value": 400, "timestamp": time.mktime(time.strptime("2015 04 01 00 15", "%Y %m %d %H %M")) },
                                    { "value": 500, "timestamp": time.mktime(time.strptime("2015 04 01 00 20", "%Y %m %d %H %M")) },
                                    { "value": 600, "timestamp": time.mktime(time.strptime("2015 04 01 00 25", "%Y %m %d %H %M")) },
                                    { "value": 700, "timestamp": time.mktime(time.strptime("2015 04 01 00 30", "%Y %m %d %H %M")) },
                                    { "value": 800, "timestamp": time.mktime(time.strptime("2015 04 01 00 35", "%Y %m %d %H %M")) },
                                    { "value": 900, "timestamp": time.mktime(time.strptime("2015 04 01 00 40", "%Y %m %d %H %M")) }
                                ]
                            },
                            "Free": {
                                "unit": "count",
                                "points": [
                                    { "value": 100, "timestamp": time.mktime(time.strptime("2015 04 01 00 00", "%Y %m %d %H %M")) },
                                    { "value": 200, "timestamp": time.mktime(time.strptime("2015 04 01 00 05", "%Y %m %d %H %M")) },
                                    { "value": 300, "timestamp": time.mktime(time.strptime("2015 04 01 00 10", "%Y %m %d %H %M")) },
                                    { "value": 600, "timestamp": time.mktime(time.strptime("2015 04 01 00 15", "%Y %m %d %H %M")) },
                                    { "value": 500, "timestamp": time.mktime(time.strptime("2015 04 01 00 20", "%Y %m %d %H %M")) },
                                    { "value": 600, "timestamp": time.mktime(time.strptime("2015 04 01 00 25", "%Y %m %d %H %M")) },
                                    { "value": 400, "timestamp": time.mktime(time.strptime("2015 04 01 00 30", "%Y %m %d %H %M")) },
                                    { "value": 800, "timestamp": time.mktime(time.strptime("2015 04 01 00 35", "%Y %m %d %H %M")) },
                                    { "value": 900, "timestamp": time.mktime(time.strptime("2015 04 01 00 40", "%Y %m %d %H %M")) }
                                ]
                            }
                        }
                    },
                    "DiscIO": {
                        "metrics": {
                            "Max": {
                                "unit": "count",
                                "points": [
                                    { "value": 100, "timestamp": time.mktime(time.strptime("2015 04 01 00 00", "%Y %m %d %H %M")) },
                                    { "value": 200, "timestamp": time.mktime(time.strptime("2015 04 01 00 05", "%Y %m %d %H %M")) },
                                    { "value": 300, "timestamp": time.mktime(time.strptime("2015 04 01 00 10", "%Y %m %d %H %M")) },
                                    { "value": 600, "timestamp": time.mktime(time.strptime("2015 04 01 00 15", "%Y %m %d %H %M")) },
                                    { "value": 500, "timestamp": time.mktime(time.strptime("2015 04 01 00 20", "%Y %m %d %H %M")) },
                                    { "value": 600, "timestamp": time.mktime(time.strptime("2015 04 01 00 25", "%Y %m %d %H %M")) },
                                    { "value": 400, "timestamp": time.mktime(time.strptime("2015 04 01 00 30", "%Y %m %d %H %M")) },
                                    { "value": 800, "timestamp": time.mktime(time.strptime("2015 04 01 00 35", "%Y %m %d %H %M")) },
                                    { "value": 900, "timestamp": time.mktime(time.strptime("2015 04 01 00 40", "%Y %m %d %H %M")) }
                                ]
                            },
                            "Average": {
                                "unit": "count",
                                "points": [
                                    { "value": 900, "timestamp": time.mktime(time.strptime("2015 04 01 00 00", "%Y %m %d %H %M")) },
                                    { "value": 800, "timestamp": time.mktime(time.strptime("2015 04 01 00 05", "%Y %m %d %H %M")) },
                                    { "value": 700, "timestamp": time.mktime(time.strptime("2015 04 01 00 10", "%Y %m %d %H %M")) },
                                    { "value": 600, "timestamp": time.mktime(time.strptime("2015 04 01 00 15", "%Y %m %d %H %M")) },
                                    { "value": 500, "timestamp": time.mktime(time.strptime("2015 04 01 00 20", "%Y %m %d %H %M")) },
                                    { "value": 400, "timestamp": time.mktime(time.strptime("2015 04 01 00 25", "%Y %m %d %H %M")) },
                                    { "value": 300, "timestamp": time.mktime(time.strptime("2015 04 01 00 30", "%Y %m %d %H %M")) },
                                    { "value": 200, "timestamp": time.mktime(time.strptime("2015 04 01 00 35", "%Y %m %d %H %M")) },
                                    { "value": 100, "timestamp": time.mktime(time.strptime("2015 04 01 00 40", "%Y %m %d %H %M")) }
                                ]
                            }
                        }
                    }
                }
            },
            "log01": {
                "dimensions": {
                    "Memory": {
                        "metrics": {
                            "Total": {
                                "unit": "count",
                                "points": [
                                    { "value": 900, "timestamp": time.mktime(time.strptime("2015 04 01 00 00", "%Y %m %d %H %M")) },
                                    { "value": 800, "timestamp": time.mktime(time.strptime("2015 04 01 00 05", "%Y %m %d %H %M")) },
                                    { "value": 700, "timestamp": time.mktime(time.strptime("2015 04 01 00 10", "%Y %m %d %H %M")) },
                                    { "value": 600, "timestamp": time.mktime(time.strptime("2015 04 01 00 15", "%Y %m %d %H %M")) },
                                    { "value": 500, "timestamp": time.mktime(time.strptime("2015 04 01 00 20", "%Y %m %d %H %M")) },
                                    { "value": 400, "timestamp": time.mktime(time.strptime("2015 04 01 00 25", "%Y %m %d %H %M")) },
                                    { "value": 300, "timestamp": time.mktime(time.strptime("2015 04 01 00 30", "%Y %m %d %H %M")) },
                                    { "value": 200, "timestamp": time.mktime(time.strptime("2015 04 01 00 35", "%Y %m %d %H %M")) },
                                    { "value": 100, "timestamp": time.mktime(time.strptime("2015 04 01 00 40", "%Y %m %d %H %M")) }
                                ]
                            },
                            "Free": {
                                "unit": "count",
                                "points": [
                                    { "value": 100, "timestamp": time.mktime(time.strptime("2015 04 01 00 00", "%Y %m %d %H %M")) },
                                    { "value": 200, "timestamp": time.mktime(time.strptime("2015 04 01 00 05", "%Y %m %d %H %M")) },
                                    { "value": 300, "timestamp": time.mktime(time.strptime("2015 04 01 00 10", "%Y %m %d %H %M")) },
                                    { "value": 400, "timestamp": time.mktime(time.strptime("2015 04 01 00 15", "%Y %m %d %H %M")) },
                                    { "value": 500, "timestamp": time.mktime(time.strptime("2015 04 01 00 20", "%Y %m %d %H %M")) },
                                    { "value": 600, "timestamp": time.mktime(time.strptime("2015 04 01 00 25", "%Y %m %d %H %M")) },
                                    { "value": 700, "timestamp": time.mktime(time.strptime("2015 04 01 00 30", "%Y %m %d %H %M")) },
                                    { "value": 800, "timestamp": time.mktime(time.strptime("2015 04 01 00 35", "%Y %m %d %H %M")) },
                                    { "value": 900, "timestamp": time.mktime(time.strptime("2015 04 01 00 40", "%Y %m %d %H %M")) }
                                ]
                            }
                        }
                    },
                    "DiscIO": {
                        "metrics": {
                            "Max": {
                                "unit": "count",
                                "points": [
                                    { "value": 900, "timestamp": time.mktime(time.strptime("2015 04 01 00 00", "%Y %m %d %H %M")) },
                                    { "value": 800, "timestamp": time.mktime(time.strptime("2015 04 01 00 05", "%Y %m %d %H %M")) },
                                    { "value": 700, "timestamp": time.mktime(time.strptime("2015 04 01 00 10", "%Y %m %d %H %M")) },
                                    { "value": 600, "timestamp": time.mktime(time.strptime("2015 04 01 00 15", "%Y %m %d %H %M")) },
                                    { "value": 500, "timestamp": time.mktime(time.strptime("2015 04 01 00 20", "%Y %m %d %H %M")) },
                                    { "value": 400, "timestamp": time.mktime(time.strptime("2015 04 01 00 25", "%Y %m %d %H %M")) },
                                    { "value": 300, "timestamp": time.mktime(time.strptime("2015 04 01 00 30", "%Y %m %d %H %M")) },
                                    { "value": 200, "timestamp": time.mktime(time.strptime("2015 04 01 00 35", "%Y %m %d %H %M")) },
                                    { "value": 100, "timestamp": time.mktime(time.strptime("2015 04 01 00 40", "%Y %m %d %H %M")) }
                                ]
                            },
                            "Average": {
                                "unit": "count",
                                "points": [
                                    { "value": 100, "timestamp": time.mktime(time.strptime("2015 04 01 00 00", "%Y %m %d %H %M")) },
                                    { "value": 200, "timestamp": time.mktime(time.strptime("2015 04 01 00 05", "%Y %m %d %H %M")) },
                                    { "value": 300, "timestamp": time.mktime(time.strptime("2015 04 01 00 10", "%Y %m %d %H %M")) },
                                    { "value": 400, "timestamp": time.mktime(time.strptime("2015 04 01 00 15", "%Y %m %d %H %M")) },
                                    { "value": 500, "timestamp": time.mktime(time.strptime("2015 04 01 00 20", "%Y %m %d %H %M")) },
                                    { "value": 600, "timestamp": time.mktime(time.strptime("2015 04 01 00 25", "%Y %m %d %H %M")) },
                                    { "value": 700, "timestamp": time.mktime(time.strptime("2015 04 01 00 30", "%Y %m %d %H %M")) },
                                    { "value": 800, "timestamp": time.mktime(time.strptime("2015 04 01 00 35", "%Y %m %d %H %M")) },
                                    { "value": 900, "timestamp": time.mktime(time.strptime("2015 04 01 00 40", "%Y %m %d %H %M")) }
                                ]
                            }
                        }
                    }
                }
            }
        }
    )

def run():
    app.run(debug=True)
