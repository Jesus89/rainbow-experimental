# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

from bottle import get, hook, run, request, response

from rainbow.app.config import build_config
from rainbow.app.response import Response

config = {}
instances = {}


def start(host='0.0.0.0', port=8081):
    run(host=host, port=port, debug=True)


def initialize(_instances):
    print _instances
    global instances, config
    instances = _instances
    config = build_config(_instances)


@get('/')
def home():
    return config


@get('/<module>/<method>')
def execute(module, method):
    kwargs = request.params
    instance = instances[module]
    function = instance.__class__.__dict__[method]
    return execute_response(function, instance, **kwargs)


@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'X-Requested-With, Content-Type'


def execute_response(function, instance, **kwargs):
    resp = Response()
    try:
        resp.data = function(instance, **kwargs)
    except Exception as e:
        resp.status = False
        resp.message = str(e)
        return str(resp)
    else:
        resp.status = True
        return str(resp)
