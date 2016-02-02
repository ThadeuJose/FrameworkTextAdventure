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
    def __init__(self, name='Player', description='The player', inventory=Inventory()):
        TextObject.__init__(self, name, description)
        self._inventory = inventory
        self._commandmnager = CommandManager()
        self._commandmnager.addcommand(CommandConst.INV, Inv(None, None, self))

    def hascommand(self, idcommand):
        return self._commandmnager.hascommand(idcommand)

    def execute(self, command, args):
        return self._commandmnager.execute(command, args)

    def additem(self, item):
        """Add a item in player inventory."""
        self._inventory.add(item)

    def hasitem(self, item):
        return item in self._inventory

    def removeitem(self, item):
        self._inventory.remove(item)

    def quantitem(self):
        return len(self._inventory)

    def inventory(self):
        return str(self._inventory)


class NPC(TextObject):
    """Keep the information about a NPC"""
    def __init__(self, name, description):
        TextObject.__init__(self, name, description)
