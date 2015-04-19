#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement, absolute_import

from plugin_loader import load_plugin
import json, sys
from fabric import state
from daos import Dao

state.output["everything"] = False # suppress fabric's console output

class ServerMap(object):
    def __init__(self):
        with open("config.json") as f:
            self.config = json.loads(f.read())
            self.dao = Dao()

    def main(self):
        sys.path.append("servermap/plugins")
        plugins = load_plugin("servermap_plugin_*")
        dimensions = [
            plugin.get_dimensions(self.config["servers"])
            for plugin in plugins
        ]
        for dimension in dimensions:
            for metric in dimension:
                self.dao.set_metric(metric)
