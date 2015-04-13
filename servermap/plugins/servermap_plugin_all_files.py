#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from plugin_utils import assign_server, metrics_formatter
from fabric.api import env, run, local

def get_metrics(servers):
    for server in servers:
        assign_server(server, env)
        ls = local("ls -la ~/", capture=True).splitlines()
        return metrics_formatter("all_files", len(ls), unit="count", value_type="number")
