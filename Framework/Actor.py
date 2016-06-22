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
        #self._commandmnager.addcommand(CommandConst.INV, Inv(None, None, self))

    def hascommand(self, idcommand):
        return self._commandmnager.hascommand(idcommand)

    def execute(self, command, args):
        return self._commandmnager.execute(command, args)


class NPC(TextObject):
    """Keep the information about a NPC"""
    def __init__(self, name, description):
        TextObject.__init__(self, name, description)
