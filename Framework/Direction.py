"""Have all the direction you can go"""
from Framework.Exceptions import DirectionNotFoundException

__author__ = 'Thadeu Jose'

DIRECTIONS = {'north': 'south', 'south': 'north',
              'west': 'east', 'east': 'west',
              'northwest': 'southeast', 'southeast': 'northwest',
              'northeast': 'southwest', 'southwest': 'northeast'}


def oppositedirection(direction):
    """Return the registered opposite direction"""
    if direction.lower() not in DIRECTIONS:
        raise DirectionNotFoundException
    return DIRECTIONS[direction.lower()]


def adddirection(direction, opposite_direction):
    direction_lower = direction.lower()
    opposite_direction_lower = opposite_direction.lower()
    DIRECTIONS[direction_lower] = opposite_direction_lower
    DIRECTIONS[opposite_direction_lower] = direction_lower