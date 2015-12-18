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

    @property
    def currentLocal(self):
        return self._currentLocal

    @currentLocal.setter
    def currentLocal(self, value):
        if isinstance(value,Local):
            self._currentLocal=value
        else:
            raise IncorrectTypeException('Local')

    def addCommand(self,localtitle,idcommand,command):
        local = self.world.getLocal(localtitle)
        local.addcommand(idcommand,command(local,self))

    def player_has(self,item):
        return item in self.player.inventory

    def setitem(self,item):
        self.player.inventory.add(item)

    def removeItem(self,itemname):
        self.player.inventory.remove(itemname)

    def exec(self,command,args):
        return self.currentLocal.exec(command,args)
