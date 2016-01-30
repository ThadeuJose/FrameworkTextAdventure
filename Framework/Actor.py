"""Create player and all NPC """

from Framework.Inventory import Inventory
from Framework.BaseTextObject import TextObject

__author__ = 'Thadeu Jose'

class Player(TextObject):
    """Manage the player"""
    def __init__(self, name='Player', description='The player', inventory=Inventory()):
        TextObject.__init__(self, name, description)
        self.inventory = inventory

    def additem(self, item):
        """Add a item in player inventory."""
        self.inventory.add(item)

    def has(self, item):
        return item in self.inventory

    def removeitem(self, item):
        self.inventory.remove(item)

class NPC(TextObject):
    """Keep the information about a NPC"""
    def __init__(self, name, description):
        TextObject.__init__(self, name, description)
