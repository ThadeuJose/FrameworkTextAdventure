__author__ = 'Thadeu Jose'


class Command:
    def __init__(self,controller):
        self.controller=controller


class Go(Command):
    def __init__(self,local,controller):
        Command.__init__(self,controller)
        self.local=local

    def __call__(self,args):
        local =self.local.getLocal(args[0])
        self.controller.currentLocal=local
        return local.__str__()

