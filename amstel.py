import numpy as np

"""
Amstel1
Heuristieken
amstel.py
Build and optimize our neighbourhood.
"""


class Amstel():
    """
    This is the Amstel neighbourhood class. It contains necessary
    attributes and methods to build and optimize a neighbourhood.
    """

    def __init__(self, verh_eengezinswoning, verh_bungalow, verh_maison, verh_wateropp )

        self.verh_eengezinswoning = verh_eengezinswoning
        self.verh_bungalow = verh_bungalow
        self.verh_maison = verh_maison
        self.verh_wateropp = verh_wateropp

        # Making the grid
        border_ID = int(1)
        grid = np.array([[0]* 321] * 361)
        grid[0] = border_ID
        grid[360] = border_ID
        grid[0:361,0:1] = border_ID
        grid[0:361,320:321] = border_ID

        # Making a border



class eengezinswoning():
    def __init__(self, oppervlakte, min_vrijstand, prijs, prijsverbetering)

        self.oppervlakte = int(8*8)
        self.min_vrijstand = int(2)
        self.prijs = int(285.000)
        self.prijsverbetering = float(0.03)

class bungalow():
    def __init__(self, oppervlakte, min_vrijstand, prijs, prijsverbetering)

        self.oppervlakte = int(10*7,5)
        self.min_vrijstand = int(3)
        self.prijs = int(399.000)
        self.prijsverbetering = float(0.06)

class maison():
    def __init__(self, oppervlakte, min_vrijstand, prijs, prijsverbetering)

        self.oppervlakte = int(11*10,5)
        self.min_vrijstand = int(6)
        self.prijs = int(610.000)
        self.prijsverbetering = float(0.012)

class water():
    def __init__(self, oppervlakte, aantal_sloten)

        self.oppervlakte= oppervlakte
        self.aantal_sloten = aantal_sloten


def vrijstandscalc(eengezingswoning, bungalow, maison):

            eengezinswoning.vrijstand
