from Framework.Constants import COMMAND_END, COMMAND_START, COMMAND_GET, STATUS_QUANT, STATUS_NOT_COLLECTABLE, COMMAND_INDEX, COMMAND_ITEM, COMMAND_GO, DIRECTION_INDEX, LOCAL_INDEX, STATUS_INVENTORY
from Framework.Item import Item
from Framework.Status import hasstatus, getstatus, addinventory, getinventory

__author__ = 'Thadeu Jose'


class CommandFactory:
    def __init__(self, controller):
        self.controller = controller

    def makecommand(self, local, command):
        if command[COMMAND_INDEX].lower() == COMMAND_START:
            self.controller.currentLocal = self.controller.getlocal(local.title)

        if command[COMMAND_INDEX].lower() == COMMAND_END:
            self.controller.endinglocal(self.controller.getlocal(local.title))

        if command[COMMAND_INDEX].lower() == COMMAND_GO:
            local.addLocal(command[DIRECTION_INDEX], self.controller.world.getlocal(command[LOCAL_INDEX]))
            self.controller.addcommand(local.title, COMMAND_GO, Go)

        if command[COMMAND_INDEX].lower()==COMMAND_ITEM:
            newitem=Item(command[1], command[2])
            if len(command)==3:
                addinventory(local, STATUS_INVENTORY, newitem)
                self.controller.addcommand(local.title, COMMAND_GET ,Get)
            else:
                for elem in command[3:]:
                    statusname,statusattribute=elem.lower().split(':')
                    newitem_dic=dict()
                    newitem_dic[statusname]=statusattribute

                if STATUS_NOT_COLLECTABLE in newitem_dic:
                    if newitem_dic[STATUS_NOT_COLLECTABLE]:
                        addinventory(local, STATUS_NOT_COLLECTABLE, newitem)

                if STATUS_QUANT in newitem_dic:
                    for i in range(int(newitem_dic[STATUS_QUANT])):
                        addinventory(local, STATUS_INVENTORY, newitem)



class Command:
    def __init__(self, local, controller):
        self.local=local
        self.controller=controller


class Go(Command):
    def __init__(self, local, controller):
        Command.__init__(self, local, controller)

    def __call__(self, args):
        local =self.local.getlocal(args[0])
        self.controller.currentLocal=local
        return local.__str__()


class Get(Command):
    def __init__(self, local, controller):
        Command.__init__(self, local, controller)

    def __call__(self, args):
        inventory = getinventory(self.local,self.local.DEFAULT_INVENTORY)
        if inventory:
            resp = " ".join(args)
            if resp in inventory:
                self.controller.setitem(inventory.take(resp))
                return "You sucessful get "+resp.capitalize()
            return "You cant get the item"
        return "There is nothing to get here"



            #TODO Get more then one item
            #REGEX see if has a number not follow for nothing
'''            if len(args)==2:
                try:
                    if args[0] in inventory:
                        self.controller.setitem(inventory.take(args[0],int(args[1].strip())))
                        return "You sucessful get "+args[0]
                    return "You cant get the item"
                except Exception as e:
                    print(e)
                    return "You cant get the item"'''






class See(Command):

    def __init__(self, local, controller):
        Command.__init__(self, local, controller)

    def __call__(self, args):
        if not args:
            resp=list()
            if hasstatus(self.local,STATUS_INVENTORY):
                inv = getstatus(self.local, STATUS_INVENTORY)
                resp.append(str(inv))
            if hasstatus(self.local, STATUS_NOT_COLLECTABLE):
                inv = getstatus(self.local, STATUS_NOT_COLLECTABLE)
                resp.append(str(inv))
            if resp:
                return "You see "+ ", ".join(resp)
            return "There nothing to see here"
        if args[0] == 'inv':
            return "You have "+ str(self.controller.player.inventory)