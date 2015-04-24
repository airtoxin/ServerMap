#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from plugin_utils import assign_server
from fabric.api import env, run, local
import re

def metadata():
    return {
        "dimension_name": "Memory",
        "description": "Memory dimension",
        "version": "0.0.1",
        "url": "https://github.com/airtoxin",
        "author": "airtoxin",
        "license": "MIT"
    }

def metric_metadata():
    return [
        {
            "metric_name": "total",
            "unit": "count",
            "value_type": "number"
        }, {
            "metric_name": "used",
            "unit": "count",
            "value_type": "number"
        }, {
            "metric_name": "free",
            "unit": "count",
            "value_type": "number"
        }, {
            "metric_name": "shared",
            "unit": "count",
            "value_type": "number"
        }, {
            "metric_name": "buffers",
            "unit": "count",
            "value_type": "number"
        }, {
            "metric_name": "cached",
            "unit": "count",
            "value_type": "number"
        }
    ]

def get_metrics(server):
    assign_server(server, env)
    mem = re.split(r"\s+", run("free | grep Mem:"))
    total   = int(mem[1])
    used    = int(mem[2])
    free    = int(mem[3])
    shared  = int(mem[4])
    buffers = int(mem[5])
    cached  = int(mem[6])
    return [
        ("total", total),
        ("used", used),
        ("free", free),
        ("shared", shared),
        ("buffers", buffers),
        ("cached", cached)
    ]
