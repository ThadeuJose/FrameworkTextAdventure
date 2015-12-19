from Framework.Item import Item
from Framework.Exceptions import *

__author__ = 'Thadeu Jose'


class Inventory:

    def __init__(self):
        self.listItem=list()
        self.INITIAL_QUANTITY=1
        self.INDEX_ITEM=0
        self.INDEX_QUANTITY=1

    def add(self,item,quant=1):
        if not isinstance(item,Item):
            raise ItemException()
        if not list:
            self.listItem.append(self._tuple(item,quant))
        if item not in self:
            self.listItem.append(self._tuple(item,quant))
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
        #todo make a test
        if not isinstance(item,Item):
            for i in self.listItem:
                if i[self.INDEX_ITEM].name.lower()==item:
                    return True
            return False
        for i in self.listItem:
            if i[self.INDEX_ITEM]==item:
                return True
        return False

    def __str__(self):
        #Quando precisar refazer vc pode usar uma high order function passando str
        resp=list()
        for i in self.listItem:
            if i[self.INDEX_QUANTITY]>1:
                resp.append(i[self.INDEX_ITEM].name+" x "+str(i[self.INDEX_QUANTITY]))
            else:
                resp.append(i[self.INDEX_ITEM].name)
        return ", ".join(resp)

    def take(self,item,quant=1):#Return the item and decrement one in the quantity
        for i in self.listItem:
            if i[self.INDEX_ITEM].name.lower()==item:
                resp = i[self.INDEX_ITEM]
                if i[self.INDEX_QUANTITY]-quant==0:
                    self.remove(resp)
                else:
                     i[self.INDEX_QUANTITY]-=quant#You take one in your quantity
                return resp
        raise ItemNotFoundException

    def remove(self,item):#Remove the item from the inventory
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
