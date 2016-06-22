from Framework.Actor import Player
from Framework.Constants import CommandConst, PrintMode
from Framework.Factory import TextObjectFactory
from Framework.Framework import Framework
from Framework.Parser import Parser
from Framework.World import World
from Framework.Controller import Controller

__author__ = 'Thadeu Jose'


class Game:
    """Main class of the framework and class who will be inherited"""
    def __init__(self, filename, debug=PrintMode.NOT_PRINT):
        self.world = World()
        self.factory = TextObjectFactory()
        self.player = Player()
        self.controller = Controller(self, self.world, self.player, self.factory)
        self.factory._controller = self.controller
        self._parser = Parser(filename, self.world, self.controller,self.factory, debug)
        self.framework = Framework(self.controller)
        self.controller.framework = self.framework
        self._endgame=False
        self._endmessage = ''

    def preprocess(self):
        pass

    def init(self):
        pass

    def endgame(self, message='Thanks for playing this game'):
        self._endgame = True
        self._endmessage=message

    def _interpreter(self, inp):
        """Interpret the given input"""
        inp = inp.strip()
        elem = inp.split(" ")
        return self.controller.execute(elem[0], elem[1:])

    def run(self, fileinput=None):
        """Run the game interactive , if a fileinput is given,
        will run the game with the inputs in the file and exist"""
        self.preprocess()
        self._parser.init()
        self.init()
        if fileinput:
            self._run_inputfile(fileinput)
        else:
            self._run_interactive()

    def _run_interactive(self):
        exe = True
        print(self.world)
        print(self.controller.currentlocal)
        while exe:
            if self._endgame:
                print(self._endmessage)
                break
            if self.controller.isendinglocal(self.controller.currentlocal):
                break
            inp = input(">>")
            if inp.strip().lower() == CommandConst.END:
                break
            print(self._interpreter(inp))

    def _run_inputfile(self, fileinput):
        out = list()
        out.append(self.world)
        out.append(self.controller.currentlocal)
        with open(fileinput, "r") as inputfile:
            commands = inputfile.readlines()
        for c in commands:
            if not c[0] == '#':
                out.append(">> " + c.rstrip('\n'))
                out.append(self._interpreter(c))
        with open(fileinput[:-4] + '_output.txt', "w") as outputfile:
            outputfile.write("\n".join(map(str, out)))
