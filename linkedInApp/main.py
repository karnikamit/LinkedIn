# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from pyramid.response import Response
import json
import auth_keys
import requests
from pyramid.response import FileResponse


def hello(request):
    return Response('Hello %(name)s!' % request.matchdict)


def re_direct(request):
    return Response()


def get_auth(request):
    ulrquote = requests.utils.quote(auth_keys.redirect_uri, safe='')
    response = requests.get('https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={}&redirect_uri={}'.format(auth_keys.Client_ID, ulrquote))
    file_op = open('a.html', 'w')
    file_op.write(response.content)
    file_op.close()
    return FileResponse('a.html')


def get_profile(request):
    url = 'https://api.linkedin.com/v1/people/~'
    print requests.get(url)
    return Response('Hello')
