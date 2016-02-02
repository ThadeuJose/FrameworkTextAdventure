from Framework.Item import Item
from Framework.Exceptions import *

__author__ = 'Thadeu Jose'


class MyTuple:
    """Mutable Tuple"""
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
        return self.name if self.quant > 1 else self.name + " x " + str(self.quant)


class Inventory:
    """Manage the inventory"""
    def __init__(self):
        self.listItem = list()
        self.index = 0

    def add(self, item):
        """Add a item if a item already exist you add one in the quantity"""
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
                if elem.item == item:  # If you find the item
                    elem.quant += 1  # You put plus one in your quantity

    def take(self, item, quant=1):
        """Return the item and decrement one in the quantity
        If quantity equal 0 the item is remove
        """
        if item in self:
            for elem in self.listItem:
                if elem == item:
                    if elem.quant - quant <= 0:
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

    def __len__(self):
        return len(self.listItem)

    def __contains__(self, item):
        for elem in self.listItem:
            if elem == item:
                return True
        return False

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.listItem[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

    def __str__(self):
        return ", ".join(map(str, self.listItem))
