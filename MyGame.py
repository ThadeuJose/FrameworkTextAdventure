__author__ = 'Thadeu Jose'

from Framework.Game import Game
from Framework.Commands import Command,See
from Framework.Item import Item
from Framework.Status import addstatus,getstatus

class MyGame(Game):

    def init(self):
        addstatus(self.controller.getLocal("Start"),"pull_lever",False)
        self.controller.addcommand("Start","Light",Light)
        self.controller.addcommand("Start","Pull",Pull)
        self.controller.addcommand("Start","Go",Go)
        self.controller.addcommand("Start","See",See)
        self.controller.setitem(Item("Wood","A piece of wood"))
        item1=Item("Knife","A Simple Knife")
        addstatus(item1,"Damage","1")

class Light(Command):
    def __init__(self,local,controller):
        Command.__init__(self,local,controller)

    def __call__(self,args):
        if self.controller.player_has("Wood"):
            self.controller.setitem(Item('Torch',"A simple torch"))
            self.controller.removeItem(Item("Wood","A piece of wood"))
            return "You light a torch"
        return "You cant do this command"

class Pull(Command):
    def __init__(self,local,controller):
        Command.__init__(self,local,controller)

    def __call__(self,args):
        if self.controller.player_has(Item('Torch',"A simple torch")) and args[0].lower()=='lever':
            self.local.setstatus("pull_lever",True)
            return "You pull the lever"
        return "You cant do this command"

class Go(Command):
    def __init__(self,local,controller):
        Command.__init__(self,local,controller)

    def __call__(self,args):
        if getstatus(self.local, "pull_lever") and args[0].lower()=='east':
            self.controller.currentLocal=self.local.getLocal(args[0])
            return self.controller.currentLocal.__str__()
        return "You cant go in this direction"

myGame=MyGame("LostCavern.yaml")
myGame.run()