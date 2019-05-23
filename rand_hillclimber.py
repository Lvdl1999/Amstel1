"""
Amstel1
Heuristieken
rand_hillclimber.py
The random hillclimber algorithm.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

def rand_hillclimber(amstel, plattegrond):
    """
            De 'rand_hillclimber' kiest een random huis uit de wijk en herplaatst
            het op een random plek en kijkt of dit een betere oplossing
            genereert. Zo niet dan wordt het huis weer teruggeplaatst.
    """

    amstel.plaats_huizen(plattegrond)

    oude_waarde = int(amstel.totale_nieuwe_huiswaarde())
    print(f"Totale wijk waarde is: {oude_waarde} euro")

    # amstel.visualisatie()

    for i in range(1000):
        huis, linksboven = amstel.herplaats_huis(plattegrond)
        nieuwe_waarde = int(amstel.totale_nieuwe_huiswaarde())

        if oude_waarde > nieuwe_waarde:
            amstel.plaats_huis(huis, linksboven)
        else:
            oude_waarde = nieuwe_waarde
            print(f"Totale wijk waarde is: {oude_waarde} euro")

        amstel.waardes_lijst.append(oude_waarde)    

            # amstel.visualisatie()


def visualisatie_rand_hillclimber(amstel):
    """
        Plot een grafiek om een kijkje in het oplossingslandschap te geven.
    """
    fig, ax = plt.subplots()

    x = [i for i in range(len(amstel.waardes_lijst))]
    y = amstel.waardes_lijst


    plt.xlabel('Iteratie')
    plt.ylabel('Wijkwaarde ')
    plt.title('Random hillclimber')

    plt.plot(x,y)
    plt.show()
