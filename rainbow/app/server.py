# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import rainbow.app.config
from rainbow.app.response import Response

from bottle import Bottle, request, response, run

app = Bottle()
config = rainbow.app.config.load_config()

# Instance objects
for name, module in config['modules'].items():
    exec('from ' + module['import'] + ' import ' + module['class'])
    exec(name + '=' + module['class'] + '()')


@app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'X-Requested-With, Content-Type'


@app.get('/')
def home():
    return config


@app.get('/<module>/<method>')
def execute(module, method):
    params = []
    for k, v in request.params.items():
        params += [k + '="' + v + '"']
    f = module + '.' + method + '(' + ','.join(params) + ')'
    return function(f)


def function(f):
    response = Response()
    try:
        exec(f)
    except Exception as e:
        response.status = False
        response.message = str(e)
        return str(response)
    else:
        response.status = True
        return str(response)


run(app, host='localhost', port=8081, debug=True)
