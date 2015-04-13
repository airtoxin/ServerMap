#!/usr/bin/env python
# -*- coding: utf-8 -*-

def assign_server(server, env):
    env.host_string = server["host"]

def metrics_formatter(graph_name, metric_name, value, unit="unit", value_type="value_type"):
    from time import time
    timestamp = time()
    return {
        "graph_name": graph_name,
        "name": metric_name,
        "value": value,
        "unit": unit,
        "value_type": value_type,
        "timestamp": timestamp
    }
