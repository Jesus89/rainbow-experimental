# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'


from bottle import route, run
from rainbow.modules.zum import Zum
from rainbow.app.response import Response

zum = Zum()


@route('/')
def home():
    return str(zum.__dict__) + str(zum.__class__.__dict__)


@route('/open')
def open():
    return function(zum.open)


@route('/close')
def close():
    return function(zum.close)


@route('/read_line')
def read_line():
    return function(zum.read_line)


@route('/read')
def read():
    return function(zum.read)


@route('/write/<char>')
def write(char):
    return function(zum.write, char)


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


run(host='localhost', port=8080, debug=True)
