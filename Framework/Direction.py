__author__ = 'Thadeu Jose'


class Direction:
    def __init__(self):
        self._dictDirec={'north':'south','south':'north','west':'east','east':'west'
                        ,'northwest':'southeast','southeast':'northwest','northeast':'southwest','southwest':'northeast'}

    def __contains__(self, item):
        return item.lower() in self._dictDirec

    def oppositeDirection(self,item):
        if item.lower() in self._dictDirec:
            return self._dictDirec[item.lower()]

