#!/usr/bin/env python

try:
    import bottle
except ImportError as e:
    print e.message
    exit(1)

from rainbow.app import server


def main():
    pass

if __name__ == '__main__':
    main()
