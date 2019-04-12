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

    # def __init__(self, verh_eengezinswoning, verh_bungalow, verh_maison, verh_wateropp )
    #
    #     self.verh_eengezinswoning = verh_eengezinswoning
    #     self.verh_bungalow = verh_bungalow
    #     self.verh_maison = verh_maison
    #     self.verh_wateropp = verh_wateropp
    #
    #     # Making the grid
    #     border_ID = int(1)
    #     grid = np.array([[0]* 321] * 361)
    #     grid[0] = border_ID
    #     grid[360] = border_ID
    #     grid[0:361,0:1] = border_ID
    #     grid[0:361,320:321] = border_ID
    #
    #     # Making a border

    def __init__(self, aantal_huizen, aantal_eengezinswoning, aantal_bungalow, aantal_maison, totaal_wateropp, aantal_sloten)

        self.aantal_huizen = get_int("Aantal huizen: ")
        self.aantal_eengezinswoning = int(aantal_huizen * 0,6)
        self.aantal_bungalow = int(aantal_huizen * 0,25)
        self.aantal_maison = int(aantal_huizen * 0,15)
        self.aantal_sloten = get_int("Aantal sloten:  ") # dit doen we voorlopig om zelf water in te richten


        if self.aantal_huizen != 20 or != 40 or !=60:
            print("Alleen keuze uit 20, 40 of 60 huizen")
            # Kan dit zo? we willen dat er opnieuw om een aantal huizen als input wordt gevraagd
            return self.aantal_huizen
        if 

        if aantal_eengezinswoning + aantal_bungalow + aantal_maison !=  aantal_huizen:
            print ("Verhoudingen kloppen niet")


        # aanmaken lijst met alle huis objecten
        self.huizen_lijst= []
        eengezinswoning.id = 0

        # elk huis object toevoegen aan lijst en daarbij behorend id elke keer met 1 verhogen.
        # je wilt dat elk huis een ander id heeft
        for huis in len(aantal_eengezinswoning):
            id = eengezinswoning.id +1
            huizen_lijst.append(eengezinswoning)


        for huis in len(aantal_bungalow):
            id = bungalow.id +1
            huizen_lijst.append(bungalow)

        for huis in len(aantal_maison):
            id = maison.id +1
            huizen_lijst.append(maison)



class eengezinswoning():
    def __init__(self, id, oppervlakte, min_vrijstand, prijs, prijsverbetering)

        self.id= int(id) # hoe elke eengezinswoning met een ander id?
        self.oppervlakte = int(8*8)
        self.min_vrijstand = int(2)
        self.prijs = int(285.000)
        self.prijsverbetering = float(0.03)

class bungalow():
    def __init__(self, id, oppervlakte, min_vrijstand, prijs, prijsverbetering)

        self.id= id
        self.oppervlakte = int(10*7,5)
        self.min_vrijstand = int(3)
        self.prijs = int(399.000)
        self.prijsverbetering = float(0.06)

class maison():
    def __init__(self, id,  oppervlakte, min_vrijstand, prijs, prijsverbetering)

        self.id= id
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
