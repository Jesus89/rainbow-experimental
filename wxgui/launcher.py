#!/usr/bin/env python

try:
    import wx._core
except ImportError as e:
    print e.message
    exit(1)

from rainbow.app import app


def main():
    app.RainbowApp().MainLoop()


if __name__ == '__main__':
    main()
