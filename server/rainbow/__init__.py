# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

__version__ = '0.0.0'

import os
import imp
import inspect

from rainbow.app import server


def main():
    filepath = load_configuration()
    if not os.path.isfile(filepath):
        print ''
        print '> Error: your module does not exist'
        print ''
        print 'Put your Python module path in: ~/.rainbow/rainbow.conf'
        print ''
        exit(1)
    server.initialize(load_instances(filepath))
    server.start(host='0.0.0.0', port=8081)


def load_configuration():
    config = None
    rainbow_path = os.path.join(os.path.expanduser('~'), '.rainbow')
    rainbow_config_path = os.path.join(rainbow_path, 'rainbow.conf')
    if not os.path.exists(rainbow_config_path):
        if not os.path.exists(rainbow_path):
            os.makedirs(rainbow_path)
        with open(rainbow_config_path, "w+") as f:
            f.write('')
    with open(rainbow_config_path, "r") as f:
        config = f.readline()
    return config.strip()


def load_instances(filepath):
    instances = {}
    module = imp.load_source('', filepath)
    for key, value in module.__dict__.items():
        if inspect.isclass(value):
            instances[key.lower()] = value()
    return instances


if __name__ == '__main__':
    main()
