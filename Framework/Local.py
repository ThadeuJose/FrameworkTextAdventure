from Framework.Exceptions import *
from Framework.Direction import directions,oppositeDirection
from Framework.Inventory import Inventory
from Framework.BaseTextObject import TextObject
from Framework.Commands import Go
from Framework.Constants import *

__author__ = 'Thadeu Jose'


class Local(TextObject):

    def __init__(self, title, description,controller):
        #TODO
        #Testar
        TextObject.__init__(self, title, description)
        self._locals=dict()
        self._commands=dict()#Dictionary contain all the command of the room index by the command
        self._commands['go']=Go(self,controller)

    @property
    def title(self):
        return self.name

    @title.setter
    def title(self, value):
        self.name=value

    def __eq__(self, other):
        return self.title==other.title

    def __ne__(self, other):
        return self.title!=other.title

    def addLocal(self,direction,Local):
        #TODO
        #Testar
        if direction.lower() not in directions:
            raise DirectionNotFoundException()
        if direction.lower() in self._locals:
            raise LocalAlreadyImplementException
        self._locals[direction.lower()]=Local
        if direction not in self._locals:
            Local.addLocal(oppositeDirection(direction),self)

    def getLocal(self,direction):
        if direction.lower() not in directions:
            return DIRECTION_NOT_VALID
        if direction.lower() not in self._locals:
            return DIRECTION_NOT_PERMITED
        return self._locals[direction.lower()]

    def exec(self,command,args):
        if command not in self._commands:
            return COMMAND_NOT_EXECUTABLE
        return self._commands[command](args)

    def __str__(self):
        return self.name+"\n"+self.description


class LocalWithItem(Local):

    def __init__(self,title,description,controller):
        Local.__init__(self,title,description,controller)
        self.inventory=Inventory()

    def __init__(self,local):
        Local.__init__(self,local.title,local.description)
        self.inventory=Inventory()

    def addItem(self,item):
        #TODO
        #Testar
        #Ver se existe exception
        self.inventory.addItem(item)