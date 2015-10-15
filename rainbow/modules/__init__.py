# -*- coding: utf-8 -*-
# This file is part of the Rainbow Project

# Import your modules here:
import rainbow.modules.example
import rainbow.modules.comms


# Root class
class Root():

    def __init__(self):
        self.initialize()

    def initialize(self):
        # Load your instances here:
        self.myclass = rainbow.modules.example.MyClass()
        self.comms = rainbow.modules.comms.Comms()

    def reload(self):
        # Reload your modules here:
        reload(rainbow.modules.example)
        reload(rainbow.modules.comms)
        self.initialize()
