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
    def _get_table(self, table_name):
        return TinyDB(conf["db"]["path"]).table("metrics_" + table_name)

    def set_metric(self, table_name, dictionary):
        table = self._get_table(table_name)
        if not dictionary.has_key("timestamp"):
            dictionary["timestamp"] = time.time()

        table.insert(dictionary)

    def bulk_set_metric(self, table_name, dictionaries):
        table = self._get_table(table_name)
        timestamp = time.time()
        for dictionary in dictionaries:
            if not dictionary.has_key("timestamp"):
                dictionary["timestamp"] = time.time()

        table.insert_multiple(dictionaries)

    def get_metric_with_range(self, table_name, from_ts, to_ts):
        table = self._get_table(table_name)
        return table.search(from_ts <= where("timestamp") < to_ts)

    def get_hourly_metrics(self, table_name):
        now = time.time()
        yesterhour = now - 3600 # 1 hour = 3600 sec
        return self.get_metric_with_range(table_name, yesterhour, now)

    def get_daily_metrics(self, table_name):
        now = time.time()
        yesterday = now - 86400 # 1 day = 86400 sec
        return self.get_metric_with_range(table_name, yesterday, now)

    def get_weekly_metrics(self, table_name):
        now = time.time()
        yesterweek = now - 604800 # 1 week = 604800 sec
        return self.get_metric_with_range(table_name, yesterweek, now)
