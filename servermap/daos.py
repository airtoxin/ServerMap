#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement, absolute_import
from tinydb import TinyDB, where
import time, json

with open("config.json") as f:
    conf = json.loads(f.read())

class ServerMapDao(object):
    def __init__(self):
        self.table = TinyDB(conf["db"]["path"]).table("servermap")

class MetricsDao(object):
    def __init__(self, table_name):
        self.table = TinyDB(conf["db"]["path"]).table("metrics_" + table_name)

    def set_metric(self, dictionary):
        if not dictionary.has_key("timestamp"):
            dictionary["timestamp"] = time.time()
        self.table.insert(dictionary)

    def bulk_set_metric(self, dictionaries):
        timestamp = time.time()
        for dictionary in dictionaries:
            if not dictionary.has_key("timestamp"):
                dictionary["timestamp"] = time.time()

        self.table.insert_multiple(dictionaries)

    def get_metric_with_range(self, from_ts, to_ts):
        self.table.search(from_ts <= where("timestamp") < to_ts)
