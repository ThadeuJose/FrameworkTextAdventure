from Framework.Inventory import Inventory

__author__='Thadeu Jose'

class Player:

    def __init__(self, name=None, description=None, inventory=Inventory()):
        self.name = name
        self.description = description
        self.inventory = inventory

    def getItem(self, item):
        self.inventory.add(item)
