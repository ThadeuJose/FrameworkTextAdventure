from Framework.Exceptions import EmptyStringException

__author__ = 'Thadeu Jose'

class TextObject:

    def __init__(self,name,description):
        if name:
            self._name=name
        else:
            raise EmptyStringException('name')

        if description:
            self._description=description
        else:
            raise EmptyStringException('description')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value:
            return value
        else:
            raise EmptyStringException('name')

    @property
    def description(self):
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