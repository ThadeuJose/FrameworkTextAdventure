__author__ = 'Thadeu Jose'


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
    def __init__(sel , alue):
        self.value = value

    def __str__(self):
        return repr(self.value+' cant be a empty string')


class IncorrectTypeException(Exception):
    def __init__(sel , alue):
        self.value = value

    def __str__(self):
        return repr('Type '+self.value+ ' is expected')

#TODO N�o � usada
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


class WrongTitleException(Exception):
    def __str__(self):
        return repr("Title should be in the format '- Title: 'string'")


class WrongDescriptionException(Exception):
    def __str__(self):
        return repr("Description should be in the format '- Description: 'string'")


class WrongSceneException(Exception):
    def __str__(self):
        return repr("Scene should be in the format '- Scene:\n")


class WrongSceneTitleException(Exception):
    def __str__(self):
        return repr("Scene Title should be in the format '- 'Title'\n")


class WrongSceneDescriptionException(Exception):
    def __str__(self):
        return repr("Scene Description should be in the format '- 'Description'\n")


class WrongCommandException(Exception):
    def __str__(self):
        return repr("Command should be in the format '- [command,arg1,arg2,...]\n")