#!/usr/bin/env python
# -*- coding: utf-8 -*-

def assign_server(server, env):
    env.host_string = server["hostname"]
    env.key_filename = server["key_file"]

def metric_formatter(server=None, dimension=None, metric=None, value=None, unit=None):
    import time
    return {
        "server":    server,
        "dimension": dimension,
        "metric":    metric,
        "timestamp": time.time(),
        "data_point": {
            "value": value,
            "unit":  unit,
        }
    }
