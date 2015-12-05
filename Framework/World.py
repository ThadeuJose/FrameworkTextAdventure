__author__ = 'Thadeu Jose'


class World:
    #todo
    #testar
    #Variavel privada
    def __init__(self,title=None,description=None):
        self.title=title
        self.description=description
        self.dictLocal=dict()

    def addLocal(self,Local):
        self.dictLocal[Local.title]=Local

    def getLocal(self,title):
        return self.dictLocal[title]

    def __str__(self):
        return self.title+"\n"+self.description
