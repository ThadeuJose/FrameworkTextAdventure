from Framework.Exceptions import *
from Framework.Direction import Direction
from Framework.Inventory import Inventory
from Framework.BaseTextObject import TextObject
from Framework.Commands import Go

__author__ = 'Thadeu Jose'


class Local(TextObject):

    def __init__(self, title, description):
        TextObject.__init__(self, title, description)
        self._locals=dict()
        self.direc=Direction()
        self._commands=dict()#Dictionary contain all the command of the room index by the command
        self._commands['go']=Go(self)

    @property
    def title(self):
        return self.name

    @title.setter
    def title(self, value):
        self.name=value

    def addLocal(self,direction,Local):
        #TODO
        #Testar
        if direction.lower() not in self.direc:
            raise DirectionNotFoundException()
        if direction.lower() not in self._locals:
            raise LocalNotImplementException()

        self._locals[direction.lower()]=Local
        Local.addLocal(self.direc.oppositeDirection(direction),self)

    def getLocal(self,direction):
        #TODO
        #Testar
        if direction.lower() not in self.direc:
            raise DirectionNotFoundException()
        if direction.lower() not in self._locals:
            raise LocalNotImplementException()
        return self._locals[direction.lower()]

    def execute(self,command,args):
        #TODO
        #Testar
        if command not in self._commands:
            raise CommandNotFoundException()
        return self._commands[command](args)

    def __str__(self):
        return self.name+"\n"+self.description


class LocalWithItem(Local):

    def __init__(self,title,description):
        Local.__init__(self,title,description)
        self.inventory=Inventory()

    def __init__(self,local):
        Local.__init__(self,local.title,local.description)
        self.inventory=Inventory()

    def addItem(self,item):
        #TODO
        #Testar
        #Ver se existe exception
        self.inventory.addItem(item)