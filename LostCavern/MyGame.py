from Framework.Game import Game
from Framework.Commands import Command, See, Go
from Framework.Item import Item
from Framework.Status import addstatus, getstatus, setstatus, getinventory

__author__ = 'Thadeu Jose'


class MyGame(Game):

    def preprocess(self):
        f = self.framework
        f.addcls("Light",Light)
        f.addcls("Pull", Pull)
        f.addcls("Shot", Shot)
        f.addcls("Observer", Observer)
        f.addcls("Tie", Tie)

    def init(self):
        f = self.framework
        f.addlocal(f.getlocal("Area 1"), "Go", Go1)
        f.addlocal(f.getlocal("Area 2"), "Go", Go2)

class Light(Command):
    def function(self, args):
        if self.framework.playerhas("wood"):
            self.framework.additemplayer('Torch', "A simple torch")
            self.framework.removeitemplayer("wood")
            return "You light a torch"
        return "You cant do this command"


class Pull(Command):
    def function(self, args):
        if args:
            if self.framework.playerhas('Torch') and args[0].lower() == 'lever':
                self.framework.setstatus(self.local, "pull_lever", True)
                return "You pull the lever"
        return "You cant do this command"


class Go1(Go):
    def function(self, args):
        if args:
            if self.framework.getstatus(self.local, "pull_lever") and args[0].lower() == 'east':
                return Go.function(self,args)
        return "You cant go in this direction"


class Observer(Command):
    def function(self, args):
        if args:
            if args[0].lower() == 'ground':
                self.framework.setstatus(self.local,"analise_ground", True)
                return "percebeu um buraco consideravelmente grande. Nele tem algumas pedras pontiagudas no chao " \
                       "alem de algumas ervas que podem ser uteis"
            if args[0].lower() == 'hole' and self.framework.getstatus(self.local,"analise_ground"):
                self.framework.setstatus(self.local, "analise_hole", True)
                return "existe um cantil e uma corda no interior do buraco"
        return "You cant do this command"


class Shot(Command):
    def function(self, args):
        if self.framework.playerhas('Stones'):
            self.framework.setstatus(self.local,"shot_stone", True)
            return "As pedras soltaram as estalactites que cairam nos morcegos. Os morcegos se afastaram" \
                    " da passagem. É possível ver uma luz que aponta para um desfiladeiro"
        return "You cant do this command"


class Tie(Command):
    def function(self, args):
        if self.framework.playerhas('Rope') and self.framework.getstatus(self.local, "shot_stone"):
            return "amarrou a corda e pode descer o desfiladeiro"
        return "You cant do this command"


class Go2(Go):
    def __call__(self,args):
        if args:
            if self.framework.getstatus(self.local, "shot_stone") and args[0].lower() == 'north':
                return "Voce desceu o desfiladeiro e pode avancar\n" +  Go.function(self,args)
        return "You cant go in this direction"


myGame = MyGame("LostCavern.yaml")
myGame.run()#"inputf.txt")