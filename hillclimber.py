"""
Amstel1
Heuristieken
hillclimber.py
Het hillclimber algoritme.
"""

from amstel import Amstel
from plattegrond import Plattegrond


def hillclimber():
    """
        De 'hillclimber' kiest een random huis uit de wijk en verschuift het met
        een random waarde tussen de -10 en 10 meter. Vervolgens wordt gekeken of
        dit een betere oplossing genereert. Zo niet, dan wordt het huis
        teruggeplaatst.
    """
    amstel = Amstel()
    plattegrond = Plattegrond(160, 180)
    amstel.plaats_huizen(plattegrond)

    oude_waarde = int(amstel.totale_nieuwe_huiswaarde())
    print(f"Totale wijk waarde is: {oude_waarde} euro")

    amstel.visualisatie()

    for i in range(1000):

        huis, linksboven_oud = amstel.schuif_huis()
        nieuwe_waarde = int(amstel.totale_nieuwe_huiswaarde())

        if oude_waarde > nieuwe_waarde:
            amstel.plaats_huis(huis, linksboven_oud)
        elif not plattegrond.grens_check(huis.rechtsonder) or plattegrond.overlap_check(huis, amstel.huizen_lijst):
            amstel.plaats_huis(huis, linksboven_oud)
        else:
            oude_waarde = nieuwe_waarde
            print(f"Totale wijk waarde is: {oude_waarde} euro")

            amstel.visualisatie()
