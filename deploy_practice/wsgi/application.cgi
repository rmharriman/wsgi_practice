#!/usr/bin/python3.4
from wsgiref.handlers import CGIHandler
from wsgi_app_v2 import app

CGIHandler().run(app)