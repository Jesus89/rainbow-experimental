# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import wx._core


class AttributePanel(wx.Panel):

    def __init__(self, parent, cls):
        wx.Panel.__init__(self, parent)

        self.item = None
        self.cls = cls
        #self.SetBackgroundColour(wx.GREEN)

        self.title = wx.StaticText(self, label='Attribute')
        self.title.SetFont((wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL)))
        self.panel = wx.Panel(self)
        self.text_box = wx.TextCtrl(self.panel)
        #self.button_get = wx.Button(self.panel, label='Get')
        self.button_set = wx.Button(self.panel, label='Set')

        # Layout
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(self.text_box, 1, wx.ALL, 5)
        #hsizer.Add(self.button_get, 0, wx.ALL, 5)
        hsizer.Add(self.button_set, 0, wx.ALL, 5)
        self.panel.SetSizer(hsizer)

        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.title, 0, wx.ALL | wx.EXPAND, 5)
        vsizer.Add(self.panel, 1, wx.TOP | wx.EXPAND, 10)
        self.SetSizer(vsizer)

        self.Layout()

        # Events
        #self.button_get.Bind(wx.EVT_BUTTON, self.on_get_button_pressed)
        self.button_set.Bind(wx.EVT_BUTTON, self.on_set_button_pressed)

    def set_item(self, item):
        self.item = item
        self.title.SetLabel('Attribute: ' + item)
        self.on_get_button_pressed(None)

    def on_get_button_pressed(self, event):
        self.text_box.SetValue(str(self.cls.__dict__[self.item]))

    def on_set_button_pressed(self, event):
        _type = type(self.cls.__dict__[self.item])
        value = self.text_box.GetValue()

        if _type is int:
            self.cls.__dict__[self.item] = self.to_int(value)
        elif _type is float:
            self.cls.__dict__[self.item] = self.to_float(value)
        elif _type is bool:
            self.cls.__dict__[self.item] = self.to_bool(value)
        elif _type is str:
            self.cls.__dict__[self.item] = value

    def to_int(self, value):
        try:
            value = int(value)
            return value
        except:
            return 0

    def to_float(self, value):
        try:
            value = float(value)
            return value
        except:
            return 0.0

    def to_bool(self, value):
        return value == 'True'
