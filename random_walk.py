import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

from amstel import Amstel
from plattegrond import Plattegrond


def random_walk():
    amstel = Amstel()
    plattegrond = Plattegrond(160, 180)
    amstel.plaats_huizen(plattegrond)

    # Loop over de huizen_lijst om het dichtstbijzijnde buurhuis te vinden
    # for huis in amstel.huizen_lijst:
    #     dichtstbij, kortste_afstand = huis.dichtsbijzijnde_huis(amstel.huizen_lijst)
        # print(f"Voor {huis.id} is het dichtstbijzijnde huis {dichtstbij.id}. Met afstand van {kortste_afstand}m.")
    oude_waarde = int(amstel.totale_nieuwe_huiswaarde())
    print(f"Totale wijk waarde is: {oude_waarde} euro")

    # amstel.visualisatie()

    for i in range(1000):
        amstel.herplaats_huis(plattegrond)
        amstel.waardes_random.append(int(amstel.totale_nieuwe_huiswaarde()))

        print(f"Totale wijk waarde is: {int(amstel.totale_nieuwe_huiswaarde())} euro")

    return amstel

def visualisatie_random_walk(amstel):
    fig, ax = plt.subplots()

    x = [i for i in range(1000)]
    y = amstel.waardes_random

    plt.xlabel('Iteratie')
    plt.ylabel('Wijkwaarde ')
    plt.title('Random waardes van de wijk')

    plt.plot(x,y)
    plt.show()
