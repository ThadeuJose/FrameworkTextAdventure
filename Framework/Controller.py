"""Contain the classes who control all the game"""

from Framework.Local import Local
from Framework.Exceptions import IncorrectTypeException
from Framework.Direction import DIRECTIONS

__author__ = 'Thadeu Jose'


class Controller:
    """Control the interation between the game and the rest of the framework"""
    def __init__(self, world, player):
        #TODO
        #Testar
        self.player = player
        self.world = world
        self._currentLocal = None
        self._endingLocals = list()

    @property
    def currentlocal(self):
        """Define the local where the player is"""
        return self._currentLocal

    @currentlocal.setter
    def currentlocal(self, value):
        if isinstance(value, Local):
            self._currentLocal = value
        else:
            raise IncorrectTypeException('Local')

    def addendinglocal(self, local):
        """Add the places where the game end"""
        self._endingLocals.append(local)

    def isendinglocal(self, local):
        """Check if a local is a ending place
        if is the game should stop"""
        return local in self._endingLocals

    def getlocal(self, title):
        """Return the local based in the title"""
        return self.world.getlocal(title)

    def addcommand(self, local, idcommand, command):
        """Add a command in a local"""
        mylocal = self.world.getlocal(local) if isinstance(local, str) else local
        mylocal.addcommand(idcommand, command(mylocal, self))

    #todo make this method in player class
    def player_has(self, item):
        return item in self.player.inventory

    def setitem(self, item):
        self.player.inventory.add(item)

    def removeitem(self, item):
        self.player.inventory.remove(item)

    def execute(self, command, args):
        """Execute the command in the current local"""
        return self.currentlocal.execute(command, args)

