import yaml
from Framework.Local import *
from Framework.Constants import *
from Framework.Commands import CommandFactory
from Framework.Constants import *

__author__ = 'Thadeu Jose'


class Parser:

    def __init__(self, filename, world, controller,  debug=False):
        self.filename = filename
        self.debugmode = debug
        self.myworld = world
        self.mycontroller = controller
        self.commandfactory = CommandFactory(self.mycontroller)

    def openfile(self):
        if not self.filename:
            raise EmptyStringException("Filename")
        with open(self.filename, "r") as stream:
            self.emptyfile(stream)
            textlist = yaml.load(stream)
            if self.debugmode:
                print(textlist)
        return textlist

    def emptyfile(self, stream):
        stream.seek(0) #ensure you're at the start of the file
        firstchar = stream.read(1) #get the first character
        if not firstchar:
            raise EmptyFileException()#first character is the empty string..
        stream.seek(0)

    def init(self):
        #todo Refatorar e criar class debugmode
        textlist = self.openfile()
        if self.debugmode:
            print(archivetype(textlist))
        if not isinstance(textlist, list):
            raise BadInput()
        if TITLE in textlist[TITLE_INDEX]:
            title = textlist[TITLE_INDEX][TITLE]
            if not title:
                raise EmptyStringException('Title')
            else:
                self.myworld.title = title
            if self.debugmode:
                print(DEBUG_TITLE_SUCESS)
        else:
            raise BadTitle()

        if DESCRIPTION in textlist[DESCRIPTION_INDEX]:
            description = textlist[DESCRIPTION_INDEX][DESCRIPTION]
            if not description:
                raise EmptyStringException('Description')
            else:
                self.myworld.description = description
            if self.debugmode:
                print(DEBUG_DESCRIPTION_SUCESS)
        else:
            raise BadDescription()

        if not textlist[SCENE_INDEX:]:
            raise EmptyScene()

        #construct all scene
        for e in textlist[SCENE_INDEX:]:
            if SCENE in e:
                if self.debugmode:
                    print(scenetype(e[SCENE]))
                    print(scenename(e[SCENE]))
                listScene = e[SCENE]
                try:
                    title = listScene[TITLE_INDEX]
                except IndexError:
                    raise EmptyTitle()
                try:
                    description = listScene[DESCRIPTION_INDEX]
                except IndexError:
                    raise EmptyDescription()

                if self.myworld.haslocal(title):
                    raise DuplicateTitleError(title)
                if self.debugmode:
                    print(description)
                local = Local(title, description.replace("\\n", "\n"), self.mycontroller)
                self.myworld.addLocal(local)
        if self.debugmode:
            print("Commands:")

        for e in textlist[SCENE_INDEX:]:
            if SCENE in e:
                listScene = e[SCENE]
                local = self.myworld.getlocal(listScene[TITLE_INDEX])
                for command in listScene[COMMANDS_INDEX:]:
                    if self.debugmode:
                        print(command)
                    self.commandfactory.makecommand(local, command)

        if self.debugmode:
            print("-"*30)

        if not self.mycontroller.currentlocal:
            raise NotStartPlace()
