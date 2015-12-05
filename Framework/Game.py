__author__ = 'Thadeu Jose'

import yaml
from Framework.World import World
from Framework.Local import *
from Framework.Commands import *

class Game:

    def __init__(self,filename,debug=True):
        #todo
        # testar filename e criar exception
        #Criar interpreter
        self.debugmode=debug
        self.filename=filename
        self.TITLE = "Title"
        self.TITLE_INDEX=0
        self.DESCRIPTION = "Description"
        self.DESCRIPTION_INDEX = 1
        self.COMMANDS_INDEX = 2 #index from the beginning of the command list
        self.COMMAND_HANDLE = 0
        self.COMMAND_GO="Go"
        self.DIRECTION_INDEX = 1
        self.LOCAL_INDEX=2
        self.SCENE = "Scene"
        self.debug_title_sucess="Title successfully added"
        self.debug_description_sucess="Description successfully added"
        self.world = World()

    def _system_init(self):
        #todo
        #existe esse arquivo
        #Testar se list[0] e titulo e list[1]
        #Ler comandos
        stream=open(self.filename,"r")
        textList=yaml.load(stream)
        if(self.debugmode):
            print("Archive Type: "+str(type(textList)))
        if self.TITLE in textList[self.TITLE_INDEX]:
                self.world.title = textList[self.TITLE_INDEX][self.TITLE]
                if(self.debugmode):
                    print(self.debug_title_sucess)
        if self.DESCRIPTION in textList[self.DESCRIPTION_INDEX]:
            self.world.description= textList[self.DESCRIPTION_INDEX][self.DESCRIPTION]
            if(self.debugmode):
                print(self.debug_description_sucess)
        #construct all scene
        for e in textList[self.DESCRIPTION_INDEX+1:]:
            #print (e)
            if self.SCENE in e:
                if(self.debugmode):
                    print("Scene Type:"+str(type(e[self.SCENE])))
                    print("Scene:"+str(e[self.SCENE]))
                #tODO
                #Raise exception if not have titulo and description
                listScene = e[self.SCENE]
                local=Local(listScene[self.TITLE_INDEX],listScene[self.DESCRIPTION_INDEX].replace("\\n","\n"))
                self.world.addLocal(local)
        if(self.debugmode):
            print("Commands:")
        for e in textList[self.DESCRIPTION_INDEX+1:]:
            if self.SCENE in e:
                listScene = e[self.SCENE]
                local = self.world.getLocal(listScene[self.TITLE_INDEX])
                for command in listScene[self.COMMANDS_INDEX:]:
                    if(self.debugmode):
                        print(command)
                    if(command==self.COMMAND_GO):
                        local.addLocal(command[self.DIRECTION_INDEX],command[self.LOCAL_INDEX])


        if(self.debugmode):
            print("-"*30)

    def init(self):
        pass

    def run(self):
        self._system_init()
        self.init()
        print(self.world)