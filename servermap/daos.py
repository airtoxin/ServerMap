#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement, absolute_import
from tinydb import TinyDB, where
import time, json

with open("config.json") as f:
    conf = json.loads(f.read())

class Dao(object):
    def __init__(self):
        self.db = TinyDB(conf["db"]["path"])

    def set_metric(self, metric):
        self.db.insert(metric)

    def find_metric_by_dimension(self, dim_name):
        return self.db.search(where("dimension") == dim_name)

    def find_servers(self):
        return set(d["server"] for d in self.db.all())
