# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import wx._core


class AttributePanel(wx.Panel):

    def __init__(self, parent, root, show_path=True):
        wx.Panel.__init__(self, parent)

        self.root = root
        self.show_path = show_path
        # self.SetBackgroundColour('#FFFF00')

        # Elements
        self.title = wx.StaticText(self, label='Attribute')
        self.title.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL))
        self.panel = wx.Panel(self)
        self.text_box = wx.TextCtrl(self.panel)
        self.button_get = wx.Button(self.panel, label='Get')
        self.button_set = wx.Button(self.panel, label='Set')

        # Layout
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(self.text_box, 1, wx.ALL, 5)
        hsizer.Add(self.button_get, 0, wx.ALL, 5)
        hsizer.Add(self.button_set, 0, wx.ALL, 5)
        self.panel.SetSizer(hsizer)

        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.title, 0, wx.ALL | wx.EXPAND, 5)
        vsizer.Add(self.panel, 1, wx.TOP | wx.EXPAND, 10)
        self.SetSizer(vsizer)

        self.Layout()

        # Events
        self.button_get.Bind(wx.EVT_BUTTON, self.on_get_button_pressed)
        self.button_set.Bind(wx.EVT_BUTTON, self.on_set_button_pressed)

    def set_item(self, instance):
        self.instance = 'self.root.' + instance
        if not self.show_path:
            instance = instance.split('.')[-1]
        self.title.SetLabel(
            'Attribute:  ' + instance)  # + '  <' + str(type(eval(self.instance)))[7:-2] + '>')
        self.on_get_button_pressed(None)

    def on_get_button_pressed(self, event):
        self.text_box.SetValue(str(eval(self.instance)))

    def execute_set(self):
        value = self.text_box.GetValue()
        _type = type(eval(self.instance))

        if _type is int:
            exec(self.instance + '= self.to_int(value)')
        elif _type is float:
            exec(self.instance + '= self.to_float(value)')
        elif _type is bool:
            exec(self.instance + '= self.to_bool(value)')
        elif _type is str or _type is unicode:
            exec(self.instance + '= value')

    def on_set_button_pressed(self, event):
        try:
            self.execute_set()
        except Exception as e:
            dlg = wx.MessageDialog(self, str(e), "Exception", wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()

        self.on_get_button_pressed(None)

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
