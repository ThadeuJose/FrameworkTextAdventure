__author__ = 'Thadeu Jose'


directions={'north':'south','south':'north','west':'east','east':'west'
            ,'northwest':'southeast','southeast':'northwest','northeast':'southwest','southwest':'northeast'}

def oppositeDirection(item):
    if item.lower() in directions:
        return directions[item.lower()]

