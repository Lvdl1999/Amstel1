"""
Amstel1
Heuristieken
sim_annealing.py
The random hillclimber algorithm.
"""

from amstel import Amstel
from plattegrond import Plattegrond


def rand_hillclimber():
    """
            De 'rand_hillclimber' kiest een random huis uit de wijk en herplaatst
            het op een random plek en kijkt of dit een betere oplossing
            genereert. Zo niet dan wordt het huis weer teruggeplaatst.
    """
    amstel = Amstel()
    plattegrond = Plattegrond(160, 180)
    amstel.plaats_huizen(plattegrond)

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
