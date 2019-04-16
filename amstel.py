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


    def __init__(self, aantal_huizen, aantal_eengezinswoning, aantal_bungalow, aantal_maison, totaal_wateropp, aantal_sloten):

        self.aantal_huizen = input("Aantal huizen: ")
        self.aantal_eengezinswoning = int(aantal_huizen * 0.6)
        self.aantal_bungalow = int(aantal_huizen * 0.25)
        self.aantal_maison = int(aantal_huizen * 0.15)
        self.aantal_sloten = input("Aantal sloten:  ") # dit doen we voorlopig om zelf water in te richten


        while True:
            if self.aantal_huizen != 20 or != 40 or !=60:
                print("Alleen keuze uit 20, 40 of 60 huizen")

        # andere optie
        #if len(self.huizen_lijst) != 20 or !=40 or !=60 :

        if aantal_eengezinswoning + aantal_bungalow + aantal_maison !=  aantal_huizen:
            print ("Verhoudingen kloppen niet")

        # aanmaken lijst met alle huis objecten
        self.huizen_lijst = []

        # elk huis object toevoegen aan lijst en daarbij behorend id elke keer met 1 verhogen.
        # je wilt dat elk huis een ander id heeft
        counter = 0
        for i in range(aantal_eengezinswoning):
            huis = Huis(counter, 2, 285000, 0.03)
            counter += 1
            huizen_lijst.append(huis)

        counter = 100
        for i in range(aantal_bungalow):
            huis = Huis(counter, 3, 399000, 0.06)
            counter += 1
            huizen_lijst.append(huis)

        counter = 200
        for i in range(aantal_maison):
            huis = Huis(counter, 6, 610000, 0.12)
            counter += 1
            huizen_lijst.append(huis)


    def lowerbound(self):
        # Geen waarde vermeerderingen door extra vrijstand. Onder voorbehoudt dat alle huizen kunnen worden geplaats.
        # In huizen_lijst opzoeken prijs per soort woning * aantal dat soort woning
        self.aantal_eengezinswoning * self.huizen_lijst["prijs"]

    def upperbound(self):


    def totale_nieuwe_huiswaarde(self, Huis):



class Huis():
    def __init__(self, id, min_vrijstand, prijs, prijsverbetering, upperleft, upperright, bottomleft, bottomright):

        self.id= int(id)
        self.min_vrijstand = int(min_vrijstand)
        self.prijs = int(prijs)
        self.prijsverbetering = float(prijsverbetering)
        self.upperleft= upperleft
        self.upperright= upperright
        self.bottomleft= bottomleft
        self.bottomright= bottomright


    def vrijstandscalc(self):

        nieuwe_huiswaarde_lijst = []
        for i in range(aantal_huizen):


class Grid():
    def __init__(self, width, height):

        self.width= int(180)
        self.height= int(160)



class water():
    def __init__(self, oppervlakte, aantal_sloten):

        self.oppervlakte= oppervlakte
        self.aantal_sloten = aantal_sloten
