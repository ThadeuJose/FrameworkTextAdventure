__author__ = 'Thadeu Jose'

from Framework.Game import Game

class MyGame(Game):

    def init(self):
        #colocar o codigo de acender aqui
        pass

myGame=MyGame("LostCavern.yaml")
myGame.run()