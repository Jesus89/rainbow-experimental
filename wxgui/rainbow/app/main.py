# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import types
import wx._core
import collections
import wx.lib.scrolledpanel

from rainbow.app.loader import load_rainbow
from rainbow.app.panels.class_panel import ClassPanel
from rainbow.app.panels.method_panel import MethodPanel
from rainbow.app.panels.attribute_panel import AttributePanel

__version__ = "0.0.3"


class MainWindow(wx.Frame):

    def __init__(self):
        super(MainWindow, self).__init__(None, size=(800, 600), title="Rainbow " + __version__)

        # Elements
        self.root = None
        self.load_menu()

        self.panel = wx.Panel(self)

        self.tree_view = wx.TreeCtrl(
            self.panel, size=(200, -1),
            style=wx.TR_DEFAULT_STYLE | wx.TR_HIDE_ROOT | wx.TR_FULL_ROW_HIGHLIGHT)

        self.control_panel = wx.lib.scrolledpanel.ScrolledPanel(self.panel)
        self.control_panel.SetupScrolling(scrollIntoView=False)

        self.class_panel = ClassPanel(self.control_panel)
        self.method_panel = MethodPanel(self.control_panel)
        self.attribute_panel = AttributePanel(self.control_panel)

        # Load tree images
        self.image_list = wx.ImageList(16, 16)
        self.class_image = self.image_list.Add(wx.Image(
            'rainbow/app/images/class.png',
            wx.BITMAP_TYPE_PNG).Scale(16, 16).ConvertToBitmap())
        self.method_image = self.image_list.Add(wx.Image(
            'rainbow/app/images/method.png',
            wx.BITMAP_TYPE_PNG).Scale(16, 16).ConvertToBitmap())
        self.attribute_image = self.image_list.Add(wx.Image(
            'rainbow/app/images/attribute.png',
            wx.BITMAP_TYPE_PNG).Scale(16, 16).ConvertToBitmap())
        self.tree_view.AssignImageList(self.image_list)

        # Layout
        contro_sizer = wx.BoxSizer(wx.HORIZONTAL)
        contro_sizer.Add(self.class_panel, 1, wx.ALL | wx.EXPAND, 5)
        contro_sizer.Add(self.method_panel, 1, wx.ALL | wx.EXPAND, 5)
        contro_sizer.Add(self.attribute_panel, 1, wx.ALL | wx.EXPAND, 5)
        self.control_panel.SetSizer(contro_sizer)

        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(self.tree_view, 0, wx.ALL | wx.EXPAND, 5)
        hsizer.Add(self.control_panel, 1, wx.ALL | wx.EXPAND, 5)
        self.panel.SetSizer(hsizer)

        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.panel, 1, wx.ALL | wx.EXPAND, 1)
        self.SetSizer(vsizer)

        self.Layout()

        # Events
        self.tree_view.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_item_selected)

    def load_menu(self):
        self.menu_bar = wx.MenuBar()
        self.menu_file = wx.Menu()
        self.menu_load_file = self.menu_file.Append(wx.NewId(), 'Load file')
        self.menu_file.AppendSeparator()
        self.menu_exit = self.menu_file.Append(wx.ID_EXIT, 'Exit')
        self.menu_bar.Append(self.menu_file, 'File')
        self.menu_edit = wx.Menu()
        self.menu_refresh = self.menu_edit.Append(wx.NewId(), 'Refresh')
        self.menu_bar.Append(self.menu_edit, 'Edit')
        self.SetMenuBar(self.menu_bar)

        self.Bind(wx.EVT_MENU, self.on_load_file, self.menu_load_file)
        self.Bind(wx.EVT_MENU, self.on_refresh, self.menu_refresh)
        self.Bind(wx.EVT_MENU, self.on_exit, self.menu_exit)

    def on_load_file(self, event):
        dlg = wx.FileDialog(self, 'Select rainbow file to load',
                            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        dlg.SetWildcard('Rainbow files (rainbow.py)|rainbow.py')
        if dlg.ShowModal() == wx.ID_OK:
            self.file_path = dlg.GetPath()
            self.initialize()
        dlg.Destroy()

    def on_refresh(self, event):
        # TODO
        self.initialize()

    def on_exit(self, event):
        self.Close(True)

    def initialize(self):
        self.root = load_rainbow(self.file_path)
        self.tree_view.DeleteAllItems()
        # Generate TreeView
        self.root_node = self.tree_view.AddRoot('Root')
        self.fill_node(self.root_node, self.root.__dict__)
        self.tree_view.ExpandAll()
        # Load instances in panels
        self.class_panel.load_root(self.root)
        self.method_panel.load_root(self.root)
        self.attribute_panel.load_root(self.root)
        # Hide all panels
        self.class_panel.Hide()
        self.method_panel.Hide()
        self.attribute_panel.Hide()
        self.Layout()

    def fill_node(self, node, dictionary):
        for key in dictionary.keys():
            if key[0] != '_':
                instance = dictionary[key]
                _type = type(instance)

                # Object instances -> class type
                # Non object instances -> types.InstanceType
                if 'class' in str(_type) or _type is types.InstanceType:
                    next_node = self.tree_view.AppendItem(node, key)
                    self.tree_view.SetItemImage(
                        next_node, self.class_image, wx.TreeItemIcon_Normal)
                    try:
                        self.fill_node(next_node, instance.__dict__)
                        self.fill_node(next_node, self.sort_dictionary(instance.__class__.__dict__))
                    except TypeError:
                        pass
                elif _type is types.MethodType or _type is types.FunctionType:
                    leave = self.tree_view.AppendItem(node, key)
                    self.tree_view.SetItemImage(leave, self.method_image, wx.TreeItemIcon_Normal)
                elif _type in [str, unicode, int, float, bool] or 'property' in str(_type):
                    leave = self.tree_view.AppendItem(node, key)
                    self.tree_view.SetItemImage(
                        leave, self.attribute_image, wx.TreeItemIcon_Normal)

    def sort_dictionary(self, dictionary):
        properties = collections.OrderedDict()
        functions = collections.OrderedDict()
        for key, value in dictionary.iteritems():
            if 'property' in str(value):
                properties[key] = value
            elif 'function' in str(value):
                functions[key] = value
        properties.update(functions)
        return properties

    def on_item_selected(self, event):
        path = self.get_item_path(event.GetItem())
        instance = '.'.join(path)
        _type = type(eval('self.root.' + instance))

        self.class_panel.Hide()
        self.method_panel.Hide()
        self.attribute_panel.Hide()

        if 'class' in str(_type) or _type is types.InstanceType:
            self.class_panel.set_item(instance)
            self.class_panel.Show()
        elif _type is types.MethodType or _type is types.FunctionType:
            self.method_panel.set_item(instance)
            self.method_panel.Show()
        elif _type in [str, unicode, int, float, bool]:
            self.attribute_panel.set_item(instance)
            self.attribute_panel.Show()

        self.Layout()

    def get_item_path(self, item):
        path = []
        while self.tree_view.GetItemParent(item):
            path = [self.tree_view.GetItemText(item)] + path
            item = self.tree_view.GetItemParent(item)
        return path
