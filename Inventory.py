__author__ = 'Thadeu Jose'

class Inventory:
    def __init__(self):
        self.listItem=list()
        self.INITIAL_QUANTITY=1
        self.INDEX_ITEM=0
        self.INDEX_QUANTITY=1

    def addItem(self,item):
        #TODO
        #Checar se o tipo é item
        #Testar se funciona
        if not list:
            self.listItem.append(list(item,self.INITIAL_QUANTITY))
        if item not in self.listItem:
            self.listItem.append(list(item,self.INITIAL_QUANTITY))
        else:
            for i in self.listItem:
                if i[self.INDEX_ITEM]==item:#If you find the item
                    i[self.INDEX_QUANTITY]+=1#You put plus one in your quantity

    def removeItem(self,item):
        #TODO
        #Checar se o tipo é item
        #Testar se funciona
        if not list:
            pass#raiseException Lista vazia
        if item not in self.listItem:
            pass#raiseException item não se encontra na lista
        else:
            for i in self.listItem:
                if i[self.INDEX_ITEM]==item:
                    self.listItem.remove(i)
