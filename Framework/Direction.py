"""Have all the direction you can go"""

__author__ = 'Thadeu Jose'


DIRECTIONS = {'north': 'south', 'south': 'north', 
			  'west': 'east', 'east': 'west',
              'northwest': 'southeast', 'southeast': 'northwest', 
              'northeast': 'southwest', 'southwest': 'northeast'}


def oppositedirection(direction):
    #Todo add exception
    """Return the registered opposite direction"""
    if direction.lower() in DIRECTIONS:
        return DIRECTIONS[direction.lower()]

