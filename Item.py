__author__ = 'Thadeu Jose'


class Item:
    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not __eq__(self, other)
