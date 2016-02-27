from Framework.Actor import NPC
from Framework.Commands import Command
from Framework.Game import Game
from Framework.Item import Item
from Framework.Status import addstatus, getstatus, getallstatus


class MyGame(Game):

    def preprocess(self):
        self.commandfactory.addnewclass("craft", Craft)
        self.commandfactory.addnewtag("monster", self.makeMonster)

    def init(self):
        addstatus(self.controller.player, "HP", 20)

    def makeMonster(self, local):
        command = self.commandfactory.CommandArgs
        monster = NPC(command[0], command[1])
        addstatus(monster, "HP", command[2])
        addstatus(monster, "A", command[3])
        addstatus(monster, "D", command[4])
        addstatus(local, "Monster", monster)
        self.controller.addcommand(local.title, "Analyze", Analyze)


class Craft(Command):
    def function(self, args):
        if args[0].lower() == "sword":
            if self.controller.hasitem("wood"):
                self.controller.removeitem("wood")
                item = Item("Sword", "A wood sword")
                addstatus(item, "Damage", 1)
                self.controller.additem(item)
                return "You make a sword"
            return "You dont have the material"
        return "you cant do that"


class Analyze(Command):
    def function(self, args):
        monster = getstatus(self.local, "Monster")
        return monster.name + " "+ getallstatus(monster)

game = MyGame("Monster.yaml")
game.run()