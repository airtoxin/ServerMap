#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement, absolute_import

from plugin_loader import load_plugin
import json, sys
from fabric import state
from daos import MetricsDao

state.output["everything"] = False # suppress fabric's output

class ServerMap(object):
    def __init__(self):
        with open("config.json") as f:
            self.config = json.loads(f.read())
            self.metrics_dao = MetricsDao()

    def main(self):
        sys.path.append("servermap/plugins")
        self.plugins = load_plugin("servermap_plugin_*")
        metricses = [
            plugin.get_metrics(self.config["servers"])
            for plugin in self.plugins
        ]
        for graph in metricses:
            for metric in graph:
                print metric
                self.metrics_dao.set_metric(metric["graph_name"], metric)

