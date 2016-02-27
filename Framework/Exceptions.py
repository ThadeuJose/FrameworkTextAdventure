from Framework.Constants import TITLE

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
    def __init__(self, name, status=None):
        self.name = name
        self.status = status

    def __str__(self):
        if self.status:
            return repr('The object '+self.name+ ' dont have the status '+self.status)
        return  repr('The object '+self.name+ ' dont have status')

class BadInput(Exception):
    def __str__(self):
        return repr('The file is not following the specification')


class HistoryElementNotFoundError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value == TITLE:
            return repr('Title not found. Title have to occupy the first position of the file')
        return repr('Description not found. Description have to occupy the second position of the file')


class EmptyElementSceneError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr('Not exist'+self.value+'in scene')


class EmptyScenes(Exception):
    def __str__(self):
        return repr('The file not contain a scene')

class EmptyScene(Exception):
    def __str__(self):
        return repr('Scene not found')


class NotStartPlace(Exception):
    def __str__(self):
        return repr('The world not have a start place put the command [Start] in the scene where the player will start')


class DuplicateTitleError(Exception):
    def __init__(self, value):
        self.name = value

    def __str__(self):
        return repr('Already exist a scene with the title ' + self.name)


class ContainerNotFoundError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr('Dont exist a container name ' + self.value)
