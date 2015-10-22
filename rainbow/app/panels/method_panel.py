# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import types
import inspect
import wx._core


class ParameterPanel(wx.Panel):

    def __init__(self, parent, name, value=''):
        wx.Panel.__init__(self, parent)

        # self.SetBackgroundColour(wx.RED)

        # Elements
        self.name = wx.StaticText(self, label=name)
        self.name.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL))
        self.value = wx.TextCtrl(self, value=str(value))

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

    def set_value(self, value):
        return self.value.SetValue(str(value))


class MethodPanel(wx.Panel):

    def __init__(self, parent, root, show_path=True):
        wx.Panel.__init__(self, parent)

        self.root = root
        self.parameters = []
        self.show_path = show_path
        # self.SetBackgroundColour(wx.RED)

        # Elements
        self.title = wx.StaticText(self, label='Method')
        self.title.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL))
        self.parameters_panel = wx.Panel(self)
        self.button_method = wx.Button(self, label='method')
        self.result = wx.TextCtrl(self, style=wx.TE_READONLY)  # wx.TE_MULTILINE

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

        self.sizer.DeleteWindows()
        self.sizer.Clear()
        self.parameters = []

        args = inspect.getargspec(eval(self.instance)).args[1:]
        defaults = inspect.getargspec(eval(self.instance)).defaults

        for arg in args:
            parameter = ParameterPanel(self.parameters_panel, arg)
            self.parameters += [parameter]
            self.sizer.Add(parameter, 0, wx.ALL | wx.EXPAND, 5)

        if defaults is not None:
            n = len(defaults)
            for parameter in list(reversed(self.parameters)):
                if n > 0:
                    n -= 1
                    parameter.set_value(defaults[n])

        self.button_method.SetLabel(instance.split('.')[-1])

        if not self.show_path:
            instance = instance.split('.')[-1]
        self.title.SetLabel('Method:  ' + instance)
        # + '  <' + str(type(eval(self.instance)))[7:-2] + '>')

        self.result.SetValue('')

    def execute_method(self):
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
                raise ValueError("Invalid parameters")
        return ret

    def on_method_button_pressed(self, event):
        ret = ''
        try:
            ret = self.execute_method()
        except Exception as e:
            dlg = wx.MessageDialog(self, str(e), "Exception", wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
        # elif _type is types.FunctionType:
        #    exec('ret = ' + self.instance + '(' + '.'.join(self.instance.split('.')[:-1]) + ')')
        self.result.SetValue(str(ret))
