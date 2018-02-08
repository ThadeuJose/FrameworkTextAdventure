"""Create player and all NPC """
from Framework.Commands import Inv
from Framework.Constants import CommandConst
from Framework.Inventory import Inventory
from Framework.BaseTextObject import TextObject
from Framework.Item import Item
from Framework.Manager import CommandManager

__author__ = 'Thadeu Jose'


class Player(TextObject):
    """Manage the player"""
    def __init__(self, name='Player', description='The player'):
        TextObject.__init__(self, name, description)
        self.inventory = Inventory()
        self.commandmanager = CommandManager()
        self.commandmanager.addcommand(CommandConst.INV, Inv(None, None, self))

    def add(self,item):
        self.inventory.add(item)

    def hasitem(self,item):
        return item in self.inventory

    def hascommand(self, idcommand):
        return self._commandmnager.hascommand(idcommand)

    def remove(self,item):
        self.inventory.remove(item)

    def takeitem(self,item):
        return self.inventory.takeitem(item)

    def quantitem(self):
        return len(self.inventory)

    def printInventory(self):
        return str(self.inventory)

    def addcommand(self,idcommand,command):
        self.commandmanager.addcommand(idcommand,command)

    def hascommand(self,idcommand):
        self.commandmanager.hascommand(idcommand)

    def execute(self, command, args):
        return self.commandmnager.execute(command, args)


class NPC(TextObject):
    """Keep the information about a NPC"""
    def __init__(self, name, description):
        TextObject.__init__(self, name, description)
