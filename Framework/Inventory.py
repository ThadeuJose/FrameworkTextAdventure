from Framework.Item import Item
from Framework.Exceptions import *

__author__ = 'Thadeu Jose'


class Inventory:
    def __init__(self):
        self.listItem=list()
        self.INITIAL_QUANTITY=1
        self.INDEX_ITEM=0
        self.INDEX_QUANTITY=1

    def addItem(self,item):
        if not isinstance(item,Item):
            raise ItemException()
        if not list:
            self.listItem.append(self._tuple(item,self.INITIAL_QUANTITY))
        if item not in self:
            self.listItem.append(self._tuple(item,self.INITIAL_QUANTITY))
        else:
            for i in self.listItem:
                if i[self.INDEX_ITEM]==item:#If you find the item
                    i[self.INDEX_QUANTITY]+=1#You put plus one in your quantity

    def _tuple(self,item,quantity):
        tuple=list()
        tuple.append(item)
        tuple.append(quantity)
        return tuple

    def __contains__(self, item):
        for i in self.listItem:
            if i[self.INDEX_ITEM]==item:
                return True
        return False

    def __str__(self):
        resp=''
        for i in self.listItem:
            resp+=i[self.INDEX_ITEM].name+"x"+str(i[self.INDEX_QUANTITY])+","
        return resp[0:len(resp)-1]

    def removeItem(self,item):
        if not isinstance(item,Item):
            raise ItemException()
        if not self.listItem:
            raise EmptyInventoryException()
        if item not in self:
            raise ItemNotFoundException()
        else:
            for i in self.listItem:
                if i[self.INDEX_ITEM]==item:
                    self.listItem.remove(i)
