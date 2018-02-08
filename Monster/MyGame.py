from Framework.Actor import NPC
from Framework.Commands import Command
from Framework.Game import Game
from Framework.Item import Item
from Framework.Status import addstatus, getstatus, getallstatus
from Framework.Tag import Tag


class MyGame(Game):

    def preprocess(self):
        self.framework.addcls("craft", Craft)
        self.framework.addcls("monster", Monster)
        self.framework.addcls("talk",Talk)

    def init(self):
        self.framework.addplayerstatus("Player", "HP", 20)
        self.framework.addplayerstatus("Player", "A", 2)
        self.framework.addplayerstatus("Player", "D", 0)


class Monster(Tag):
    def make(self):
        monster = self.framework.createtextobject(self.args[0], self.args[1],
                                                   {"HP": self.args[2], "A": self.args[3], "D": self.args[4]})
        self.framework.addlocal(self.local, self.args[0], monster)
        self.framework.addlocal(self.local, "Analyze", Analyze)
        self.framework.addlocal(self.local, "Attack", Attack)


class Attack(Command):
    def function(self, args):
        f = self.framework
        player = f.getplayer()
        monster = f.gettextobject(self.local,"Rabbit")

        hpplayer = f.getstatus(player,"HP")
        atkplayer = f.getstatus(player,"A")
        defplayer = f.getstatus(player,"D")

        hpmonster = f.getstatus(monster,"HP")
        atkmonster = f.getstatus(monster,"A")
        defmonster = f.getstatus(monster,"D")

        if hpmonster>0:
            hpplayer = hpplayer -( atkmonster - defplayer)
            hpmonster = hpmonster - (atkplayer - defmonster)
            f.setstatus(player,"HP",hpplayer)
            f.setstatus(monster,"HP",hpmonster)
            return "You attack\n HP Player "+ str(hpplayer) +" HP Monster "+str(hpmonster)
        else:
            return "There is nothing to attack here"


class Talk(Command):
    def function(self, args):
        if args:
            if args[0].lower() == "mi":
                return "Mi - Hi"
            if args[0].lower() == "ki":
                return "Ki - Hello"
        return "choose who you want to speak"


class Craft(Command):
    def function(self, args):
        if args:
            if args[0].lower() == "sword":
                if self.framework.playerhas("wood"):
                    self.framework.removeitemplayer("wood")
                    self.framework.additemplayer("Sword", "A wood sword", {"Damage": 1})
                    return "You make a sword"
                return "You don't have the material"
        return "you cant do that"


class Analyze(Command):
    def function(self, args):
        monster = self.framework.gettextobject(self.local, "Rabbit")
        return monster.name + " " + self.framework.getallstatus(monster)

game = MyGame("Monster.yaml")
game.run("inputf.txt")