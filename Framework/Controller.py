from Framework.Local import Local
from Framework.Exceptions import IncorrectTypeException

__author__ = 'Thadeu Jose'


class Controller:

    def __init__(self,world,player):
        #TODO
        #Testar
        self.player=player
        self.world = world
        self._currentLocal = None
        self.COMMAND_GO="go"

    @property
    def currentLocal(self):
        return self._currentLocal

    @currentLocal.setter
    def currentLocal(self, value):
        if isinstance(value,Local):
            self._currentLocal=value
        else:
            raise IncorrectTypeException('Local')

    def exec(self,command,args):
        return self.currentLocal.exec(command,args)
