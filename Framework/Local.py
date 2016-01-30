from Framework.Direction import DIRECTIONS, oppositedirection
from Framework.BaseTextObject import TextObject
from Framework.Constants import DIRECTION_NOT_VALID, DIRECTION_NOT_PERMITED
from Framework.Exceptions import DirectionNotFoundException, LocalAlreadyImplementException
from Framework.Manager import CommandManager

__author__ = 'Thadeu Jose'


class Local(TextObject):

    def __init__(self, title, description):
        TextObject.__init__(self, title, description)
        self._locals = dict()
        self.commandmanager = CommandManager()

    @property
    def title(self):
        return self.name

    @title.setter
    def title(self, value):
        self.name = value

    def __eq__(self, other):
        return self.title == other.title

    def __ne__(self, other):
        return self.title != other.title

    def addLocal(self, direction, local):
        if direction.lower() not in DIRECTIONS:
            raise DirectionNotFoundException()
        if direction.lower() in self._locals:
            raise LocalAlreadyImplementException()
        self._locals[direction.lower()] = local
        if direction not in self._locals:
            local.addLocal(oppositedirection(direction), self)

    def getlocal(self, direction):
        if direction.lower() not in DIRECTIONS:
            return DIRECTION_NOT_VALID
        if direction.lower() not in self._locals:
            return DIRECTION_NOT_PERMITED
        return self._locals[direction.lower()]

    def addcommand(self, idcommand, command):
        self.commandmanager.addcommand(idcommand, command)

    def execute(self, command, arg):
        return self.commandmanager.execute(command, arg)