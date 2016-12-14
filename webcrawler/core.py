# -*- coding: utf-8 -*-
from threading import Thread
from webcrawler.configmanager import ConfigManager
import os

class Controller(Thread):
    def __init__(self):
        super().__init__()
        print(os.path.realpath)
        self.config=ConfigManager(os.path.realpath)

    def run(self):
        print("ok")
        pass