"""
Amstel1
Heuristieken
sim_annealing.py
Calculating the upper- and lowerbound of the case AmstelHaege.
"""

from amstel import Amstel
from huis import Huis
from plattegrond import Plattegrond

def upperbound_calc():
    """
        De 'upperbound_calc' berekent en returnt hoeveel de wijk waard is in de
        meest optimale situatie. Namelijk dat ieder huis de maximale vrijstand
        in de wijk zou hebben.
    """
    amstel = Amstel()
    plattegrond = Plattegrond(160, 180)
    upperbound = 0
    for huis in amstel.huizen_lijst:
        oude_huisprijs = float(huis.prijs)
        waardevermeerdering = float(huis.prijsverbetering)
        min_vrijstand = float(huis.min_vrijstand)

        # Voor elk huis wordt berekend hoeveel vrijstand hij zou hebben als
        # dat huis midden in de wijk staat.
        max_vrije_afstand = ((plattegrond.hoogte / 2) - (huis.hoogte /2))
                            - min_vrijstand
        nieuwe_huiswaarde = oude_huisprijs + (oude_huisprijs *
                            (waardevermeerdering * max_vrije_afstand))

        upperbound += nieuwe_huiswaarde

    return upperbound


def lowerbound_calc():
    """
        De 'lowerbound_calc' berekent en returnt hoeveel de wijk waard is in de
        minst optimale situatie. Namelijk dat ieder huis alleen z'n minimale
        vrijstand in de wijk zou hebben.
    """
    amstel = Amstel()
    plattegrond = Plattegrond(160, 180)
    lowerbound = 0
    for huis in amstel.huizen_lijst:
        prijs = huis.prijs
        lowerbound += prijs

    return lowerbound

# TODO afhankelijk van wat eentje returnt moet ie dat printen zodat
# docent niet print statement hoeft te veranderen
if __name__ == '__main__':
    print(upperbound_calc())
