# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import serial


class Zum(object):

    def __init__(self):
        self._serial = serial.Serial()
        self._serial.port = '/dev/ttyUSB0'
        self._serial.baudrate = 9600

    def open(self):
        self._serial.open()
        return self._serial.isOpen()

    def close(self):
        self._serial.close()
        return not self._serial.isOpen()

    def led(self, value):
        msg = '\n'
        if len(value) > 0:
            if value[0] == 'on':
                msg = 'on\n'
        self._serial.write(msg.encode())
