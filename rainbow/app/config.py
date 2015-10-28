# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import os
import json
import inspect


def load_config():
    if True:
        # Automatic config generation from code
        config = build_config('rainbow.modules.zum', 'Zum')
    else:
        with open(os.path.abspath('rainbow/app/config.json'), 'r') as content_file:
            content = content_file.read()
        config = json.loads(content)
    return config


def build_config(_import, _class):
    config_dict = {}
    modules_list = {}

    module = {}
    module['import'] = _import
    module['class'] = _class
    # Load methods
    exec('from ' + _import + ' import ' + _class)
    exec('cls = ' + _class)
    methods_dict = {}
    methods = inspect.getmembers(cls, predicate=inspect.ismethod)
    for name, method in methods:
        if name[0] != '_':
            m = {}
            m['doc'] = method.__doc__
            args = inspect.getargspec(method).args
            if len(args) > 1:
                m['args'] = args[1:]
            else:
                m['args'] = None
            methods_dict[name] = m
    module['methods'] = methods_dict

    modules_list[_class.lower()] = module
    config_dict['modules'] = modules_list

    return config_dict
