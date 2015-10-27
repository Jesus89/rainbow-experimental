# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'


import os
import json
from bottle import route
from rainbow.app.response import Response
from rainbow.app.inspect_object import build_config

if True:
    # Automatic config generation from code
    config = build_config('rainbow.modules.zum', 'Zum')
else:
    with open(os.path.abspath('rainbow/app/config.json'), 'r') as content_file:
        content = content_file.read()
    config = json.loads(content)


main = config['main']
modules = main['modules']
instances = main['instances']
methods = main['methods']

# Import modules
for module in modules:
    exec('import ' + module)

# Load instances
for key, instance in instances.items():
    exec(key + '=' + instance)

# Create methods
# TODO: implement generic route function /<execute>/<parameters>
for key, method in methods.items():
    args = method['args']
    if args is not None:
        # One parameter suposed
        parameter = args[0]
        function = """@route('/{0}/<{2}>')\ndef {0}({2}):\n\treturn function({1}, {2})
        """.format(key, method['engine'], parameter)
    else:
        function = """@route('/{0}')\ndef {0}():\n\treturn function({1})
        """.format(key, method['engine'])
    exec(function)


def function(f, *args):
    response = Response()
    try:
        if len(args) > 0:
            response.data = str(f(args))
        else:
            response.data = str(f())
    except Exception as e:
        response.status = False
        response.message = str(e)
        return str(response)
    else:
        response.status = True
        return str(response)
