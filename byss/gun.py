# -*- coding: utf-8 -*-
import multiprocessing

bind = "0.0.0.0:8888"
pidfile = 'data/gunicorn.pid'
workers = multiprocessing.cpu_count() * 2
worker_class = 'sync'
backlog = 2048
daemon = True
errorlog = 'data/error.log'

