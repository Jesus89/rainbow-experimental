#!/usr/bin/env python

import os
import sys
import imp
import inspect

from rainbow.app import server

# Load file
if len(sys.argv) == 2:
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print "File do not exists"
        exit(1)
else:
    print "Wrong number of parameters"
    exit(1)


def main():
    server.initialize(load_instances(filepath))
    server.start(host='0.0.0.0', port=8081)


def load_instances(filepath):
    instances = {}
    module = imp.load_source('', filepath)
    for key, value in module.__dict__.items():
        if inspect.isclass(value):
            instances[key.lower()] = value()
    return instances


if __name__ == '__main__':
    main()
