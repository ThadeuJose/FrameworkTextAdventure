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

    def __init__(self):
        self._controller = None
        self.framework = None
        self._command = None
        self._local = None
        self._commanddispatch = {
            CommandConst.START: self._make_start,
            CommandConst.END: self._make_end,
            CommandConst.GO: self._make_go,
            CommandConst.ITEM: self._make_item,
            CommandConst.STATUS: self._make_status,
            CommandConst.NPC: self._make_NPC,
        }
        self._tagdispatch = {}

    def maketextobject(self, local, command):
        """Make a text object based in what is write in the YAML file"""
        self._command = command
        self._local = local
        commandindex = self._command[CommandIndex.Command].lower()
        if commandindex in self._commanddispatch:
            self._commanddispatch[commandindex]()
        elif commandindex in self._tagdispatch:
            self._tagdispatch[commandindex]._aux_make()
        else:
            raise CommandNotFoundException(commandindex)

    def addnewtag(self, id, cls):
        """Add a new tag. If the parser find this tag,he execute the function"""
        self._tagdispatch[id.lower()] = cls(self, self._controller)

    def addnewclass(self, id, commandclass):
        """Add a new tag.
        Only use if:
        tag in yaml and command who player will type is equal
        is only need to add the command to class
        """
        controller = self._controller

        def make():
            controller.addcommand(self._local.title, id, commandclass)
        self._commanddispatch[id.lower()] = make

    def _createstatus(self, cls, lis):
        """Add a list of status in a class"""
        for elem in lis:
            statusname, statusattribute = elem.lower().split(':')
            addstatus(cls, statusname, statusattribute)

    def _make_start(self):
        self._controller.currentlocal = self._controller.getlocal(self._local.title)

    def _make_end(self):
        self._controller.addendinglocal(self._controller.getlocal(self._local.title))

    def _make_go(self):
        self._local.addLocal(self._command[DIRECTION_INDEX], self._controller.world.getlocal(self._command[LOCAL_INDEX]))
        self._controller.addcommand(self._local.title, CommandConst.GO, Go)

    #Todo não esta fazendo multiplos itens, consertar
    def _make_item(self):
        newitem = Item(self._command[1], self._command[2])
        addinventory(self._local, StatusConst.INVENTORY, newitem)
        self._controller.addcommand(self._local.title, CommandConst.GET, Get)
        self._controller.addcommand(self._local.title, CommandConst.SEE, See)
        if len(self._command) > 3:
            self._createstatus(newitem, self._command[3:])
            if hasstatus(newitem, StatusConst.CONTAINER):
                self._controller.addcommand(self._local.title, CommandConst.OPEN, Open)
            if hasstatus(newitem, StatusConst.QUANT):
                for i in range(int(getstatus(newitem, StatusConst.QUANT-1))):
                    addinventory(self._local, StatusConst.INVENTORY, newitem)
            if hasstatus(newitem, StatusConst.INSIDE):
                containername = getstatus(newitem, StatusConst.INSIDE)
                inv = getinventory(self._local, StatusConst.INVENTORY)
                if containername in inv:
                    addstatus(newitem, StatusConst.VISIBLE, False)
                else:
                    raise ContainerNotFoundError(containername)

    def _make_status(self):
        self._createstatus(self._local, self._command[1:])

    def _make_NPC(self):
        newnpc = NPC(self._command[1], self._command[2])
        addstatus(self._local, self._command[1], newnpc)
        if len(self._command) > 3:
            self._createstatus(newnpc, self._command[3:])