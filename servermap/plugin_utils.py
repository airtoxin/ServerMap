#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def assign_server(server, env):
    env.host_string = server["hostname"]
    env.key_filename = server["key_file"]

_re_hostname = re.compile(r"^(.*@)?(.*)(:\d)?$")
def get_user(hostname):
    return _re_hostname.search(hostname).group(1)

def get_host(hostname):
    return _re_hostname.search(hostname).group(2)

def get_port(hostname):
    return _re_hostname.search(hostname).group(3)
