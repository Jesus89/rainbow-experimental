# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import wx._core


class MainWindow(wx.Frame):

    def __init__(self):
        super(MainWindow, self).__init__(None, size=(600, 300), title="Rainbow 0.0.1")

        tree_view = wx.TreeCtrl(self, size=(250, -1))
        control_panel = wx.Panel(self)

        sizer = wx.BoxSizer(wx.HORIZONTAL)

        sizer.Add(tree_view, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(control_panel, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(sizer)

        # Test
        self.fill_tree_view(tree_view)
        tree_view.ExpandAll()

    def fill_tree_view(self, tree_view):
        root = tree_view.AddRoot('Programmer')
        os = tree_view.AppendItem(root, 'Operating Systems')
        pl = tree_view.AppendItem(root, 'Programming Languages')
        tk = tree_view.AppendItem(root, 'Toolkits')
        tree_view.AppendItem(os, 'Linux')
        tree_view.AppendItem(os, 'FreeBSD')
        tree_view.AppendItem(os, 'OpenBSD')
        tree_view.AppendItem(os, 'NetBSD')
        tree_view.AppendItem(os, 'Solaris')
        cl = tree_view.AppendItem(pl, 'Compiled languages')
        sl = tree_view.AppendItem(pl, 'Scripting languages')
        tree_view.AppendItem(cl, 'Java')
        tree_view.AppendItem(cl, 'C++')
        tree_view.AppendItem(cl, 'C')
        tree_view.AppendItem(cl, 'Pascal')
        tree_view.AppendItem(sl, 'Python')
        tree_view.AppendItem(sl, 'Ruby')
        tree_view.AppendItem(sl, 'Tcl')
        tree_view.AppendItem(sl, 'PHP')
        tree_view.AppendItem(tk, 'Qt')
        tree_view.AppendItem(tk, 'MFC')
        tree_view.AppendItem(tk, 'wxPython')
        tree_view.AppendItem(tk, 'GTK+')
        tree_view.AppendItem(tk, 'Swing')
