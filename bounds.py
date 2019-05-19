from amstel import Amstel
from huis import Huis
from plattegrond import Plattegrond

def upperbound():
    amstel = Amstel()
    plattegrond = Plattegrond(160, 180)
    upperbound = 0
    for huis in amstel.huizen_lijst:
        oude_huisprijs = float(huis.prijs)
        waardevermeerdering = float(huis.prijsverbetering)
        min_vrijstand = float(huis.min_vrijstand)
        max_vrije_afstand = ((plattegrond.hoogte / 2) - (huis.hoogte /2)) - min_vrijstand
        nieuwe_huiswaarde = (((oude_huisprijs + (waardevermeerdering * max_vrije_afstand))
        upperbound += nieuwe_huiswaarde
        return nieuwe_huiswaarde


def lowerbound():
    amstel = Amstel()
    plattegrond = Plattegrond(160, 180)
    for huis in amstel.huizen_lijst:
        prijs = huis.prijs
        totale_waarde += prijs

if __name__ == '__main__':
    print(upperbound())
