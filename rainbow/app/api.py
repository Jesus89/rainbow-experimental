# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'


import os
import json
from rainbow.app.response import Response
from rainbow.app.inspect_object import build_config

MODULES = {}


# TODO: refactor!
def build_api(app):
    if True:
        # Automatic config generation from code
        config = build_config('rainbow.modules.zum', 'Zum')
    else:
        with open(os.path.abspath('rainbow/app/config.json'), 'r') as content_file:
            content = content_file.read()
        config = json.loads(content)

    modules = config['modules']
    for module in modules:
        module = modules[0]

        # Import modules
        exec('from ' + module['import'] + ' import ' + module['class'])

        # Load instance
        exec(module['name'] + '=' + module['class'] + '()')
        exec('MODULES["' + module['name'] + '"] = ' + module['name'])

        # Create methods
        methods = module['methods']
        # TODO: implement generic route function /<execute>/<parameters>
        for key, method in methods.items():
            args = method['args']
            if args is not None:
                function = """@app.get('/{0}/{1}/<{3}>')\ndef {1}({4}):\n\treturn function(MODULES["{0}"].{2}, {4})
                """.format(module['name'], key, method['engine'], '>,<'.join(args), ', '.join(args))
            else:
                function = """@app.get('/{0}/{1}')\ndef {1}():\n\treturn function(MODULES["{0}"].{2})
                """.format(module['name'], key, method['engine'])
            exec(function)

        return config


def function(f, *args):
    response = Response()
    try:
        if len(args) > 0:
            response.data = str(f(*args))
        else:
            response.data = str(f())
    except Exception as e:
        response.status = False
        response.message = str(e)
        return str(response)
    else:
        response.status = True
        return str(response)
