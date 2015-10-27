# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import inspect


def build_config(_import, _class):
    config_dict = {}
    modules_list = []

    module = {}
    module['import'] = _import
    module['class'] = _class
    module['name'] = _class.lower()
    # Load methods
    exec('from ' + _import + ' import ' + _class)
    exec('cls = ' + _class)
    methods_dict = {}
    methods = inspect.getmembers(cls, predicate=inspect.ismethod)
    for name, method in methods:
        if name[0] != '_':
            m = {}
            m['doc'] = method.__doc__
            m['engine'] = name
            args = inspect.getargspec(method).args
            if len(args) > 1:
                m['args'] = args[1:]
            else:
                m['args'] = None
            methods_dict[name] = m
    module['methods'] = methods_dict

    modules_list += [module]
    config_dict['modules'] = modules_list

    return config_dict
