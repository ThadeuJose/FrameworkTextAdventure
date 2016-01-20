from Framework.Game import Game
from Framework.Commands import Go
from Framework.Direction import adddirection

class MyGame(Game):

    def init(self):
        self.controller.addcommand("Entrance", "Go", ConditionalGo)
        self.controller.addcommand("Cave", "Go", ConditionalGo)
        self.controller.addcommand("Corridor", "Go", ConditionalGo)
        self.controller.addcommand("Hallway", "Go", ConditionalGo)
        self.controller.addcommand("Vault", "Go", ConditionalGo)
        self.controller.addcommand("Study", "Go", ConditionalGo)

        adddirection("Up", "Down")


class ConditionalGo(Go):
    def __init__(self, local, controller):
        Go.__init__(self, local, controller)

    def __call__(self, args):
        if self.local.name == 'Entrance':
            self.local.description = "You are in the Entrance.\nThe Cave is to the north."
        if self.local.name == 'Cave':
            self.local.description = "You are in the Cave.\n" \
                                     "The Corridor is to the east and the Entrance is to the south."
        if self.local.name == 'Corridor':
            self.local.description = "You are in the Corridor.\nThe Cave is to the east and the sign will tell " \
                                     "you where the next room is."
        if self.local.name == 'Hallway':
            self.local.description = "You are in the Hallway.\nBelow you is the Corridor and east of you is the door. " \
                                     "You can also see a box here."
        if self.local.name == 'Vault':
            self.local.description = "Here is a button and a gate that leads to the south.\n " \
                                     "To open the gate, you must push the button.\n " \
                                     "To press the button and open the gate, simply type 'push button'.\nGo ahead and try it now."
        if self.local.name == 'Study':
            self.local.description = "You are in the Study.\n" \
                                     "You see a portal to the west and a Wizard here.\nThe Vault is to the north."
        return Go.__call__(self, args)



game = Game("Tutorial.yaml", True)
game.run()
