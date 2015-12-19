__author__ = 'Thadeu Jose'


DIRECTIONS = {'north':'south', 'south':'north', 'west':'east', 'east':'west',
              'northwest':'southeast', 'southeast':'northwest', 'northeast':'southwest', 'southwest':'northeast'}

def oppositedirection(item):
    if item.lower() in DIRECTIONS:
        return DIRECTIONS[item.lower()]

