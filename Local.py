__author__ = 'Thadeu Jose'

from Direction import Direction

class Local:

    def __init__(self,title,description):
        self.title=title
        self.description=description
        self.locals=dict()
        self.direc=Direction()

    def addLocal(self,direction,Local):
        #TODO
        #Testar
        if direction in self.direc and direction not in self.locals:
            self.locals[direction.lower()]=Local
            Local.addLocal(self.direc.oppositeDirection(direction),self)#Perigo


    def go(self,direction):
        if direction.lower() in self.direc:
            return self.locals[direction.lower()]

    def __str__(self):
        return self.title+"\n"+self.description