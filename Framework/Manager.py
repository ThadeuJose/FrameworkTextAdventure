from Framework.Constants import COMMAND_NOT_EXECUTABLE

__author__ = 'Thadeu Jose'


class CommandManager:

    def __init__(self):
        self._commands = dict()

    def addcommand(self, idcommand, command):
        self._commands[idcommand.lower()] = command

    def hascommand(self,idcommand):
        return idcommand.lower() in self._commands

    def execute(self, command, args):
        mycommand = command.lower()
        if mycommand not in self._commands:
            return COMMAND_NOT_EXECUTABLE
        return self._commands[mycommand](args)