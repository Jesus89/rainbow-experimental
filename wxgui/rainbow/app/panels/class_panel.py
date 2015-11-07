# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import types
import wx._core
import collections

from rainbow.app.panels.method_panel import MethodPanel
from rainbow.app.panels.attribute_panel import AttributePanel


class ClassPanel(wx.Panel):

    def __init__(self, parent, show_path=True):
        wx.Panel.__init__(self, parent)

        self.root = None
        self.show_path = show_path

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
        self.Hide()
        self.Layout()

    def load_root(self, root):
        self.root = root

    def set_item(self, instance):
        self.instance = 'self.root.' + instance

        self.sizer.DeleteWindows()
        self.sizer.Clear()
        exec('dictionary = ' + self.instance + '.__dict__')
        self.fill_elements(instance, dictionary)
        exec('dictionary = self.sort_dictionary(' + self.instance + '.__class__.__dict__)')
        self.fill_elements(instance, dictionary)

        if not self.show_path:
            instance = instance.split('.')[-1]
        self.title.SetLabel(
            'Class:  ' + instance)  # + '  <' + str(type(eval(self.instance)))[8:-2] + '>')

    def fill_elements(self, instance, dictionary):
        for k, v in dictionary.iteritems():
            if k[0] != '_':
                _type = type(v)
                inst = instance + '.' + k
                if 'class' in str(_type) or _type is types.InstanceType:
                    _class = wx.StaticText(self.panel)
                    _class.SetLabel(
                        'Class:  ' + k)
                        # + '  <' + str(type(eval('self.root.' + instance)))[8:-2] + '>')
                    _class.SetFont(
                        wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL))
                    self.sizer.Add(_class, 0, wx.ALL | wx.EXPAND, 15)
                elif _type is types.MethodType or _type is types.FunctionType:
                    method = MethodPanel(self.panel, show_path=False)
                    method.load_root(self.root)
                    method.set_item(inst)
                    method.Show()
                    self.sizer.Add(method, 0, wx.ALL | wx.EXPAND, 5)
                elif _type in [str, unicode, int, float, bool] or 'property' in str(_type):
                    attribute = AttributePanel(self.panel, show_path=False)
                    attribute.load_root(self.root)
                    attribute.set_item(inst)
                    attribute.Show()
                    self.sizer.Add(attribute, 0, wx.ALL | wx.EXPAND, 5)

                self.sizer.Add(wx.StaticLine(self.panel), 0, wx.EXPAND | wx.ALL, 5)

    def sort_dictionary(self, dictionary):
        properties = collections.OrderedDict()
        functions = collections.OrderedDict()
        for item in dictionary.iteritems():
            if 'property' in str(item[1]):
                properties[item[0]] = item[1]
            elif 'function' in str(item[1]):
                functions[item[0]] = item[1]
        properties.update(functions)
        return properties
