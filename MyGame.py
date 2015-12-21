from Framework.Game import Game
from Framework.Commands import Command, See
from Framework.Item import Item
from Framework.Status import addstatus, getstatus, setstatus, getinventory

__author__ = 'Thadeu Jose'


class MyGame(Game):

    def init(self):
        addstatus(self.controller.getlocal("Area 1"), "pull_lever", False)
        self.controller.addcommand("Area 1", "Light", Light)
        self.controller.addcommand("Area 1", "Pull", Pull)
        self.controller.addcommand("Area 1", "Go", Go1)
        self.controller.addcommand("Area 1", "See", See)

        addstatus(self.controller.getlocal("Area 2"), "shot_stone", False)
        addstatus(self.controller.getlocal("Area 2"), "analise_ground", False)
        addstatus(self.controller.getlocal("Area 2"), "analise_hole", False)
        self.controller.addcommand("Area 2", "Go", Go2)
        self.controller.addcommand("Area 2", "Shot", Shot)
        self.controller.addcommand("Area 2", "Observer", Observer)
        self.controller.addcommand("Area 2", "Get", Get)
        self.controller.addcommand("Area 2", "Tie", Tie)


class Light(Command):
    def __init__(self,local,controller):
        Command.__init__(self,local,controller)

    def __call__(self,args):
        if self.controller.player_has(Item('Wood',"A piece of wood")):
            self.controller.setitem(Item('Torch',"A simple torch"))
            self.controller.removeitem(Item("Wood","A piece of wood"))
            return "You light a torch"
        return "You cant do this command"


class Pull(Command):
    def __init__(self,local,controller):
        Command.__init__(self,local,controller)

    def __call__(self,args):
        if self.controller.player_has(Item('Torch',"A simple torch")) and args[0].lower() == 'lever':
            setstatus(self.local, "pull_lever", True)
            return "You pull the lever"
        return "You cant do this command"


class Go1(Command):
    def __init__(self,local,controller):
        Command.__init__(self,local,controller)

    def __call__(self,args):
        if getstatus(self.local, "pull_lever") and args[0].lower()=='east':
            self.controller.currentLocal=self.local.getlocal(args[0])
            return self.controller.currentLocal.__str__()
        return "You cant go in this direction"


class Get(Command):
    def __init__(self, local, controller):
        Command.__init__(self, local, controller)

    def __call__(self, args):
        inventory = getinventory(self.local,self.local.DEFAULT_INVENTORY)
        if inventory:
            collectable = list()
            resp = " ".join(args)
            if resp in inventory and getstatus(self.local, "analise_ground"):
                collectable.extend(['herb', 'stones'])
            if resp in inventory and getstatus(self.local, "analise_hole"):
                collectable.extend(['rope', 'flask'])
            if resp.lower() in collectable:
                self.controller.setitem(inventory.take(resp))
                return "You sucessful get "+resp.capitalize()
            return "You cant get the item"
        return "There is nothing to get here"


class Observer(Command):
    def __init__(self,local,controller):
        Command.__init__(self,local,controller)

    def __call__(self,args):
        if args[0].lower() == 'ground':
            setstatus(self.local,"analise_ground", True)
            return "percebeu um buraco consideravelmente grande. Nele tem algumas pedras pontiagudas no chao " \
                   "alem de algumas ervas que podem ser uteis"
        if args[0].lower() == 'hole' and getstatus(self.local,"analise_ground"):
            setstatus(self.local, "analise_hole", True)
            return "existe um cantil e uma corda no interior do buraco"
        return "You cant do this command"



class Shot(Command):
    def __init__(self,local,controller):
        Command.__init__(self,local,controller)

    def __call__(self,args):
        if self.controller.player_has(Item('Stones',"A simple stone")):
            setstatus(self.local,"shot_stone", True)
            return "As pedras soltaram as estalactites que cairam nos morcegos. Os morcegos se afastaram" \
                    " da passagem. É possível ver uma luz que aponta para um desfiladeiro"
        return "You cant do this command"


class Tie(Command):
    def __init__(self,local,controller):
        Command.__init__(self,local,controller)

    def __call__(self,args):
        if self.controller.player_has(Item('Rope','1.2m of rope ')) and getstatus(self.local, "shot_stone"):
            return "amarrou a corda e pode descer o desfiladeiro"
        return "You cant do this command"


class Go2(Command):
    def __init__(self,local,controller):
        Command.__init__(self,local,controller)

    def __call__(self,args):
        if getstatus(self.local, "shot_stone") and args[0].lower() == 'north':
            self.controller.currentLocal=self.local.getlocal(args[0])
            return "Voce desceu o desfiladeiro e pode avancar\n" +self.controller.currentLocal.__str__()
        return "You cant go in this direction"


myGame = MyGame("LostCavern.yaml")
myGame.run("inputf.txt")