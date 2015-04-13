#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from plugin_utils import BaseMetric
from fabric.api import env, run, local

class Graph(BaseMetric):
    def __init__(self):
        self.graph_name = "files"

    def get_metrics(self, servers):
        for server in servers:
            self.assign_server(server, env)
            ls = local("ls ~/", capture=True).splitlines()
            lsla = local("ls -la ~/", capture=True).splitlines()
            return [
                self.metrics_formatter(metric_name="ls_files", metric_value=len(ls), metric_unit="count", metric_value_type="number"),
                self.metrics_formatter(metric_name="lsla_files", metric_value=len(lsla), metric_unit="count", metric_value_type="number")
            ]
