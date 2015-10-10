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
        self.myclass = rainbow.modules.example.MyClass()

    def reload(self):
        # Reload your modules here:
        reload(rainbow.modules.example)
        self.initialize()
