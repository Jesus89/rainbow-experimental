# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2015 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import os
import sys
import imp
import uuid


class Root():
    pass


class NotRainbow(Exception):
    pass


def add_path(file_path):
    """ Add rainbow file path to Python path """
    path = os.path.dirname(file_path)
    sys.path.append(path)


def check_rainbow(rainbow_file):
    """ Check the integrity of a rainbow file """
    try:
        dic = rainbow_file.__dict__['__instances__']
        if isinstance(dic, dict):
            return dic
        else:
            raise Exception('Rainbow file must contain a dictionary')
    except KeyError:
        raise NotRainbow()


def build_root(dic):
    """ Create root class with rainbow file loaded """
    root = Root()
    root.__dict__ = dic
    return root


def load_rainbow(file_path):
    """ Load rainbow file """

    if os.path.exists(file_path + "c"):
        os.unlink(file_path + "c")

    if not os.path.exists(file_path):
        raise Exception("%s not found!" % file_path)

    add_path(file_path)
    module_id = uuid.uuid1()
    try:
        rainbow_file = imp.load_source("rainbow%s" % module_id, file_path)
        dic = check_rainbow(rainbow_file)
        root = build_root(dic)
        return root
    except:
        raise Exception("Unable to load %s" % file_path)
