from Framework.Constants import Printm, TITLE_INDEX, DESCRIPTION_INDEX

__author__ = 'Thadeu Jose'


class Debug:

    def __init__(self, printm=Printm.NOT_PRINT):
        self.text = list()
        self.commands = dict()
        self.myprintm = printm

    def archivetype(self, arch):
        self.text.append("Archive Type: "+str(type(arch)))

    def scene(self, scene):
        self.text.append("-"*30)
        self.text.append("Scene:")
        self.text.append("Name:"+str(scene[TITLE_INDEX]))
        self.text.append("Type:"+str(type(scene)))
        self.text.append("Description:"+str(scene[DESCRIPTION_INDEX]))

    def addcommand(self, scenename, command):
        if scenename not in self.commands:
            self.commands[scenename]=list()
        self.commands[scenename].append(command)

    def printf(self):
        if self.myprintm == Printm.ON_SCREEN:
            print("\n".join(self.text))
            for key, elem in self.commands.items():
                print("-"*30)
                print(key)
                print(elem)
            print("-"*30)
        if self.myprintm == Printm.ON_FILE:
            with open("debug.txt", "w") as outputfile:
                outputfile.write("\n".join(self.text))
                outputfile.write("-"*30+"\n")
                for key, elem in self.commands.items():
                    outputfile.write("-"*30+"\n")
                    outputfile.write(key+"\n")
                    outputfile.write("\n".join(map(str, elem)))
                    outputfile.write("\n")
                outputfile.write("-"*30)