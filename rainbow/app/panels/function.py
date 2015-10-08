# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import wx._core

from rainbow.app.panels.attribute import AttributePanel


class FunctionPanel(wx.Panel):

    def __init__(self, parent, cls):
        wx.Panel.__init__(self, parent)

        self.item = None
        self.cls = cls
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

    def set_item(self, item):
        self.item = item
        self.button_function.SetLabel(item)
        self.title.SetLabel('Function: ' + item)
        self.result.SetLabel('')

    def on_function_button_pressed(self, event):
        ret = self.cls.__class__.__dict__[self.item](self.cls)
        self.result.SetLabel(str(ret))
