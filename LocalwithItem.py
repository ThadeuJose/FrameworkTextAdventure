__author__ = 'Thadeu Jose'

import Local,Inventory


class LocalWithItem(Local):

    def __init__(self,title,description):
        self.title=title
        self.description=description
        self.inventory=Inventory()

    def addItem(self,item):
        #TODO
        #Testar
        #Ver se existe exception
        self.inventory.addItem(item)

