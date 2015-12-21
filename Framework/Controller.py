from Framework.Local import Local
from Framework.Exceptions import IncorrectTypeException

__author__ = 'Thadeu Jose'


class Controller:

    def __init__(self,world,player):
        #TODO
        #Testar
        self.player=player
        self.world = world
        self._currentLocal = None
        self._endingLocals = list()

    @property
    def currentLocal(self):
        return self._currentLocal

    @currentLocal.setter
    def currentLocal(self, value):
        if isinstance(value, Local):
            self._currentLocal = value
        else:
            raise IncorrectTypeException('Local')

    def endinglocal(self, local):
        self._endingLocals.append(local)

    def isendinglocal(self, local):
        return local in self._endingLocals

    def getlocal(self, title):
        return self.world.getlocal(title)

    def addcommand(self, local, idcommand, command):
        if isinstance(local, str):
            mylocal = self.world.getlocal(local)
            mylocal.addcommand(idcommand, command(mylocal, self))
        elif isinstance(local, Local):
            local.addcommand(idcommand, command(local, self))

    def player_has(self, item):
        return item in self.player.inventory

    def setitem(self, item):
        self.player.inventory.add(item)

    def removeitem(self, item):
        self.player.inventory.remove(item)

    def execute(self, command, args):
        return self.currentLocal.execute(command, args)
