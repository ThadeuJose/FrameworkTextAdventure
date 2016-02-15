from Framework.Actor import NPC
from Framework.Commands import Command
from Framework.Game import Game
from Framework.Item import Item
from Framework.Status import addstatus


class MyGame(Game):

    def preprocess(self):
        self.commandfactory.addmakefunction("craft", self.makeCraft)
        self.commandfactory.addmakefunction("monster", self.makeMonster)

    def init(self):
        addstatus(self.controller.player, "HP", 20)

    def makeCraft(self, local):
        self.controller.addcommand(local.title, "craft", Craft)


    def makeMonster(self, local):
        command = self.commandfactory._command
        monster = NPC(command[1], command[2])
        addstatus(monster, "HP", command[3])
        addstatus(monster, "A", command[4])
        addstatus(monster, "D", command[5])
        addstatus(local, "Monster", monster)
        self.controller.addcommand(local.title, "Attack", Attack)


class Craft(Command):

    def __call__(self, args):
        if args[0].lower() == "sword":
            if self.controller.hasitem("wood"):
                self.controller.removeitem("wood")
                item = Item("Sword","A wood sword")
                addstatus(item, "Damage", 1)
                self.controller.additem(item)
                return "You make a sword"
            return "You dont have the material"
        return "you cant do that"


class Attack(Command):
    def __call__(self, args):
        sword = self.controller.takeitem("Sword")
        if not sword:
            return "You cant attack"


game = MyGame("Monster.yaml")
game.run()