# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import types
import wx._core

from rainbow.app.panels.attribute import AttributePanel
from rainbow.app.panels.function import FunctionPanel


# Test classes

class A(object):

    def __init__(self):
        self.value = True

    def inc(self):
        self.value += 1


class MyClass():

    def __init__(self):
        self.a = 0
        self.b = 0
        self._c = 1
        self.cla = A()

    def add(self):
        return self.a + self.b

    def log(self):
        return "log:", self.a, self.b, self.cla.value


# Root class
class Root():

    def __init__(self):
        # Load instances
        self.test1 = MyClass()
        #self.test2 = MyClass()

root = Root()


class MainWindow(wx.Frame):

    def __init__(self):
        super(MainWindow, self).__init__(None, size=(800, 400), title="Rainbow 0.0.1")

        self.tree_view = wx.TreeCtrl(
            self, size=(200, -1), style=wx.TR_DEFAULT_STYLE | wx.TR_HIDE_ROOT)
        self.root_node = self.tree_view.AddRoot('Root')
        self.attribute_panel = AttributePanel(self, root)
        self.function_panel = FunctionPanel(self, root)

        # Layout
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.tree_view, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.attribute_panel, 1, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.function_panel, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(sizer)

        self.attribute_panel.Hide()
        self.function_panel.Hide()
        self.Layout()

        # Events
        self.tree_view.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_item_selected)

        # Generate TreeView
        self.fill_node(self.root_node, root.__dict__)
        self.tree_view.ExpandAll()

    def fill_node(self, node, dictionary):
        for key in dictionary.keys():
            if key[0] != '_':
                instance = dictionary[key]

                # Object instances -> class type
                # Non object instances -> types.InstanceType
                if 'class' in str(type(instance)) or \
                   type(instance) is types.InstanceType:
                    next_node = self.tree_view.AppendItem(node, key)
                    try:
                        self.fill_node(next_node, instance.__dict__)
                        self.fill_node(next_node, instance.__class__.__dict__)
                    except TypeError:
                        pass
                else:
                    self.tree_view.AppendItem(node, key)

    def is_callable(self, item):
        return hasattr(item, '__call__')

    def on_item_selected(self, event):
        path = self.get_item_path(event.GetItem())
        instance = '.'.join(path)
        _type = type(eval('root.' + instance))

        self.attribute_panel.Hide()
        self.function_panel.Hide()

        if _type in [str, int, float, bool]:
            self.attribute_panel.set_item(instance)
            self.attribute_panel.Show()
        elif _type is types.MethodType:
            self.function_panel.set_item(instance)
            self.function_panel.Show()
        elif _type is types.InstanceType:
            pass

        self.Layout()

    def get_item_path(self, item):
        path = []
        while self.tree_view.GetItemParent(item):
            path = [self.tree_view.GetItemText(item)] + path
            item = self.tree_view.GetItemParent(item)
        return path
