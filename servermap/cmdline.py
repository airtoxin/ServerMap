#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from servermap import ServerMap
import dashboard

def main():
    u"""Command line entry point"""
    ServerMap().main()
    dashboard.run()
