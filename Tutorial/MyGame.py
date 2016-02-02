from Framework.Commands import Command,Go
from Framework.Direction import adddirection
from Framework.Game import Game
from Framework.Status import setstatus, getstatus


class MyGame(Game):

    def preprocess(self):
        adddirection("up", "down")
        adddirection("portal", "ectasy")

    def init(self):
        self.controller.addcommand("Entrance", "Go", ConditionalGo)
        self.controller.addcommand("Cave", "Go", ConditionalGo)
        self.controller.addcommand("Corridor", "Go", ConditionalGo)
        self.controller.addcommand("Hallway", "Go", ConditionalGo)
        self.controller.addcommand("Vault", "Go", ConditionalGo)
        self.controller.addcommand("Vault","Push",Push)
        self.controller.addcommand("Study", "Go", ConditionalGo)
        self.controller.addcommand("Study","Show",Show)


class ConditionalGo(Go):
    def __init__(self, local, controller):
        Go.__init__(self, local, controller)

    def __call__(self, args):
        if self.local.name == 'Entrance' and args[0].lower() == 'north':
            self.local.description = ('You are in the Entrance.\n'
                                      'The Cave is to the north.')
        if self.local.name == 'Cave' and args[0].lower() == 'east':
            self.local.description = ('You are in the Cave.\n'
                                      'The Corridor is to the east and the Entrance is to the south.')
        if self.local.name == 'Corridor' and args[0].lower() == 'up':
            self.local.description = ('You are in the Corridor.\n'
                                      'The Cave is to the east and the sign will tell '
                                      'you where the next room is.')
        if self.local.name == 'Hallway' and self.controller.hasitem("Key") and args[0].lower() == 'east':
            self.local.description = ("You are in the Hallway.\n"
                                      "Below you is the Corridor and east of you is the door."
                                      "You can also see a box here.")

        if self.local.name == 'Vault' and not getstatus(self.local,"gate_closed") and args[0].lower() == 'south':
            self.local.description = ('Here is a button and a gate that leads to the south.\n '
                                      'To open the gate, you must push the button.\n '
                                      'To press the button and open the gate, simply type \'push button\'.\n'
                                      'Go ahead and try it now.')
            return Go.__call__(self, args)
        if self.local.name == 'Study' and not getstatus(self.local,"portal_closed"):
            self.local.description = ('You are in the Study.\n'
                                      'You see a portal to the west and a Wizard here.\n'
                                      'The Vault is to the north.')
            return Go.__call__(self, args)
        return Go.__call__(self,args)


class Push(Command):
    def __init__(self, local, controller):
        Command.__init__(self, local, controller)

    def __call__(self, args):
        if args[0].lower() == "button":
            setstatus(self.local, "gate_closed", False)
            return "You sucessful press the button"


class Ask(Command):
    def __init__(self, local, controller):
        Command.__init__(self, local, controller)

    def __call__(self, args):
        if args.lower().strip() == "wizard about the portal":
            return ('So you want to go through my portal? Well then, we may have a problem.\n'
                    'See, I forgot how to open it. If only I could remember...\n'
                    "Say, I've heard you may have something in your inventory that could help me.\n"
                    "Check your inventory by  typing 'inventory' or 'i' and then show me something you think\n"
                    "would help by typing 'show (object) to wizard'.\n")


class Show(Command):
    def __init__(self, local, controller):
        Command.__init__(self, local, controller)

    def __call__(self, args):
        itemname = " ".join(args)
        if itemname.lower() != "potion book":
            return 'No, no, no. What else do you have?'
        setstatus(self.local, "portal_closed", False)
        return 'Just what I was looking for! Ok, now the portal to the west is open. Go through it to end your game.'

game = MyGame("Tutorial.yaml")
game.run()#'inputf.txt')
