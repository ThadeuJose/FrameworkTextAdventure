__author__ = 'Thadeu Jose'


class ItemException(Exception):
    def __str__(self):
         return repr('You dont pass a class or subclass of Item')


class EmptyInventoryException(Exception):
     def __str__(self):
         return repr('You cant remove a item from a empty inventory')


class ItemNotFoundException(Exception):
    def __str__(self):
         return repr('Item not found in the inventory')


class EmptyStringException(Exception):
    def __init__(self,value):
        self.value=value

    def __str__(self):
         return repr(self.value+' cant be a empty string')


class IncorrectTypeException(Exception):
    def __init__(self,value):
        self.value=value

    def __str__(self):
         return repr('Type '+self.value+ ' is expected')


class CommandNotFoundException(Exception):
    def __str__(self):
         return repr('Command not found in the dictionary')

class LocalAlreadyImplementException(Exception):
    def __str__(self):
         return repr('There are already a class Local implemented in this direction')

class LocalNotImplementException(Exception):
    def __str__(self):
         return repr('There are no class Local implemented in this direction')


class DirectionNotFoundException(Exception):
    def __str__(self):
         return repr('The direction give is not a direction')