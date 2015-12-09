__author__ = 'Thadeu Jose'

import yaml
from Framework.World import World
from Framework.Local import *
from Framework.Constants import *
from Framework.Controller import Controller
from Framework.Actor import Player
from Framework.Constants import *

class Game:

    def __init__(self,filename,debug=False):
        #todo
        # testar filename e criar exception
        #Criar interpreter
        #Usar expresso�es regulares no interpretador
        self.debugmode=debug
        self.filename=filename
        self.world = World()
        self.controller = None

    def openfile(self):
        if not self.filename:
            raise EmptyStringException("Filename")
        with open(self.filename,"r") as stream:
            textlist=yaml.load(stream)
        return textlist

    def _system_init(self):
        #todo
        #Testar se list[0] e titulo e list[1]
        textList=self.openfile()
        self.controller = Controller(self.world,Player())
        if self.debugmode:
            print(archivetype(textList))
        if TITLE in textList[TITLE_INDEX]:
                self.world.title = textList[TITLE_INDEX][TITLE]
                if self.debugmode:
                    print(DEBUG_TITLE_SUCESS)
        if DESCRIPTION in textList[DESCRIPTION_INDEX]:
            self.world.description= textList[DESCRIPTION_INDEX][DESCRIPTION]
            if(self.debugmode):
                print(DEBUG_DESCRIPTION_SUCESS)
        #construct all scene
        for e in textList[SCENE_INDEX:]:
            #print (e)
            if SCENE in e:
                if self.debugmode:
                    print(scenetype(e[self.SCENE]))
                    print(scenename(e[self.SCENE]))
                #tODO
                #Raise exception if not have titulo and description
                listScene = e[SCENE]
                local=Local(listScene[TITLE_INDEX],listScene[DESCRIPTION_INDEX].replace("\\n","\n"),self.controller)
                self.world.addLocal(local)
        if self.debugmode:
            print("Commands:")
        for e in textList[SCENE_INDEX:]:
            if SCENE in e:
                listScene = e[SCENE]
                local = self.world.getLocal(listScene[TITLE_INDEX])
                for command in listScene[COMMANDS_INDEX:]:
                    if(self.debugmode):
                        print(command)
                    if(command[COMMAND_INDEX].lower()==COMMAND_GO):
                        local.addLocal(command[DIRECTION_INDEX],self.world.getLocal(command[LOCAL_INDEX]))

        if self.debugmode:
            print("-"*30)
        self.controller.currentLocal=self.world.getLocal("Start")

    def init(self):
        pass

    def interpreter(self,inp):
        inp=inp.lower()
        list = inp.split(" ")
        print(self.controller.exec(list[0],list[1:]))


    def run(self):
        #TODO
        #Salvar os inputs num arquivo e os output no outro
        exe=''
        self._system_init()
        self.init()
        print(self.world)
        print(self.controller.currentLocal)
        while(exe!="END"):
            inp=input(">>")
            exe=self.interpreter(inp)
