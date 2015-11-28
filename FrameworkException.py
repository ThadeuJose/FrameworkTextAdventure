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

class CommandNotFoundException(Exception):
    def __str__(self):
         return repr('Command not found in the dictionary')

class LocalNotImplementException(Exception):
    def __str__(self):
         return repr('There are no class Local implment in this direction')

class DirectionNotFoundException(Exception):
    def __str__(self):
         return repr('The direction give is not a direction')