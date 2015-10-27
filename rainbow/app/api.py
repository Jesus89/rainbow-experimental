# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'


from bottle import route
from rainbow.app.response import Response


def build_api():
    # >>>> Generate code <<<<

    # modules
    import rainbow.modules.zum

    # instances
    zum = rainbow.modules.zum.Zum()

    # methods

    @route('/open')
    def open():
        return function(zum.open)

    @route('/close')
    def close():
        return function(zum.close)

    @route('/led/<status>')  # <"on", !"on">
    def led(status):
        return function(zum.led, status)

    # <<<< >>>>


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
