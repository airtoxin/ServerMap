#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement, absolute_import

from plugin_loader import load_plugin
import json, sys, logging
from fabric import state
from dao import Dao

logging.basicConfig(filename="system.log", level=logging.ERROR)
state.output["everything"] = False # suppress fabric's console output

class ServerMap(object):
    def __init__(self):
        self.dao = Dao()
        sys.path.append("servermap/plugins")

        self.reload()

    def load_servers(self):
        for server in self.config.get("servers"):
            hostname = server.get("hostname")
            self.dao.save_server_data(**server)

    def load_dimensions(self):
        for dimension in self.dimensions:
            self.dao.save_dimension_data(**dimension.metadata())

    def load_metrics(self):
        for dimension in self.dimensions:
            for metric in dimension.metric_metadata():
                self.dao.save_metric_data(dimension_name=dimension.metadata().get("dimension_name"), **metric)

    def reload(self):
        self.dimensions = load_plugin("servermap_dimension_*")
        for dimension in self.dimensions:
            reload(dimension)
        with open("config.json") as f:
            self.config = json.loads(f.read())
        self.load_servers()
        self.load_dimensions()
        self.load_metrics()

    def main(self):
        self.get_data()

    def get_data(self):
        for dimension in self.dimensions:
            for server in self.dao.get_servers():
                # TODO: threading
                try:
                    for metric in dimension.get_metrics(server):
                        datapoint = {
                            "dimension_name": dimension.metadata().get("dimension_name"),
                            "host": server.get("host"),
                            "metric_name": metric[0],
                            "value": metric[1],
                            "timestamp": metric[2]
                        }
                        self.dao.save_datapoint_data(**datapoint)
                except Exception as e:
                    logging.error(str(e))
