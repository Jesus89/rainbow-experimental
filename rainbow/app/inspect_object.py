# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import inspect


def build_config(module, _class):
    instance = _class.lower()
    config_dict = {}
    main_dict = {}
    modules_list = []
    instances_dict = {}
    methods_dict = {}

    modules_list += [module]
    instances_dict[instance] = module + '.' + _class + '()'

    # Load methods
    exec('import ' + module)
    exec('cls = ' + module + '.' + _class)
    methods = inspect.getmembers(cls, predicate=inspect.ismethod)
    for name, method in methods:
        if name[0] != '_':
            m = {}
            m['doc'] = method.__doc__
            m['engine'] = instance + '.' + name
            args = inspect.getargspec(method).args
            if len(args) > 1:
                m['args'] = args[1:]
            else:
                m['args'] = None
            methods_dict[name] = m

    # Build main dictionary
    main_dict['modules'] = modules_list
    main_dict['instances'] = instances_dict
    main_dict['methods'] = methods_dict
    config_dict['main'] = main_dict

    return config_dict
