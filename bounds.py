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
    amstel = Amstel()
    plattegrond = Plattegrond(160, 180)
    upperbound = 0
    for huis in amstel.huizen_lijst:
        oude_huisprijs = float(huis.prijs)
        waardevermeerdering = float(huis.prijsverbetering)
        min_vrijstand = float(huis.min_vrijstand)
        max_vrije_afstand = ((plattegrond.hoogte / 2) - (huis.hoogte /2)) - min_vrijstand
<<<<<<< HEAD
        nieuwe_huiswaarde = (((oude_huisprijs + (waardevermeerdering * max_vrije_afstand))
=======
        nieuwe_huiswaarde = oude_huisprijs + (oude_huisprijs *(waardevermeerdering * max_vrije_afstand))

>>>>>>> ae9844b3abe7881b420442dc37bdf9d509ddbab9
        upperbound += nieuwe_huiswaarde

    return upperbound


def lowerbound():
    amstel = Amstel()
    plattegrond = Plattegrond(160, 180)
    for huis in amstel.huizen_lijst:
        prijs = huis.prijs
        totale_waarde += prijs


# TODO afhankelijk van wat eentje returnt moet ie dat printen zodat 
# docent niet print statement hoeft te veranderen
if __name__ == '__main__':
<<<<<<< HEAD
    print(upperbound())
=======
    print(upperbound_calc())
>>>>>>> ae9844b3abe7881b420442dc37bdf9d509ddbab9
