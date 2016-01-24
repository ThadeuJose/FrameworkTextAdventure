from Framework.Actor import Player
from Framework.Parser import Parser
from Framework.World import World
from Framework.Controller import Controller

__author__ = 'Thadeu Jose'


class Game:
    """Main class of the framework and class who will be inherited"""
    def __init__(self, filename, debug=False):
        # todo
        # testar arquivo existente criar exception
        # Criar interpreter
        # Usar expressoes regulares no interpretador
        self.debugmode = debug
        self.filename = filename
        self.world = World()
        self.controller = Controller(self.world, Player())
        self.parser = Parser(self.filename, self.world, self.controller, self.debugmode)

    def preprocess(self):
        pass

    def init(self):
        pass

    def interpreter(self, inp):
        """Interpret the given input"""
        # Todo depois do modo logger implementado
        # tirar inp.lower()
        inp = inp.lower().strip()
        elem = inp.split(" ")
        return self.controller.execute(elem[0], elem[1:])

    def run(self, fileinput=None):
        """Run the game if a fileinput is given, will run the game with the inputs and exists"""
        # TODO
        # Chegar se arquivo de input e txt
        exe = True
        self.preprocess()
        self.parser.init()
        self.init()
        if not fileinput:
            print(self.world)
            print(self.controller.currentlocal)
            while exe:
                if self.controller.isendinglocal(self.controller.currentlocal):
                    break
                inp = input(">>")
                #TODO Command END
                print(self.interpreter(inp))

        else:
            out = list()
            out.append(self.world)
            out.append(self.controller.currentlocal)
            with open(fileinput, "r") as inputfile:
                commands = inputfile.readlines()
            for c in commands:
                if not c[0] == '#':
                    out.append(">> " + c.rstrip('\n'))
                    out.append(self.interpreter(c))
            with open(fileinput[:-4] + '_output.txt', "w") as outputfile:
                outputfile.write("\n".join(map(str, out)))
