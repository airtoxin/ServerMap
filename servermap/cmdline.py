#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from apscheduler.schedulers.background import BackgroundScheduler as Scheduler
from servermap import ServerMap
import dashboard

def main():
    scheduler = Scheduler()
    servermap = ServerMap()
    scheduler.add_job(servermap.reload, trigger='cron', minute='*/5')
    scheduler.add_job(servermap.main, trigger='cron', minute='*/1')
    scheduler.start()
    dashboard.run()
