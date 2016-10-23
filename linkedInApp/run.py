# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
from main import hello, get_profile, re_direct, get_auth
from config import HOST, PORT


if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello, route_name='hello')

    config.add_route('re', '/redirect')
    config.add_view(re_direct, route_name='re')

    config.add_route('auth', '/auth')
    config.add_view(get_auth, route_name='auth')

    config.add_route('profile', '/')
    config.add_view(get_profile, route_name='profile')
    app = config.make_wsgi_app()
    logger.info('pyramid app running on http://{}:{}'.format(HOST, PORT))
    server = make_server(HOST, PORT, app)
    server.serve_forever()
