# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'


class Response(object):

    def __init__(self):
        self.status = False
        self.data = None
        self.message = None

    def __str__(self):
        resp = '{'
        resp += '"status":' + self.to_string(self.status) + ','
        resp += '"data":' + self.to_string(self.data) + ','
        resp += '"message":' + self.to_string(self.message)
        resp += '}'
        return resp

    def to_string(self, value):
        if value is None:
            return 'null'
        elif isinstance(value, bool):
            return str(value).lower()
        else:
            return '"' + str(value) + '"'
