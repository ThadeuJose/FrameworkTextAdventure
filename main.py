__author__ = 'Thadeu Jose'

from parserException import *

class History:
    def __init__(self,title=None,description=None):
        self.title=title
        self.description=description
        self.listScene=list()

    def addScene(self,title,description):
        pass


reserveWords = ["History:"]

def removeComents(lines):
    #remove all coments
    #return a list of strings with blank and normal lines
    resp=list()
    for string in lines:
        string=string.partition("#")[0]#Take everything before '#'
        string=string.strip()
        resp.append(string)
    return resp

def findFirstLine(index,listLines):
    #Find the first not blank line
    respIndex=index+1
    while listLines[respIndex]=='':
        respIndex+=1
    return listLines[respIndex],respIndex

def getBlock(indexLine,listLines):
    resp=listLines[indexLine][1:]
    respIndex=indexLine+1
    while not "\"" in listLines[respIndex]:
        resp+=listLines[respIndex]
        respIndex+=1
    resp+=listLines[respIndex].replace("\"","")
    return resp

def parse(string):
    history = History()
    file = open(string,"r")
    indexLine=0
    listLines=removeComents(file.readlines())
    if listLines[indexLine]!=reserveWords[indexLine]:
        raise historyException()
    history.title,indexLine=findFirstLine(indexLine,listLines)
    _,indexLine=findFirstLine(indexLine,listLines)#get the start of description block
    history.description=getBlock(indexLine,listLines)
    #TODO
    #Update a part string in python cheat sheet
    #Make a Location loop
    #Make a parser a class ?
    print(history.description)



parse("exemplo.txt")