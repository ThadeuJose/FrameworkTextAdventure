"""Create and implements the commands"""
from Framework.Constants import CommandIndex, COMMAND_END, COMMAND_START, COMMAND_GET, STATUS_QUANT, \
    COMMAND_ITEM, COMMAND_GO, DIRECTION_INDEX, COMMAND_NPC, \
    LOCAL_INDEX, STATUS_INVENTORY, STATUS_COLLECTABLE, COMMAND_STATUS, COMMAND_SEE,STATUS_CONTAINER,STATUS_INSIDE,\
    STATUS_VISIBLE,COMMAND_OPEN
from Framework.Item import Item
from Framework.Status import addstatus, hasstatus, getstatus,setstatus, addinventory, getinventory
from Framework.Exceptions import CommandNotFoundException,ContainerNotFoundError
from Framework.Local import Local
from Framework.Actor import NPC

__author__ = 'Thadeu Jose'

#TODO Take magic number and character ':'
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
            COMMAND_NPC: self._make_NPC,
        }

    def makecommand(self, local, command):
        """Make a command based in what is write in the YAML file"""
        self.command = command
        commandindex = self.command[CommandIndex.Command].lower()
        if commandindex in self._dispatch:
            self._dispatch[commandindex](local)
        else:
            raise CommandNotFoundException(commandindex)

    def createstatus(self, cls, lis):
        """Add a list of status in a class"""
        for elem in lis:
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
        self.controller.addcommand(local.title, COMMAND_SEE, See)
        if len(self.command) > 3:
            self.createstatus(newitem, self.command[3:])
            if hasstatus(newitem,STATUS_CONTAINER):
                self.controller.addcommand(local.title, COMMAND_OPEN, Open)
            if hasstatus(newitem, STATUS_QUANT):
                for i in range(int(getstatus(newitem, STATUS_QUANT-1))):
                    addinventory(local, STATUS_INVENTORY, newitem)
            if hasstatus(newitem, STATUS_INSIDE):
                containername = getstatus(newitem, STATUS_INSIDE)
                inv = getinventory(local, STATUS_INVENTORY)
                if containername in inv:
                    addstatus(newitem, STATUS_VISIBLE, False)
                else:
                    raise ContainerNotFoundError(containername)

    def _make_status(self, local):
        self.createstatus(local, self.command[1:])

    def _make_NPC(self, local):
        addstatus(local, self.command[1], NPC(self.command[1], self.command[2]))

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
        local = self.local.getlocal(args[0])
        if isinstance(local, Local):
            self.controller.currentlocal = local
            return local.__str__()
        return "You cant go in this direction"



class Get(Command):
    """Command you use to pick a item"""

    def __init__(self, local, controller):
        Command.__init__(self, local, controller)

    def __call__(self, args):
        inventory = getinventory(self.local, self.local.DEFAULT_INVENTORY)
        itemname = " ".join(args)
        if not inventory:
            return "There is nothing to get here"
        if itemname not in inventory:
            return "There is no item call " + itemname.capitalize()
        item = inventory.take(itemname)
        cancollect = self._collectable(item, STATUS_COLLECTABLE) and self._collectable(item, STATUS_VISIBLE)
        if cancollect:
            inventory.add(item)
            self.controller.setitem(item)
            return "You sucessful get " + itemname.capitalize()
        inventory.add(item)
        return "You cant get the item"

    def _collectable(self, item, idstatus):
        return getstatus(item, idstatus) if hasstatus(item, idstatus) else True




    # TODO Get more then one item
    # REGEX see if has a number not follow for nothing


'''            if len(args == :
                try:
                    if args[0] in inventory:
                        self.controller.setitem(inventory.take(args[0 , nt(args[1].strip())))
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
            result = list()
            for elem in inv:
                if hasstatus(elem, STATUS_VISIBLE):
                    if getstatus(elem, STATUS_VISIBLE):
                        result.append(elem)
                result.append(elem)
            return "You see " + ", ".join(result)
        if args[0] == 'inv':
            return "You have " + str(self.controller.player.inventory)
        if args and hasstatus(self.local, STATUS_INVENTORY):
            inv = getstatus(self.local, STATUS_INVENTORY)
            itemname = " ".join(args)
            if itemname in inv:
                item = inv.take(itemname)
                inv.add(item)
                return str(item)
        return "There nothing to see here"


class Open(Command):
    def __init__(self, local, controller):
        Command.__init__(self, local, controller)

    def __call__(self, args):
        if not args and not hasstatus(self.local, STATUS_INVENTORY):
            return "You have to give the name of the item you want to open"
        inv = getstatus(self.local, STATUS_INVENTORY)
        itemname = " ".join(args)
        if itemname not in inv:
            return "There is no item call " + itemname.capitalize()
        for elem in inv:
            item = elem.item
            if hasstatus(item, STATUS_INSIDE):
                containername = getstatus(item, STATUS_INSIDE)
                if itemname.lower() == containername.lower():
                    setstatus(item, STATUS_VISIBLE, True)
        return "You open " + containername.capitalize()