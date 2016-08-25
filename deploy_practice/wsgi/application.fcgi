#!/usr/bin/python3.4
from flup.server.fcgi import WSGIServer
from wsgi_app_v2 import app

if __name__ == '__main__':
    WSGIServer(app).run()