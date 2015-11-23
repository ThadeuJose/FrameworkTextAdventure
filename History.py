__author__ = 'Thadeu Jose'

import Local

class World:
    def __init__(self,title=None,description=None):
        self.title=title
        self.description=description
        self.dictLocal=dict()

    def addLocal(self,Local):
        self.dicLocal[Local.title]=Local

    def getLocalDescription(self,title):
        return self.dictLocal[title]

