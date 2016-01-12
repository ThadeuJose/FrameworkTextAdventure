from Framework.Item import Item
from Framework.Exceptions import *

__author__ = 'Thadeu Jose'


class MyTuple:

    def __init__(self, item, quantity=1):
        self.item = item
        self.quant = quantity

    @property
    def name(self):
        return self.item.name

    def __eq__(self, other):
        if isinstance(other, Item) and self.item == other:
            return True
        elif isinstance(other, str) and self.name.lower() == other.lower():
            return True
        return False

    def __str__(self):
        if self.quant>1:
            return self.name+" x "+str(self.quant)
        return self.name


class Inventory:

    def __init__(self):
        self.listItem = list()

    def add(self, item):
        if isinstance(item, Item):
            mytuple = MyTuple(item)
        elif isinstance(item, MyTuple):
            mytuple = item
        else:
            raise ItemException()

        if not list:
            self.listItem.append(mytuple)
        if item not in self:
            self.listItem.append(mytuple)
        else:
            for elem in self.listItem:
                if elem.item == item:#If you find the item
                    elem.quant += 1  #You put plus one in your quantity

    def __contains__(self, item):
        for elem in self.listItem:
            if elem == item:
                return True
        return False

    def __str__(self):
        return ", ".join(map(str, self.listItem))

    def take(self, item, quant=1):
        """Return the item and decrement one in the quantity"""
        if item in self:
            for elem in self.listItem:
                if elem == item:
                    if elem.quant-quant <= 0:
                        self.remove(elem.item)
                    else:
                        elem.quant -= quant
                    return elem.item
        raise ItemNotFoundException

    def remove(self, item):
        """Remove the item from the inventory"""
        if not self.listItem:
            raise EmptyInventoryException()
        if item not in self:
            raise ItemNotFoundException()
        else:
            for elem in self.listItem:
                if elem == item:
                    self.listItem.remove(elem)


