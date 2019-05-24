"""
Amstel1
Heuristieken
coord.py
Maakt coördinaten aan voor een huis en returnt deze met def 'coords'.
"""

class Coord():
    def __init__(self, x, y):

        self.x = x
        self.y = y

    def coords(self):
        return (self.x, self.y)
