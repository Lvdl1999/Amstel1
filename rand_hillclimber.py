"""
Amstel1
Heuristieken
sim_annealing.py
The random hillclimber algorithm.
"""

from amstel import Amstel
from plattegrond import Plattegrond


def rand_hillclimber():
    amstel = Amstel()
    plattegrond = Plattegrond(160, 180)
    amstel.plaats_huizen(plattegrond)

    # Loop over de huizen_lijst om het dichtstbijzijnde buurhuis te vinden
    # for huis in amstel.huizen_lijst:
    #     dichtstbij, kortste_afstand = huis.dichtsbijzijnde_huis(amstel.huizen_lijst)
        # print(f"Voor {huis.id} is het dichtstbijzijnde huis {dichtstbij.id}. Met afstand van {kortste_afstand}m.")
    oude_waarde = int(amstel.totale_nieuwe_huiswaarde())
    print(f"Totale wijk waarde is: {oude_waarde} euro")

    amstel.visualisatie()

    for i in range(1000):
        huis, linksboven = amstel.herplaats_huis(plattegrond)
        nieuwe_waarde = int(amstel.totale_nieuwe_huiswaarde())

        if oude_waarde > nieuwe_waarde:
            amstel.plaats_huis(huis, linksboven)
        else:
            oude_waarde = nieuwe_waarde
            print(f"Totale wijk waarde is: {oude_waarde} euro")

            amstel.visualisatie()



# lowerbound alle huizen aan elkaar
# upperbound alle huizen alleen op de plattegrond
