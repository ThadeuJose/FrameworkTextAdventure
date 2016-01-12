from Framework.BaseTextObject import TextObject

__author__ = 'Thadeu Jose'


class Item(TextObject):
    """The item of the game"""
    def __init__(self, name, description):
        TextObject.__init__(self,name, description)

