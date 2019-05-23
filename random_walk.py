"""
Amstel1
Heuristieken
random_walk.py
Het random walk algoritme.
"""

import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math



def random_walk(amstel, plattegrond):
    """
        Een wijk word random geplaatst. Vervolgens word een random gekozen huis
        ook weer random verschoven. Er wordt hierin niet gekeken naar verbetering
        en verslechtering.
    """

    amstel.plaats_huizen(plattegrond)

    oude_waarde = int(amstel.totale_nieuwe_huiswaarde())
    print(f"Totale wijk waarde is: {oude_waarde} euro")

    amstel.visualisatie()

    for i in range(1000):
        amstel.herplaats_huis(plattegrond)
        amstel.waardes_random.append(int(amstel.totale_nieuwe_huiswaarde()))

        print(f"Totale wijk waarde is: {int(amstel.totale_nieuwe_huiswaarde())} euro")

    return amstel


def visualisatie_random_walk(amstel):
    """
        Plot een grafiek om een kijkje in het oplossingslandschap te geven.
    """
    fig, ax = plt.subplots()

    x = [i for i in range(1000)]
    y = amstel.waardes_random

    plt.xlabel('Iteratie')
    plt.ylabel('Wijkwaarde ')
    plt.title('Random walk')

    plt.plot(x,y)
    plt.show()
