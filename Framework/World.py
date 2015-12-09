from Framework.Exceptions import LocalNotImplementException,IncorrectTypeException
from Framework.Local import Local

__author__ = 'Thadeu Jose'


class World:

    def __init__(self,title=None,description=None):
        self.title=title
        self.description=description
        self._dictLocal=dict()

    def addLocal(self,local):
        if isinstance(local,Local):
            self._dictLocal[local.title]=local
        else:
            raise IncorrectTypeException('Local')

    def getLocal(self,title):
        if title not in self._dictLocal:
            raise LocalNotImplementException()
        return self._dictLocal[title]

    def __str__(self):
        return self.title+"\n"+self.description
