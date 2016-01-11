from Framework.Exceptions import DontHaveStatusException
from Framework.Inventory import Inventory

__author__ = 'Thadeu Jose'



class Status(dict):
    pass


def addstatus(cls, idstatus, status):
    try:
        cls.status[idstatus] = status
    except AttributeError:
        cls.status=Status()
        cls.status[idstatus]=status


def getstatus(cls, idstatus):
    try:
        status = cls.status[idstatus]
    except AttributeError:
        raise DontHaveStatusException(cls.name, idstatus)
    except KeyError:
        raise DontHaveStatusException(cls.name, idstatus)
    return status


def setstatus(cls, idstatus, status):
    try:
        cls.status[idstatus] = status
    except AttributeError:
        raise DontHaveStatusException(cls.name, idstatus)
    except KeyError:
        raise DontHaveStatusException(cls.name, idstatus)


def hasstatus(cls, idstatus):
    try:
        return idstatus in cls.status
    except AttributeError:
        return False
    except KeyError:
        return False

#todo falta o removestatus


def addinventory(cls, inventoryname, item):
    inv = getstatus(cls, inventoryname) if hasstatus(cls, inventoryname) else Inventory()
    inv.add(item)
    addstatus(cls, inventoryname, inv)


def getinventory(cls, inventoryname):
    return getstatus(cls, inventoryname) if hasstatus(cls, inventoryname) else None
