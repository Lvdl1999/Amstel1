"""
Amstel1
Heuristieken
hillclimber.py
Het hillclimber algoritme.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches


def hillclimber(amstel, plattegrond):
    """
        De 'hillclimber' kiest een random huis uit de wijk en verschuift het met
        een random waarde tussen de -10 en 10 meter. Vervolgens wordt gekeken of
        dit een betere oplossing genereert. Zo niet, dan wordt het huis
        teruggeplaatst.
    """

    oude_waarde = int(amstel.totale_nieuwe_huiswaarde())
    print(f"Totale wijk waarde is: {oude_waarde} euro")

    amstel.visualisatie()

    for i in range(1000):

        huis, linksboven_oud = amstel.schuif_huis()
        nieuwe_waarde = int(amstel.totale_nieuwe_huiswaarde())

        if oude_waarde > nieuwe_waarde:
            amstel.plaats_huis(huis, linksboven_oud)
        elif not plattegrond.grens_check(huis) or plattegrond.overlap_check(huis, amstel.wijk_lijst):
            amstel.plaats_huis(huis, linksboven_oud)
        else:
            oude_waarde = nieuwe_waarde
            if oude_waarde > amstel.hoogste_waarde:
                amstel.hoogste_waarde = oude_waarde
            print(f"Totale wijk waarde is: {oude_waarde} euro")

        amstel.waardes_lijst.append(oude_waarde)

    # amstel.visualisatie()


def visualisatie_hillclimber(amstel):
    """
        Plot een grafiek om een kijkje in het oplossingslandschap te geven.
    """
    fig, ax = plt.subplots()

    x = [i for i in range(len(amstel.waardes_lijst))]
    y = amstel.waardes_lijst


    plt.xlabel('Iteratie')
    plt.ylabel('Wijkwaarde ')
    plt.title('Hillclimber')

    plt.plot(x,y)
    plt.show()
