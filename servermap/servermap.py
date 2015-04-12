#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from fetcher import Fetcher
from daos import MetricsDao
from plugin_loader import load_plugin
import importlib

class ServerMap(object):
    def __init__(self):
        self.hosts = config.get("hosts") # TODO: define config

    def main(self):
        self.plugins = load_plugin("servermap_plugin_*")
        metricses = [plugin.get_metrics(self.hosts) for plugin in self.plugins]

    def cron_job(self):
        metricses = self.fetch_metrics()
        self.save_data(metricses)
