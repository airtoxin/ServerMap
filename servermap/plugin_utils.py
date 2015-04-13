#!/usr/bin/env python
# -*- coding: utf-8 -*-

class BaseMetric(object):
    def assign_server(self, server, env):
        env.host_string = server["host"]

    def metrics_formatter(
        self,
        metric_name=None,
        metric_value=None,
        metric_unit=None,
        metric_value_type=None
    ):
        from time import time
        return {
            "graph_name": self.graph_name,
            "name": metric_name,
            "value": metric_value,
            "unit": metric_unit,
            "value_type": metric_value_type,
            "timestamp": time()
        }
