# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from main import hello
# import auth_keys

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello, route_name='hello')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()
