import yaml

from Framework.Debug import Debug
from Framework.Local import Local
from Framework.Exceptions import *
from Framework.Factory import TextObjectFactory
from Framework.Constants import *

__author__ = 'Thadeu Jose'


class Parser:

    def __init__(self, filename, world, controller, printDebug):
        self.filename = filename
        self.debugmode = Debug(printDebug)
        self.myworld = world
        self.mycontroller = controller
        self.textobjectfactory = TextObjectFactory(self.mycontroller)
        self._textlist = self.openfile()

    def openfile(self):
        if not self.filename:
            raise EmptyStringException("Filename")
        with open(self.filename, "r") as stream:
            self.emptyfile(stream)
            textlist = yaml.load(stream)
            #TODO if self.debugmode: print(textlist)
        return textlist

    def emptyfile(self, stream):
        stream.seek(0) #ensure you're at the start of the file
        firstchar = stream.read(1) #get the first character
        if not firstchar:
            raise EmptyFileException()#first character is the empty string..
        stream.seek(0)

    def init(self):
        self.debugmode.archivetype(self._textlist)

        if not isinstance(self._textlist, list):
            raise BadInput()

        self._create_history_element(TITLE_INDEX, TITLE)
        self._create_history_element(DESCRIPTION_INDEX, DESCRIPTION)

        if not self._getscenes():
            raise EmptyScene()

        #construct all scene
        for e in self._getscenes():
            scene = self._getscene(e)

            self.debugmode.scene(scene)

            title = self._create_scene_element(scene,TITLE_INDEX, TITLE)
            description = self._create_scene_element(scene,DESCRIPTION_INDEX, DESCRIPTION)

            if self.myworld.haslocal(title):
                raise DuplicateTitleError(title)

            local = Local(title, description.replace("\\n", "\n"))
            self.myworld.addLocal(local)

        for e in self._getscenes():
            scene = self._getscene(e)
            local = self.myworld.getlocal(self._get_scene_title(scene))
            for command in self._get_scene_commands(scene):
                self.debugmode.addcommand(self._get_scene_title(scene), command)
                self.textobjectfactory.maketextobject(local, command)

        if not self.mycontroller.currentlocal:
            raise NotStartPlace()

        self.debugmode.printf()

    def _get_scene_commands(self,scene):
        return scene[COMMANDS_INDEX:]

    def _get_scene_title(self, scene):
        return scene[TITLE_INDEX]

    def _getscene(self, elem):
        if SCENE not in elem:
            raise EmptyScene()
        return elem[SCENE]

    def _getscenes(self):
        return self._textlist[SCENE_INDEX:]

    def _create_scene_element(self, scene, index, strtype):
        try:
            result = scene[index]
        except IndexError:
            raise EmptyElementSceneError(strtype)
        return result

    def _create_history_element(self, index, typeelem):
        result = self._get_history_element(index, typeelem)
        if not result:
            raise EmptyStringException(typeelem)
        self._set_history_element(typeelem, result)
        #TODO self.debugmode.sucess(type) print debug sucess message

    def _set_history_element(self, typeelem, elem):
        if typeelem == DESCRIPTION:
            self.myworld.description = elem
        elif typeelem == TITLE:
            self.myworld.title = elem

    def _get_history_element(self, index, elem):
        if elem not in self._textlist[index]:
            raise HistoryElementNotFoundError(elem)
        return self._textlist[index][elem]
