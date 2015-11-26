from BaseTextObject import TextObject

__author__ = 'Thadeu Jose'


class Item(TextObject):
    def __init__(self, name, description):
        TextObject.__init__(self,name,description)