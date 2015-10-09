# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

# Import your modules here:
import rainbow.modules.example


# Root class
class Root():

    def __init__(self):
        self.initialize()

    def initialize(self):
        # Load your instances here:
        self.test1 = rainbow.modules.example.MyClass()
        self.test2 = rainbow.modules.example.A()

    def reload(self):
        reload(rainbow.modules.example)
        self.initialize()
