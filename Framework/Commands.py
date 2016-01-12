"""Create and implements the commands"""

from Framework.Constants import COMMAND_END, COMMAND_START, COMMAND_GET, STATUS_QUANT, STATUS_NOT_COLLECTABLE, COMMAND_INDEX, COMMAND_ITEM, COMMAND_GO, DIRECTION_INDEX, LOCAL_INDEX, STATUS_INVENTORY
from Framework.Item import Item
from Framework.Status import addstatus,hasstatus, getstatus, addinventory, getinventory

__author__ = 'Thadeu Jose'


class CommandFactory:
    """Create all the commands"""
    def __init__(self, controller):
        self.controller = controller

    def makecommand(self, local, command):
        """Make a command based in what is write in the YAML file"""
        if command[COMMAND_INDEX].lower() == COMMAND_START:
            self.controller.currentlocal = self.controller.getlocal(local.title)

        if command[COMMAND_INDEX].lower() == COMMAND_END:
            self.controller.addendinglocal(self.controller.getlocal(local.title))

        if command[COMMAND_INDEX].lower() == COMMAND_GO:
            local.addLocal(command[DIRECTION_INDEX], self.controller.world.getlocal(command[LOCAL_INDEX]))
            self.controller.addcommand(local.title, COMMAND_GO, Go)

        if command[COMMAND_INDEX].lower()==COMMAND_ITEM:
            newitem = Item(command[1], command[2])
            if len(command) == 3:
                addinventory(local, STATUS_INVENTORY, newitem)
                self.controller.addcommand(local.title, COMMAND_GET, Get)
            else:
                for elem in command[3:]:
                    statusname, statusattribute = elem.lower().split(':')
                    addstatus(newitem, statusname, statusattribute)

                if hasstatus(newitem, STATUS_NOT_COLLECTABLE):
                    if getstatus(newitem, STATUS_NOT_COLLECTABLE):
                        addinventory(local, STATUS_NOT_COLLECTABLE, newitem)

                if hasstatus(newitem, STATUS_QUANT):
                    for i in range(int(getstatus(newitem,STATUS_QUANT))):
                        addinventory(local, STATUS_INVENTORY, newitem)


class Command:
    """Base class of all commands"""
    def __init__(self, local, controller):
        self.local = local
        self.controller = controller


class Go(Command):
    """Command you use to walk in the history"""
    def __init__(self, local, controller):
        Command.__init__(self, local, controller)

    def __call__(self, args):
        local =self.local.getlocal(args[0])
        self.controller.currentlocal=local
        return local.__str__()


class Get(Command):
    """Command you use to pick a item"""
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
    """Command you use to see in detail something"""
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