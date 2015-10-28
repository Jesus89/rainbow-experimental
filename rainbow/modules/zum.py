# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import time
import serial


class Zum(object):

    def __init__(self):
        self._serial = serial.Serial()
        self._serial.port = '/dev/ttyUSB0'
        self._serial.baudrate = 9600

    def port(self, port='/dev/ttyUSB0'):
        self._serial.port = port

    def baudrate(self, baudrate=9600):
        self._serial.baudrate = baudrate

    def open(self):
        """Open serial port"""
        self._serial.open()
        return self._serial.isOpen()

    def close(self):
        """Close serial port"""
        self._serial.close()
        return not self._serial.isOpen()

    def led(self, value, times):
        """Turn on/off a led"""
        if value == 'on':
            for i in range(int(times)):
                self._send_wait_msg('on\n')
                self._send_wait_msg('\n')

    def _send_wait_msg(self, msg):
        self._serial.write(msg.encode())
        time.sleep(0.1)
