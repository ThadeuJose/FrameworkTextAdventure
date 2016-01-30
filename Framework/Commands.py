"""Create and implements the commands"""
from Framework.Constants import StatusConst
from Framework.Status import hasstatus, getstatus, setstatus,  getinventory
from Framework.Local import Local

__author__ = 'Thadeu Jose'


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
        inventory = getinventory(self.local, StatusConst.INVENTORY)
        itemname = " ".join(args)
        if not inventory:
            return "There is nothing to get here"
        if itemname not in inventory:
            return "There is no item call " + itemname.capitalize()
        item = inventory.take(itemname)
        cancollect = self._collectable(item, StatusConst.COLLECTABLE) and self._collectable(item, StatusConst.VISIBLE)
        if cancollect:
            inventory.add(item)
            self.controller.additem(item)
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
        if not args and hasstatus(self.local, StatusConst.INVENTORY):
            inv = getstatus(self.local, StatusConst.INVENTORY)
            result = list()
            for elem in inv:
                if hasstatus(elem, StatusConst.VISIBLE):
                    if getstatus(elem, StatusConst.VISIBLE):
                        result.append(elem)
                result.append(elem)
            return "You see " + ", ".join(result)
        if args[0] == 'inv':
            return "You have " + str(self.controller.player.inventory)
        if args and hasstatus(self.local, StatusConst.INVENTORY):
            inv = getstatus(self.local, StatusConst.INVENTORY)
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
        if not args:
            return "You have to give the name of the item you want to open"
        inv = getstatus(self.local, StatusConst.INVENTORY)
        itemname = " ".join(args)
        if itemname not in inv:
            return "There is no item call " + itemname.capitalize()
        for elem in inv:
            item = elem.item
            if hasstatus(item, StatusConst.INSIDE):
                containername = getstatus(item, StatusConst.INSIDE)
                if itemname.lower() == containername.lower():
                    setstatus(item, StatusConst.VISIBLE, True)
        return "You open " + containername.capitalize()