"""
Amstel1
Heuristieken
hillclimber.py
Het hillclimber algoritme.
"""


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
        elif not plattegrond.grens_check(huis) or plattegrond.overlap_check(huis, amstel.huizen_lijst):
            amstel.plaats_huis(huis, linksboven_oud)
        else:
            oude_waarde = nieuwe_waarde
            print(f"Totale wijk waarde is: {oude_waarde} euro")

    amstel.visualisatie()
