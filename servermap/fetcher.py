#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from fabric.api import run, local, env
from metrics.metrics_memory import MetricsMemory
import pkgutil

class Fetcher(object):
    def fetch(self):
        return MetricsMemory().get()
