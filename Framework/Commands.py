"""Create and implements the commands"""
from Framework.Constants import StatusConst
from Framework.Status import hasstatus, getstatus, setstatus,  getinventory, getallstatus
from Framework.Local import Local

__author__ = 'Thadeu Jose'


class Command:
    """Base class of all commands"""
    def __init__(self, local, controller, framework):
        self.local = local
        self._controller = controller
        self.framework = framework

    def __call__(self, args):
        return self.function(args)

    def function(self, args):
        """Define what the command will do"""
        pass


class Go(Command):
    """Command you use to walk in the history"""
    def function(self, args):
        local = self.local.getlocal(args[0])
        if isinstance(local, Local):
            self._controller.currentlocal = local
            return local.__str__()
        return "You cant go in this direction"


class Get(Command):
    """Command you use to pick a item"""
    def function(self, args):
        inventory = getinventory(self.local, StatusConst.INVENTORY)
        itemname = " ".join(args)
        if not inventory:
            return "There is nothing to get here"
        if itemname not in inventory:
            return "There is no item call " + itemname.capitalize()
        item = inventory.take(itemname)
        cancollect = self._collectable(item, StatusConst.COLLECTABLE) and self._collectable(item, StatusConst.VISIBLE)
        if cancollect:
            self._controller.additem(item)
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


#Revisar
#-----------------------------------------------------------------------------------------------------------------------

class Inv(Command):
    def function(self, args):
        if self._controller.quantitem() == 0:
            return "You have no item"
        return "You have " + str(self._controller.inventory())


class See(Command):
    """Command you use to see in detail something"""
    def function(self, args):
        inv = getstatus(self.local, StatusConst.INVENTORY)
        if not args:
            result = list()
            for elem in inv:
                result.append(str(elem))
            if not result:
                return "You see nothing"
            return "You see "+",".join(result)
        if args:
            itemname = " ".join(args)
            if itemname in inv:
                item = inv.take(itemname)
                inv.add(item)
                return str(item)
        return "There nothing to see here"

    def _visible(self, item, idstatus):
        return getstatus(item, idstatus) if hasstatus(item, idstatus) else True

class Open(Command):
    """Command you use to open a container"""
    def function(self, args):
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