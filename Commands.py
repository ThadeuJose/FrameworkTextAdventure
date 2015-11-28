__author__ = 'Thadeu Jose'

class Command:
    pass

class Go(Command):
    def __init__(self,local):
        self.local=local

    def __call__(self,direction):
        return self.local.getLocal(direction)

