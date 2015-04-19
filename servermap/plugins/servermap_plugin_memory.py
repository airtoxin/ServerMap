#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from plugin_utils import assign_server, metric_formatter
from fabric.api import env, run, local
import re

def get_dimensions(servers):
    for server in servers:
        assign_server(server, env)
        mem = re.split(r"\s+", run("free | grep Mem:"))
        total   = int(mem[1])
        used    = int(mem[2])
        free    = int(mem[3])
        shared  = int(mem[4])
        buffers = int(mem[5])
        cached  = int(mem[6])
        return [
            metric_formatter(server=server["hostname"], dimension="memory", metric="total", value=total, unit="count"),
            metric_formatter(server=server["hostname"], dimension="memory", metric="used", value=used, unit="count"),
            metric_formatter(server=server["hostname"], dimension="memory", metric="free", value=free, unit="count"),
            metric_formatter(server=server["hostname"], dimension="memory", metric="shared", value=shared, unit="count"),
            metric_formatter(server=server["hostname"], dimension="memory", metric="buffers", value=buffers, unit="count"),
            metric_formatter(server=server["hostname"], dimension="memory", metric="cached", value=cached, unit="count")
        ]
