"""Create all the NPC"""

from Framework.Inventory import Inventory

__author__ = 'Thadeu Jose'


#TODO Herdar de textObject com nome default
class Player:
    """Manage the player"""
    def __init__(self, name=None, description=None, inventory=Inventory()):
        self.name = name
        self.description = description
        self.inventory = inventory

    def additem(self, item):
        """Add a item in player inventory."""
        self.inventory.add(item)
