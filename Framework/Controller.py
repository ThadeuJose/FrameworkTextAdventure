"""Contain the classes who control all the game"""
from Framework.Commands import Inv
from Framework.Constants import CommandConst
from Framework.Local import Local
from Framework.Exceptions import IncorrectTypeException

__author__ = 'Thadeu Jose'


class Controller:
    """Control the interation between the game and the rest of the framework"""
    def __init__(self, game, world, player, factory):
        self.player = player
        self.world = world
        self.factory = factory
        self.framework = None
        self.player.addcommand(CommandConst.INV, Inv(None, self, self.framework))
        self._game = game
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

    def additem(self, item):
        self.player.add(item)

    def hasitem(self, item):
        return self.player.hasitem(item)

    def removeitem(self, item):
        self.player.remove(item)

    def takeitem(self,item):
        return self.player.takeitem(item)

    def quantitem(self):
        return self.player.quantitem()

    def inventory(self):
        return self.player.printInventory()

    def getlocal(self,name):
        return self.world.getlocal(name)

    def endgame(self, message=None):
        self._game.endgame(message)

    def addcommand(self, local, idcommand, command):
        """Add a command in a local"""
        mylocal = self.world.getlocal(local) if isinstance(local, str) else local
        mycommand = command(mylocal, self,self.framework)
        mylocal.addcommand(idcommand, mycommand)

    def execute(self, command, args):
        """Execute the command"""
        return self.player.execute(command, args) if self.player.hascommand(
                command) else self.currentlocal.execute(command, args)

