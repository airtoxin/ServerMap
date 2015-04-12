#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from fabric.api import run, local, env

class MetricsMemory(object):
    def get(self):
        return local( 'echo hellowold!', capture=True )
