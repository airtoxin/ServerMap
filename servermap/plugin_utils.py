#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def assign_server(server, env):
    host_string = server.get("host")
    user = server.get("user")
    port = server.get("port")

    if user is not None: host_string = str(user) + "@" + host_string
    if port is not None: host_string = host_string + ":" + str(port)

    env.host_string = host_string
    env.key_filename = server.get("key")
