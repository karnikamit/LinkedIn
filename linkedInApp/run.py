# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
from main import hello, hi
from config import HOST, PORT
# import auth_keys

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello, route_name='hello')
    config.add_route('hi', '/')
    config.add_view(hi, route_name='hi')
    app = config.make_wsgi_app()
    logger.info('pyramid app running on http://{}:{}'.format(HOST, PORT))
    server = make_server(HOST, PORT, app)
    server.serve_forever()
