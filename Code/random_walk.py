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
        Een wijk wordt random geplaatst. Vervolgens wordt een random gekozen huis
        ook weer random verschoven. Er wordt hierin niet gekeken naar verbetering
        en verslechtering.
    """

    amstel.plaats_huizen(plattegrond)

    oude_waarde = int(amstel.totale_nieuwe_huiswaarde())
    print(f"Totale wijk waarde is: €{oude_waarde},-")

    # amstel.visualisatie()
    nieuwe_waarde = int(amstel.totale_nieuwe_huiswaarde())

    iteraties = 1000
    for i in range(iteraties):
        amstel.herplaats_huis(plattegrond)
        nieuwe_waarde = int(amstel.totale_nieuwe_huiswaarde())
        amstel.waardes_random.append((int(nieuwe_waarde)))
        amstel.resultaten_random_walk.append(int(nieuwe_waarde))

        print(f"Totale wijk waarde is: €{(int(nieuwe_waarde))},-")

    return amstel


def visualisatie_random_walk(amstel):
    """
        Plot een grafiek om een kijkje in het oplossingslandschap te geven.
    """
    fig, ax = plt.subplots()

    x = [i for i in range(len(amstel.waardes_random))]
    y = amstel.waardes_random

    plt.xlabel('Iteratie')
    plt.ylabel('Wijkwaarde ')
    plt.title('Random walk')

    plt.plot(x,y)
    plt.show()
