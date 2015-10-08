# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import wx._core

from rainbow.app.panels.attribute import AttributePanel
from rainbow.app.panels.function import FunctionPanel


# Test class
class MyClass(object):

    def __init__(self):
        self.a = 0
        self.b = False
        self.c = 34.3

    def add(self, x, y):
        return x + y

    def log(self):
        print "log:", self.a, self.b, self.c

test_class = MyClass()


class MainWindow(wx.Frame):

    def __init__(self):
        super(MainWindow, self).__init__(None, size=(600, 300), title="Rainbow 0.0.1")

        self.tree_view = wx.TreeCtrl(
            self, size=(200, -1), style=wx.TR_DEFAULT_STYLE | wx.TR_HIDE_ROOT)
        self.root = self.tree_view.AddRoot('Root')
        self.attribute_panel = AttributePanel(self, test_class)
        self.function_panel = FunctionPanel(self, test_class)

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

        # Att TestClass to TreeView
        self.fill_tree_view(self.tree_view, test_class)
        self.tree_view.ExpandAll()

    def fill_tree_view(self, tree_view, instance):
        c = self.tree_view.AppendItem(self.root, instance.__class__.__name__)

        [self.tree_view.AppendItem(c, k) for (k, v) in instance.__dict__.iteritems()
         if k[:1] != '_' and not self.is_callable(v)]

        [self.tree_view.AppendItem(c, k) for (k, v) in instance.__class__.__dict__.iteritems()
         if k[:1] != '_' and self.is_callable(v)]

    def is_callable(self, item):
        return hasattr(item, '__call__')

    def on_item_selected(self, event):
        path = self.get_item_path(event.GetItem())
        item = self.tree_view.GetItemText(event.GetItem())

        if self.is_attr(item):
            self.attribute_panel.set_item(item)
            self.attribute_panel.Show()
            self.function_panel.Hide()

        elif self.is_function(item):
            self.function_panel.set_item(item)
            self.attribute_panel.Hide()
            self.function_panel.Show()

        self.Layout()

    def is_attr(self, item):
        if item in test_class.__dict__.keys():
            _type = type(test_class.__dict__[item])
            if _type in [str, int, float, bool]:
                return True
            return False
        return False

    def is_function(self, item):
        if item in test_class.__class__.__dict__.keys():
            _type = type(test_class.__class__.__dict__[item])
            if str(_type) == "<type 'function'>":
                return True
            return False
        return False

    def get_item_path(self, item):
        pieces = []
        while self.tree_view.GetItemParent(item):
            piece = self.tree_view.GetItemText(item)
            pieces.insert(0, piece)
            item = self.tree_view.GetItemParent(item)
        return str(pieces)
