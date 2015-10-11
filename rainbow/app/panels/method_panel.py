# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import types
import inspect
import wx._core

from rainbow.app.panels.attribute_panel import AttributePanel


class ParameterPanel(wx.Panel):

    def __init__(self, parent, name):
        wx.Panel.__init__(self, parent)

        # self.SetBackgroundColour(wx.RED)

        # Elements
        self.name = wx.StaticText(self, label=name)
        self.name.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL))
        self.value = wx.TextCtrl(self)

        # Layout
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(self.name, 0, wx.TOP | wx.EXPAND, 13)
        hsizer.Add(self.value, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(hsizer)

        self.Layout()

    def get_name(self):
        return self.name.GetValue()

    def get_value(self):
        return self.value.GetValue()


class MethodPanel(wx.Panel):

    def __init__(self, parent, root):
        wx.Panel.__init__(self, parent)

        self.root = root
        self.parameters = []
        # self.SetBackgroundColour(wx.RED)

        # Elements
        self.title = wx.StaticText(self, label='Method')
        self.title.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL))
        self.parameters_panel = wx.Panel(self)
        self.button_method = wx.Button(self, label='method')
        self.result = wx.StaticText(self, label='Output: ')

        # Layout
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.parameters_panel.SetSizer(self.sizer)

        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.title, 0, wx.ALL | wx.EXPAND, 5)
        vsizer.Add(self.parameters_panel, 0, wx.ALL, 5)
        vsizer.Add(self.button_method, 0, wx.ALL, 5)
        vsizer.Add(self.result, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(vsizer)

        self.Layout()

        # Events
        self.button_method.Bind(wx.EVT_BUTTON, self.on_method_button_pressed)

    def set_item(self, instance):
        self.instance = 'self.root.' + instance
        self.title.SetLabel('Method:  ' + instance)

        self.sizer.DeleteWindows()
        self.sizer.Clear()
        self.parameters = []

        args = inspect.getargspec(eval(self.instance)).args[1:]
        # print inspect.getargspec(eval(self.instance)).defaults

        for arg in args:
            parameter = ParameterPanel(self.parameters_panel, arg)
            self.parameters += [parameter]
            self.sizer.Add(parameter, 0, wx.ALL | wx.EXPAND, 5)

        # + '  <' + str(type(eval(self.instance)))[7:-2] + '>')
        self.button_method.SetLabel(instance.split('.')[-1])
        self.result.SetLabel('Output: ')

    def on_method_button_pressed(self, event):
        ret = ''
        _type = type(eval(self.instance))
        if _type is types.MethodType:
            values = []
            for p in self.parameters:
                value = p.get_value()
                if value != '':
                    values += [p.get_value()]
            if len(values) == len(self.parameters):
                exec('ret = ' + self.instance + '(' + ','.join(values) + ')')
            else:
                print "Error: Invalid parameters"
        # elif _type is types.FunctionType:
        #    exec('ret = ' + self.instance + '(' + '.'.join(self.instance.split('.')[:-1]) + ')')
        self.result.SetLabel('Output:  ' + str(ret))
