# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from pyramid.response import Response


def hello(request):
    return Response('Hello %(name)s!' % request.matchdict)
