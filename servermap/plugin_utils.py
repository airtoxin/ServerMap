#!/usr/bin/env python
# -*- coding: utf-8 -*-

def assign_server(server, env):
    env.host_string = server["host"]

def metrics_formatter(name, value, unit="unit", value_type="value_type"):
    from time import time
    return {
        "name": name,
        "value": value,
        "unit": unit,
        "type": value_type,
        "timestamp": time()
    }
