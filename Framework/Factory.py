from Framework.Commands import Go, Get, See, Open
from Framework.Constants import CommandIndex,CommandConst,StatusConst, DIRECTION_INDEX,LOCAL_INDEX
from Framework.Item import Item
from Framework.Status import addstatus, hasstatus, getstatus, addinventory, getinventory
from Framework.Exceptions import CommandNotFoundException,ContainerNotFoundError, IncorrectTypeException
from Framework.Actor import NPC

__author__ = 'Thadeu Jose'


#TODO Take magic number and character ':'
class TextObjectFactory:
    """Create all the commands"""

    def __init__(self, controller):
        self.controller = controller
        self.command = None
        self._dispatch = {
            CommandConst.START: self._make_start,
            CommandConst.END: self._make_end,
            CommandConst.GO: self._make_go,
            CommandConst.ITEM: self._make_item,
            CommandConst.STATUS: self._make_status,
            CommandConst.NPC: self._make_NPC,
        }

    def maketextobject(self, local, command):
        """Make a text object based in what is write in the YAML file"""
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
        self.controller.addcommand(local.title, CommandConst.GO, Go)

    def _make_item(self, local):
        newitem = Item(self.command[1], self.command[2])
        addinventory(local, StatusConst.INVENTORY, newitem)
        self.controller.addcommand(local.title, CommandConst.GET, Get)
        self.controller.addcommand(local.title, CommandConst.SEE, See)
        if len(self.command) > 3:
            self.createstatus(newitem, self.command[3:])
            if hasstatus(newitem, StatusConst.CONTAINER):
                self.controller.addcommand(local.title, CommandConst.OPEN, Open)
            if hasstatus(newitem, StatusConst.QUANT):
                for i in range(int(getstatus(newitem, StatusConst.QUANT-1))):
                    addinventory(local, StatusConst.INVENTORY, newitem)
            if hasstatus(newitem, StatusConst.INSIDE):
                containername = getstatus(newitem, StatusConst.INSIDE)
                inv = getinventory(local, StatusConst.INVENTORY)
                if containername in inv:
                    addstatus(newitem, StatusConst.VISIBLE, False)
                else:
                    raise ContainerNotFoundError(containername)

    def _make_status(self, local):
        self.createstatus(local, self.command[1:])

    def _make_NPC(self, local):
        addstatus(local, self.command[1], NPC(self.command[1], self.command[2]))
