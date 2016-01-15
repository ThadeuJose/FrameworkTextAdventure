"""Basic framework objects"""

from Framework.Exceptions import EmptyStringException

__author__ = 'Thadeu Jose'


class TextObject:
    """Basic object of the framework
    Name and Description cant be empty string
    """

    def __init__(self, name, description):
        if name:
            self._name = name
        else:
            raise EmptyStringException('name')

        if description:
            self._description = description
        else:
            raise EmptyStringException('description')

    @property
    def name(self):
        """The name of the object
        Use to index in the framework
        """
        return self._name

    @name.setter
    def name(self, value):
        if value:
            return value
        else:
            raise EmptyStringException('name')

    @property
    def description(self):
        """Describe the object
        Cant be empty string
        """
        return self._description

    @description.setter
    def description(self, value):
        if value:
            return value
        else:
            raise EmptyStringException('description')

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not __eq__(self, other)

    def __str__(self):
        return self._name+"\n"+self._description
