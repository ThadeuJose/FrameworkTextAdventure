__author__ = 'Thadeu Jose'

#Todo replace Exception with Error
#TODO Colocar toda a parte de string em format {0} {1} e na parte de constant
class ItemException(Exception):
    def __str__(self):
        return repr('You dont pass a class or subclass of Item')


class EmptyInventoryException(Exception):
     def __str__(self):
        return repr('The inventory is empty')


class ItemNotFoundException(Exception):
    def __str__(self):
        return repr('Item not found in the inventory')


class EmptyStringException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value+' cant be a empty string')


class IncorrectTypeException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr('Type '+self.value+ ' is expected')


class CommandNotFoundException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr('Command '+self.value +' not found in the list of command')

class LocalAlreadyImplementException(Exception):
    def __str__(self):
        return repr('There are already a class Local implemented in this direction')

class LocalNotImplementException(Exception):
    def __str__(self):
        return repr('There are no class Local implemented in this direction')


class DirectionNotFoundException(Exception):
    def __str__(self):
        return repr('The direction give is not a direction')


class EmptyFileException(Exception):
    def __str__(self):
        return repr('The file is empty.')


class DontHaveLocalID(Exception):
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return repr("The are no class Local implemented with the title "+self.title)


class DontHaveStatusException(Exception):
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return repr('The object '+self.name+ ' dont have the status '+self.status)


class BadInput(Exception):
    def __str__(self):
        return repr('The file is not following the specification')


class BadTitle(Exception):
    def __str__(self):
        return repr('The title is not occupying the first position of the file')


class BadDescription(Exception):
    def __str__(self):
        return repr('The description is not occupying the second position of the file')


class EmptyTitle(Exception):
    def __str__(self):
        return repr('Not exist title in scene')


class EmptyDescription(Exception):
    def __str__(self):
        return repr('Not exist description in scene')


class EmptyScene(Exception):
    def __str__(self):
        return repr('The file not contain a scene')


class NotStartPlace(Exception):
    def __str__(self):
        return repr('The world not have a start place put the command [Start] in the scene where the player will start')


class DuplicateTitleError(Exception):
    def __init__(self, value):
        self.name = value
    def __str__(self):
        return repr('Already exist a scene with the title '+self.name)
