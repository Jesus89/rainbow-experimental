# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import inspect


def build_config(instances):
    instance_dict = {}

    for key, value in instances.items():
        # Load methods
        methods_dict = {}
        methods = inspect.getmembers(value, predicate=inspect.ismethod)
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
        instance_dict[key] = methods_dict

    return instance_dict
