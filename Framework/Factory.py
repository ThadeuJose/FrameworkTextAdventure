from Framework.Commands import Go, Get, See, Open
from Framework.Constants import CommandIndex, CommandConst, StatusConst, DIRECTION_INDEX, LOCAL_INDEX
from Framework.Item import Item
from Framework.Status import addstatus, hasstatus, getstatus, addinventory, getinventory
from Framework.Exceptions import CommandNotFoundException,ContainerNotFoundError, IncorrectTypeException
from Framework.Actor import NPC

__author__ = 'Thadeu Jose'


#TODO Take magic number and character ':'
class TextObjectFactory:
    """Create all the commands"""

    def __init__(self, controller):
        self._controller = controller
        self._command = None
        self._dispatch = {
            CommandConst.START: self._make_start,
            CommandConst.END: self._make_end,
            CommandConst.GO: self._make_go,
            CommandConst.ITEM: self._make_item,
            CommandConst.STATUS: self._make_status,
            CommandConst.NPC: self._make_NPC,
        }

    @property
    def CommandArgs(self):
        """The arguments of the command
        The first index is the command without the tag
        """
        return self._command[1:]

    @CommandArgs.setter
    def CommandArgs(self, value):
        pass

    def maketextobject(self, local, command):
        """Make a text object based in what is write in the YAML file"""
        self._command = command
        commandindex = self._command[CommandIndex.Command].lower()
        if commandindex in self._dispatch:
            self._dispatch[commandindex](local)
        else:
            raise CommandNotFoundException(commandindex)

    def addnewtag(self, id, function):
        """Add a new tag. If the parser find this tag,he execute the function"""
        self._dispatch[id.lower()] = function

    def addnewclass(self, id, commandclass):
        """Add a new tag.
        Only use if:
        tag in yaml and command who player will type is equal
        is only need to add the command to class
        """
        controller = self._controller

        def make(local):
            controller.addcommand(local.title, id, commandclass)
        self.addnewtag(id, make)

    def _createstatus(self, cls, lis):
        """Add a list of status in a class"""
        for elem in lis:
            statusname, statusattribute = elem.lower().split(':')
            addstatus(cls, statusname, statusattribute)

    def _make_start(self, local):
        self._controller.currentlocal = self._controller.getlocal(local.title)

    def _make_end(self, local):
        self._controller.addendinglocal(self._controller.getlocal(local.title))

    def _make_go(self, local):
        local.addLocal(self._command[DIRECTION_INDEX], self._controller.world.getlocal(self._command[LOCAL_INDEX]))
        self._controller.addcommand(local.title, CommandConst.GO, Go)

    def _make_item(self, local):
        newitem = Item(self._command[1], self._command[2])
        addinventory(local, StatusConst.INVENTORY, newitem)
        self._controller.addcommand(local.title, CommandConst.GET, Get)
        self._controller.addcommand(local.title, CommandConst.SEE, See)
        if len(self._command) > 3:
            self._createstatus(newitem, self._command[3:])
            if hasstatus(newitem, StatusConst.CONTAINER):
                self._controller.addcommand(local.title, CommandConst.OPEN, Open)
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
        self._createstatus(local, self._command[1:])

    def _make_NPC(self, local):
        addstatus(local, self._command[1], NPC(self._command[1], self._command[2]))
