"""
Amstel1
Heuristieken
bounds.py
Calculating the upper- and lowerbound of the case AmstelHaege.
"""

from Code.amstel import Amstel
from Code.huis import Huis
from Code.plattegrond import Plattegrond

def upperbound_calc():
    """
        De 'upperbound_calc' berekent en returnt hoeveel de wijk waard is in de
        meest optimale situatie. Namelijk dat ieder huis de maximale vrijstand
        in de wijk zou hebben.
    """

    upperbound = 0
    for huis in amstel.wijk_lijst:
        oude_huisprijs = float(huis.prijs)
        waardevermeerdering = float(huis.prijsverbetering)
        min_vrijstand = float(huis.min_vrijstand)

        # Voor elk huis wordt berekend hoeveel vrijstand hij zou hebben als
        # dat huis midden in de wijk staat.
        max_vrije_afstand = ((plattegrond.hoogte / 2) - (huis.hoogte /2)) - min_vrijstand
        nieuwe_huiswaarde = oude_huisprijs + (oude_huisprijs * (waardevermeerdering * max_vrije_afstand))

        upperbound += nieuwe_huiswaarde

    return int(upperbound)


def lowerbound_calc():
    """
        De 'lowerbound_calc' berekent en returnt hoeveel de wijk waard is in de
        minst optimale situatie. Namelijk dat ieder huis alleen z'n minimale
        vrijstand in de wijk zou hebben.
    """

    lowerbound = 0
    for huis in amstel.wijk_lijst:
        prijs = huis.prijs
        lowerbound += prijs

    return int(lowerbound)


if __name__ == '__main__':

    amstel = Amstel()
    print("______________________________________________________________ \n")
    plattegrond = Plattegrond(160, 180)

    while True:
        antwoord = input("De upperbound','lowerbound' of 'beide' berekenen?:  ")
        print("___________________________________________________________ \n")
        if antwoord not in ["upperbound", "lowerbound", "beide"]:
            print("Beantwoord vraag met: 'upperbound', 'lowerbound', 'beide'")
        elif antwoord == "lowerbound":
            print(f"De lowerbound is: {lowerbound_calc()} euro.\n")
            break
        elif antwoord == "upperbound":
            print(f"De upperbound is: {upperbound_calc()} euro.\n")
            break
        else:
            print(f"De lowerbound is: €{lowerbound_calc()},-")
            print(f"De upperbound is: €{upperbound_calc()},-\n")
            break
