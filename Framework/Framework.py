from Framework.BaseTextObject import TextObject
from Framework.Item import Item
from Framework.Status import addstatus, getallstatus, getstatus, setstatus
from Framework.Tag import Tag
from Framework.Commands import Command
from Framework.Exceptions import ClassInvalid


class Framework:

    def __init__(self,controller):
        self._controller = controller
        self._idplayer = "player"

    def getplayer(self):
        return self._controller.player

    def addcls(self, idx, cls):
        if issubclass(cls, Command):
            self._controller.factory.addnewclass(idx, cls)
        elif issubclass(cls, Tag):
            self._controller.factory.addnewtag(idx, cls)
        else:
            ClassInvalid()

    def addplayerstatus(self, idx, idstatus, valuestatus):
        if idx.lower() == self._idplayer:
            addstatus(self._controller.player,idstatus,valuestatus)


    def setstatus(self, textobject, idx, valuestatus):
        setstatus(textobject,idx,valuestatus)

    def getstatus(self,idx,idstatus):
        return getstatus(idx,idstatus)

    def getallstatus(self,idx):
        return getallstatus(idx)

    def getlocal(self,name):
        return self._controller.getlocal(name)

#Itens manipulations  ------------------------------------------------------------------
    def playerhas(self, idx):
        return self._controller.hasitem(idx)

    def createitem(self,name,description, statusdic=None):
        item = Item(name,description)
        if statusdic:
            for k, v in statusdic.items():
                addstatus(item, k, v)
        return item

    def additemplayer(self,name,description,statusdic=None):
        self._controller.additem(self.createitem(name,description,statusdic))

    def removeitem(self, idx):
        self._controller.removeitem(idx)
#Itens manipulations  ------------------------------------------------------------------

    def createtextobject(self,name,description, statusdic=None):
        obj = TextObject(name,description)
        for k, v in statusdic.items():
            addstatus(obj, k, v)
        return obj

    def addlocal(self, local, idx, object):
        if isinstance(object, TextObject):
            addstatus(local, idx, object)
        else:
            self._controller.addcommand(local, idx, object)

    def gettextobject(self, local, idx):
        return getstatus(local, idx)