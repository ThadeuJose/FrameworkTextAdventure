from Framework.Exceptions import DontHaveStatusException
from Framework.Inventory import Inventory

__author__ = 'Thadeu Jose'


#TODO GameObject
class Status(dict):
    pass


def addstatus(cls, idstatus, status):
    try:
        cls.status[idstatus] = status
    except AttributeError:
        cls.status = Status()
        cls.status[idstatus] = status


def getstatus(cls, idstatus):
    try:
        status = cls.status[idstatus]
        if isinstance(status,str):
            if status.lower() == 'false':
                return False
            if status.lower() == 'true':
                return True
    except AttributeError:
        raise DontHaveStatusException(cls.name, idstatus)
    except KeyError:
        raise DontHaveStatusException(cls.name, idstatus)
    return status


def getallstatus(cls):
    resp = list()
    for idstatus in cls.status:
        try:
            resp.extend([idstatus, cls.status[idstatus]])
        except AttributeError:
            raise DontHaveStatusException(cls.name, idstatus)
        except KeyError:
            raise DontHaveStatusException(cls.name, idstatus)
    return ", ".join(resp)


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


def addinventory(cls, inventoryname, item=None):
    inv = getstatus(cls, inventoryname) if hasstatus(cls, inventoryname) else Inventory()
    if item:
        inv.add(item)
    addstatus(cls, inventoryname, inv)


def getinventory(cls, inventoryname):
    return getstatus(cls, inventoryname) if hasstatus(cls, inventoryname) else None
