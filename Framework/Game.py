from Framework.Actor import Player
from Framework.Parser import Parser
from Framework.World import World
from Framework.Controller import Controller

__author__ = 'Thadeu Jose'


class Game:

    def __init__(self,filename,debug=False):
        #todo
        # testar arquivo existente criar exception
        #Criar interpreter
        #Usar expressoes regulares no interpretador
        self.debugmode = debug
        self.filename = filename
        self.world = World()
        self.controller = Controller(self.world, Player())
        self.parser = Parser(self.filename, self.world, self.controller)

    def init(self):
        pass

    def interpreter(self,inp):
        #Todo depois do modo logger implementado
        #tirar inp.lower()
        inp=inp.lower().strip()
        list = inp.split(" ")
        return self.controller.execute(list[0],list[1:])

    def run(self, fileinput=None):
        #TODO
        #Chegar so arquivo e txt
        exe=True
        self.parser.init()
        self.init()
        if not fileinput:
            print(self.world)
            print(self.controller.currentLocal)
            while exe:
                if self.controller.endinglocal(self.controller.currentLocal):
                    print(self.controller.currentLocal)
                    break
                inp=input(">>")
                print(self.interpreter(inp))
        else:
            out=list()
            out.append(self.world)
            out.append(self.controller.currentLocal)
            with open(fileinput, "r") as inputfile:
                commands = inputfile.readlines()
                for c in commands:
                    if not c[0] == '#':
                        out.append(">> "+c.rstrip('\n'))
                        out.append(self.interpreter(c))
            with open(fileinput[:-4]+'_output.txt', "w") as outputfile:
                outputfile.write("\n".join(map(str, out)))