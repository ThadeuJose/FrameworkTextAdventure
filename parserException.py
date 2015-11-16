__author__ = 'Thadeu Jose'

class historyException(Exception):
    def __init__(self):
       pass

    def __str__(self):
         return repr("Don't have 'History:' in first line")