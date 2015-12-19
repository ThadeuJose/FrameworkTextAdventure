from Framework.Exceptions import *
from Framework.Direction import DIRECTIONS,oppositedirection
from Framework.BaseTextObject import TextObject
from Framework.Commands import Go
from Framework.Constants import *
from Framework.Status import Status

__author__ = 'Thadeu Jose'



class Local(TextObject):

    def __init__(self, title, description,controller):
        TextObject.__init__(self, title, description)
        self._locals=dict()
        self._commands=dict()#Dictionary contain all the command of the room index by the command
        self._commands[COMMAND_GO]=Go(self,controller)
        self._status=Status()

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
        if direction.lower() not in DIRECTIONS:
            raise DirectionNotFoundException()
        if direction.lower() in self._locals:
            raise LocalAlreadyImplementException
        self._locals[direction.lower()]=Local
        if direction not in self._locals:
            Local.addLocal(oppositedirection(direction),self)

    def getLocal(self,direction):
        if direction.lower() not in DIRECTIONS:
            return DIRECTION_NOT_VALID
        if direction.lower() not in self._locals:
            return DIRECTION_NOT_PERMITED
        return self._locals[direction.lower()]

    def addcommand(self,idcommand,command):
        #todo checar se e mesmo um command
        self._commands[idcommand.lower()]=command
    #todo falta o removecommand

    def exec(self,command,args):
        if command not in self._commands:
            return COMMAND_NOT_EXECUTABLE
        return self._commands[command](args)

    def __str__(self):
        return self.name+"\n"+self.description

