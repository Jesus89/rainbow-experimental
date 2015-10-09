# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import wx._core

from rainbow.app.panels.attribute import AttributePanel


class FunctionPanel(wx.Panel):

    def __init__(self, parent, root):
        wx.Panel.__init__(self, parent)

        self.root = root
        #self.SetBackgroundColour(wx.RED)

        self.title = wx.StaticText(self, label='Function')
        self.title.SetFont((wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL)))
        self.button_function = wx.Button(self, label='function')
        self.result = wx.StaticText(self, label='')

        # Layout
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.title, 0, wx.ALL | wx.EXPAND, 5)
        vsizer.Add(self.button_function, 0, wx.TOP | wx.EXPAND, 10)
        vsizer.Add(self.result, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(vsizer)

        self.Layout()

        # Events
        self.button_function.Bind(wx.EVT_BUTTON, self.on_function_button_pressed)

    def set_item(self, instance):
        self.instance = 'self.root.' + instance
        self.title.SetLabel('Function: ' + instance)
        self.button_function.SetLabel(instance.split('.')[-1])
        self.result.SetLabel('')

    def on_function_button_pressed(self, event):
        exec('ret = ' + self.instance + '()')
        self.result.SetLabel(str(ret))
