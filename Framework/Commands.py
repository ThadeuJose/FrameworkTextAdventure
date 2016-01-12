"""Create and implements the commands"""
from Framework.Constants import COMMAND_END, COMMAND_START, COMMAND_GET, STATUS_QUANT, \
    COMMAND_INDEX, COMMAND_ITEM, COMMAND_GO, DIRECTION_INDEX, \
    LOCAL_INDEX, STATUS_INVENTORY, STATUS_NOT_COLLECTABLE, COMMAND_STATUS
from Framework.Item import Item
from Framework.Status import addstatus,hasstatus, getstatus, addinventory, getinventory,getallstatus

__author__ = 'Thadeu Jose'


class CommandFactory:
    """Create all the commands"""
    def __init__(self, controller):
        self.controller = controller
        self.command = None
        self._dispatch = {
            COMMAND_START: self._make_start,
            COMMAND_END: self._make_end,
            COMMAND_GO: self._make_go,
            COMMAND_ITEM: self._make_item,
            COMMAND_STATUS: self._make_status,
        }

    def makecommand(self, local, command):
        """Make a command based in what is write in the YAML file"""
        self.command = command
        commandindex = self.command[COMMAND_INDEX].lower()
        if commandindex in self._dispatch:
            self._dispatch[commandindex](local)

    def createstatus(self, cls, list):
        """Add status in a class"""
        for elem in list:
            statusname, statusattribute = elem.lower().split(':')
            addstatus(cls, statusname, statusattribute)

    def _make_start(self, local):
        self.controller.currentlocal = self.controller.getlocal(local.title)

    def _make_end(self, local):
            self.controller.addendinglocal(self.controller.getlocal(local.title))

    def _make_go(self, local):
            local.addLocal(self.command[DIRECTION_INDEX], self.controller.world.getlocal(self.command[LOCAL_INDEX]))
            self.controller.addcommand(local.title, COMMAND_GO, Go)

    def _make_item(self, local):
            newitem = Item(self.command[1], self.command[2])
            addinventory(local, STATUS_INVENTORY, newitem)
            self.controller.addcommand(local.title, COMMAND_GET, Get)
            if len(self.command) > 3:
                self.createstatus(newitem, self.command[3:])
                if hasstatus(newitem, STATUS_QUANT):
                    for i in range(int(getstatus(newitem, STATUS_QUANT))):
                        addinventory(local, STATUS_INVENTORY, newitem)

    def _make_status(self, local):
        self.createstatus(local, self.command[1:])


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
        inventory = getinventory(self.local, self.local.DEFAULT_INVENTORY)
        if inventory:
            resp = " ".join(args)
            if resp in inventory:
                item = inventory.take(resp)
                if hasstatus(item, STATUS_NOT_COLLECTABLE) and getstatus(item, STATUS_NOT_COLLECTABLE):
                    inventory.add(item)
                    return "You cant get the item"
                self.controller.setitem(item)
                return "You sucessful get "+resp.capitalize()
            else:
                return "There is no item call "+resp.capitalize()
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
        if not args and hasstatus(self.local, STATUS_INVENTORY):
            inv = getstatus(self.local, STATUS_INVENTORY)
            return "You see " + str(inv)
        if args[0] == 'inv':
            return "You have "+ str(self.controller.player.inventory)
        return "There nothing to see here"
