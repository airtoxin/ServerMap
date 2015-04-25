#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from apscheduler.schedulers.background import BackgroundScheduler as Scheduler
from servermap import ServerMap
import dashboard

def main():
    scheduler = Scheduler()
    scheduler.add_job(ServerMap().main, trigger='cron', minute='*/1')
    scheduler.start()
    dashboard.run()
