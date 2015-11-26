__author__ = 'Thadeu Jose'

class ItemException(Exception):
    def __init__(self):
        pass

    def __str__(self):
         return repr('You dont pass a class or subclass of Item')

class EmptyInventoryException(Exception):
    def __init__(self):
        pass

    def __str__(self):
         return repr('You cant remove a item from a empty inventory')

class ItemNotFoundException(Exception):
    def __init__(self):
        pass

    def __str__(self):
         return repr('Item not found in the inventory')

class EmptyStringException(Exception):
    def __init__(self,value):
        self.value=value

    def __str__(self):
         return repr(self.value+' cant be a empty string')