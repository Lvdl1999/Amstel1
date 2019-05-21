"""
Amstel1
Heuristieken
sim_annealing.py
Het simulated annealing algoritme.
"""

from amstel import Amstel
from plattegrond import Plattegrond


def simannealing():
    """
        Bij de functie 'annealing'wordt 1000 keer de random_walk gedaan en de
        hoogste waarde opgeslagen. Mocht deze waarde beter zijn dan de begin
        waarde, wordt dit de nieuwe waarde en zo gaat dit door.
    """

    amstel = Amstel()
    plattegrond = Plattegrond(160, 180)
    amstel.plaats_huizen(plattegrond)

    oude_waarde = int(amstel.totale_nieuwe_huiswaarde())
    print(f"Totale beginwaarde wijk is: {oude_waarde} euro")
    amstel.visualisatie()

    start_waarde = amstel.opslaan_wijk()
    top_waarde = (oude_waarde, start_waarde)
    for i in range(10):
        for j in range(1000):
            huis, linksboven = amstel.herplaats_huis(plattegrond)

        nieuwe_waarde = int(amstel.totale_nieuwe_huiswaarde())
        if oude_waarde > nieuwe_waarde:
            # Als de oude waarde hoger is dan de nieuwe waarde zal de oude wijk
            # worden teruggeplaatst.
            amstel.herplaats_wijk(start_waarde)
        else:
            top_waarde = (nieuwe_waarde, amstel.opslaan_wijk())

    print(f"Uiteindelijke wijk waarde is: {top_waarde[0]} euro")
    amstel.visualisatie()
    amstel.herplaats_wijk(top_waarde[1])
