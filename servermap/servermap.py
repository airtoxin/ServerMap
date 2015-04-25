#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement, absolute_import

from plugin_loader import load_plugin
import json, sys
from fabric import state
from dao import Dao
from plugin_utils import get_host, get_user, get_port

state.output["everything"] = False # suppress fabric's console output

class ServerMap(object):
    def __init__(self):
        self.dao = Dao()
        sys.path.append("servermap/plugins")
        self.dimensions = load_plugin("servermap_dimension_*")

        self.reload()

    def load_servers(self):
        for server in self.config["servers"]:
            self.dao.save_server_data(
                server_name=server["server_name"],
                host=get_host(server["hostname"]),
                user=get_user(server["hostname"]),
                port=get_port(server["hostname"])
            )

    def load_dimensions(self):
        for dimension in self.dimensions:
            self.dao.save_dimension_data(**dimension.metadata())

    def load_metrics(self):
        for dimension in self.dimensions:
            for metric in dimension.metric_metadata():
                self.dao.save_metric_data(dimension_name=dimension.metadata()["dimension_name"], **metric)

    def reload(self):
        with open("config.json") as f:
            self.config = json.loads(f.read())
        self.load_servers()
        self.load_dimensions()
        self.load_metrics()

    def main(self):
        self.get_data()

    def get_data(self):
        for dimension in self.dimensions:
            for server in self.config["servers"]:
                for metric in dimension.get_metrics(server):
                    datapoint = {
                        "dimension_name": dimension.metadata()["dimension_name"],
                        "metric_name": metric[0],
                        "host": get_host(server["hostname"]),
                        "value": metric[1],
                        "timestamp": metric[2]
                    }
                    self.dao.save_datapoint_data(**datapoint)
