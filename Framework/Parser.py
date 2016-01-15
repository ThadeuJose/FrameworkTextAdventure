import yaml
from Framework.Local import *
from Framework.Constants import *
from Framework.Commands import CommandFactory
from Framework.Constants import *
import re
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
            self.preprocess(stream)
            textlist = yaml.load(stream)
        return textlist


    def preprocess(self, stream):
        text = stream.read()
        self.emptyfile(stream)

        text = self.consumeentry("- Title: '[A-Za-z0-9\s]+'", text, WrongTitleException())
        text = self.consumeentry("- Description: '[A-Za-z0-9\s]+'", text, WrongDescriptionException())
        while len(text):
            print(text)
            text = self.consumeentry(r"- Scene:\n", text, WrongSceneException())
            text = self.consumeentry(r"\s+- '[A-Za-z0-9\s]+'\n", text, WrongSceneTitleException())
            text = self.consumeentry(r"\s+- '[A-Za-z0-9\s]+'\n?", text, WrongSceneDescriptionException())
            matchCommand = r"\s+- \[[[A-Za-z0-9\s,]+\]\n?"
            if re.search(matchCommand, text):
                text = self.consumeentry(matchCommand, text, WrongCommandException())

    def consumeentry(self, pattern, text, exception):
        match = re.search(pattern, text)
        if self.debugmode:
            print(match)
        if not match:
            raise exception
        if match.span()[0] == 0:
            return text[match.span()[1]:]
        if match.span()[1] == len(text):
            return text[:match.span()[0]]
        else:
            return text[:match.span()[0]] + text[match.span()[1]:]



    def emptyfile(self, stream):
        stream.seek(0) #ensure you're at the start of the file
        firstchar = stream.read(1) #get the first character
        if not firstchar:
            raise EmptyFileException()#first character is the empty string..
        stream.seek(0)

    def init(self):
        #todo
        #Testar se list[0] e titulo e list[1]
        #Testar arquivos errados
        textlist = self.openfile()
        if self.debugmode:
            print(archivetype(textlist))
        if TITLE in textlist[TITLE_INDEX]:
            self.myworld.title = textlist[TITLE_INDEX][TITLE]
            if self.debugmode:
                print(DEBUG_TITLE_SUCESS)
        if DESCRIPTION in textlist[DESCRIPTION_INDEX]:
            self.myworld.description = textlist[DESCRIPTION_INDEX][DESCRIPTION]
            if self.debugmode:
                print(DEBUG_DESCRIPTION_SUCESS)
        #construct all scene
        for e in textlist[SCENE_INDEX:]:
            if SCENE in e:
                if self.debugmode:
                    print(scenetype(e[SCENE]))
                    print(scenename(e[SCENE]))
                #tODO
                #Raise exception if not have titulo and description
                listScene = e[SCENE]
                local = Local(listScene[TITLE_INDEX], listScene[DESCRIPTION_INDEX].replace("\\n", "\n"), self.mycontroller)
                self.myworld.addLocal(local)
        if self.debugmode:
            print("Commands:")
        #todo check duplicate
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

        #todo check if has a start place

