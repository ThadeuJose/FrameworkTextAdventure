"""Contain the classes who control all the game"""
from Framework.Commands import Command, Inv
from Framework.Constants import CommandConst
from Framework.Inventory import Inventory
from Framework.Local import Local
from Framework.Exceptions import IncorrectTypeException
from Framework.Manager import CommandManager

__author__ = 'Thadeu Jose'


class Controller:
    """Control the interation between the game and the rest of the framework"""
    def __init__(self, game, world, player, factory):
        self.player = player
        self.playerinventory = Inventory()
        self.playercommandmanager = CommandManager()
        self.world = world
        self.factory = factory
        self.framework = None
        self.playercommandmanager.addcommand(CommandConst.INV, Inv(None, self, self.framework))
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
        self.playerinventory.add(item)

    def hasitem(self, item):
        return item in self.playerinventory

    def removeitem(self, item):
        self.playerinventory.remove(item)

    def takeitem(self,item):
        return self.player.takeitem(item)

    def quantitem(self):
        return len(self.playerinventory)

    def inventory(self):
        return str(self.playerinventory)

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
        return self.playercommandmanager.execute(command, args) if self.playercommandmanager.hascommand(
                command) else self.currentlocal.execute(command, args)

