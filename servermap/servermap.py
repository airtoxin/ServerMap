#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement, absolute_import

from plugin_loader import load_plugin
import importlib, json, sys
from fabric import state

state.output["everything"] = False # suppress fabric's output

class ServerMap(object):
    def __init__(self):
        with open("config.json") as f:
            self.config = json.loads(f.read())

    def main(self):
        sys.path.append("servermap/plugins")
        self.plugins = load_plugin("servermap_plugin_*")
        metricses = [
            plugin.get_metrics(self.config["servers"])
            for plugin in self.plugins
        ]
        print metricses
