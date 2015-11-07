# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import wx._core

from rainbow.app.main import MainWindow


class RainbowApp(wx.App):

    def __init__(self):
        super(RainbowApp, self).__init__()
        MainWindow().Show()
