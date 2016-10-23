# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from pyramid.response import Response
import json


def hello(request):
    return Response('Hello %(name)s!' % request.matchdict)


def hi(request):
    return Response(json.dumps({'response': 'success'}))
