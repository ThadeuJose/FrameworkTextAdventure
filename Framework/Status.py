from Framework.Exceptions import DontHaveStatusException
__author__ = 'Thadeu Jose'


class Status(dict):
    pass


def addstatus(cls,idstatus,status):
    cls.status=Status()
    cls.status[idstatus]=status

def getstatus(cls,idstatus):
    try:
        status =cls.status[idstatus]
    except AttributeError:
        raise DontHaveStatusException(cls.name,idstatus)
    return status

#todo falta o removestatus