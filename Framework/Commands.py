from Framework.Constants import *
from Framework.Item import Item
from Framework.Inventory import Inventory

__author__ = 'Thadeu Jose'


class CommandFactory:
    def __init__(self,controller):
        self.controller=controller

    def makeCommand(self,local,command):
        if(command[COMMAND_INDEX].lower()==COMMAND_GO):
            local.addLocal(command[DIRECTION_INDEX],self.controller.world.getLocal(command[LOCAL_INDEX]))
        '''if(command[COMMAND_INDEX].lower()==COMMAND_ITEM):
            if(command[COMMAND_INDEX].lower()==COMMAND_ITEM):
                newitem=Item(command[1],command[2])
                if ':notCollectable' in command:
                    command.remove(':notCollectable')

                    local.addstatus('notCollectable',Inventory())

'''

class Command:
    def __init__(self,local,controller):
        self.local=local
        self.controller=controller


class Go(Command):
    def __init__(self,local,controller):
        Command.__init__(self,local,controller)

    def __call__(self,args):
        local =self.local.getLocal(args[0])
        self.controller.currentLocal=local
        return local.__str__()

class Get(Command):
    def __init__(self,local,controller):
        Command.__init__(self,local,controller)

    def __call__(self,args):
        inventory =self.local.getstatus(STATUS_INVENTORY)
        self.controller.setItem(inventory.get(args[0]))
        return "You sucessful get "+args[0]


