# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import time
import serial


class Testbot(object):

    def __init__(self):
        self._serial = serial.Serial('/dev/ttyUSB0', 9600)

    def connect(self):
        self._serial.open()

    def disconnect(self):
        self.led_off()
        self._serial.close()

    def led_on(self):
        self._send_msg('on')

    def led_off(self):
        self._send_msg('off')

    def fade_on(self):
        self._send_msg('fon')

    def set_color(self, r='FF', g='FF', b='FF'):
        """Set RGB color"""
        color = '#' + r + g + b
        self._send_msg(color)
        return 'Set RGB color: ' + color

    def _send_msg(self, msg):
        self._serial.write(msg.encode() + '\n')
        time.sleep(0.1)
