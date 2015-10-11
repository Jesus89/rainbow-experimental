# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import types
import wx._core

from rainbow.app.panels.method_panel import MethodPanel
from rainbow.app.panels.attribute_panel import AttributePanel


class ClassPanel(wx.Panel):

    def __init__(self, parent, root):
        wx.Panel.__init__(self, parent)

        self.root = root
        #self.SetBackgroundColour(wx.BLUE)

        # Elements
        self.title = wx.StaticText(self, label='Class')
        self.title.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD))
        self.panel = wx.Panel(self)

        # Layout
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetSizer(self.sizer)

        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.title, 0, wx.ALL | wx.EXPAND, 5)
        vsizer.Add(self.panel, 1, wx.ALL | wx.EXPAND, 10)
        self.SetSizer(vsizer)

        self.Layout()

    def set_item(self, instance):
        self.instance = 'self.root.' + instance
        self.title.SetLabel(
            'Class:  ' + instance)  # + '  <' + str(type(eval(self.instance)))[8:-2] + '>')

        self.sizer.DeleteWindows()
        self.sizer.Clear()
        exec('dictionary = ' + self.instance + '.__dict__')
        self.fill_elements(instance, dictionary)
        exec('dictionary = ' + self.instance + '.__class__.__dict__')
        self.fill_elements(instance, dictionary)

    def fill_elements(self, instance, dictionary):
        for k, v in dictionary.iteritems():
            if k[0] != '_':
                _type = type(v)
                inst = instance + '.' + k
                if 'class' in str(_type) or _type is types.InstanceType:
                    _class = wx.StaticText(self.panel)
                    _class.SetLabel(
                        'Class:  ' + inst)
                        # + '  <' + str(type(eval('self.root.' + instance)))[8:-2] + '>')
                    _class.SetFont(
                        wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL))
                    self.sizer.Add(_class, 0, wx.ALL | wx.EXPAND, 15)
                elif _type is types.MethodType or _type is types.FunctionType:
                    method = MethodPanel(self.panel, self.root)
                    method.set_item(inst)
                    self.sizer.Add(method, 0, wx.ALL | wx.EXPAND, 5)
                elif _type in [str, int, float, bool]:
                    attribute = AttributePanel(self.panel, self.root)
                    attribute.set_item(inst)
                    self.sizer.Add(attribute, 0, wx.ALL | wx.EXPAND, 5)

                self.sizer.Add(wx.StaticLine(self.panel), 0, wx.EXPAND | wx.ALL, 5)
