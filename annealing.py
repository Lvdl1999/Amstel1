"""
Amstel1
Heuristieken
annealing.py
Het simulated annealing algoritme.
"""

from hillclimber import hillclimber
import math
import random


def acceptatie_kans(nieuwe, oude, temperatuur):

    acceptatie = (nieuwe - oude)/temperatuur

    acckans = math.exp(acceptatie)

    return acckans


def linear_afkoeling(begin_temperatuur, temperatuur, iteraties, i):

    afname_temp = temperatuur/iteraties

    return afname_temp

def log_afkoeling(begin_temperatuur, temperatuur, iteraties, i):

    huidige_temperatuur = math.log(temperatuur/ begin_temperatuur)

    afname_temp = temperatuur - huidige_temperatuur
    return afname_temp

def exp_afkoeling(begin_temperatuur, temperatuur, iteraties, i):

    eind_temperatuur = 1

    huidige_temperatuur = begin_temperatuur * (eind_temperatuur/begin_temperatuur)**(i/iteraties)

    afname_temp = temperatuur - huidige_temperatuur

    return afname_temp


def annealing(amstel, plattegrond, afkoeling, begin_temperatuur):
    """
        Beginnend met de hillclimber om vervolgens met een bepaalde kans een
        verslechtering toe te laten. Bij een verslechtering moet de kans op
        toelating kleiner dan bij een verbetering van de waarde. Bedoeld om
        uit het optimale maximum te komen en een hoger optimaal maximum te
        vinden.
    """

    amstel.plaats_huizen(plattegrond)
    temperatuur = begin_temperatuur

    oude_waarde = int(amstel.totale_nieuwe_huiswaarde())
    print(f"Totale wijk waarde is: {oude_waarde} euro")

    amstel.visualisatie()
    # Beginnen met random_hillclimber
    iteraties = 1000
    for i in range(iteraties):

        huis, linksboven_oud = amstel.schuif_huis()
        nieuwe_waarde = int(amstel.totale_nieuwe_huiswaarde())

        if oude_waarde > nieuwe_waarde:
            if random.randrange(0,1) > acceptatie_kans(nieuwe_waarde, oude_waarde, temperatuur):
                amstel.plaats_huis(huis, linksboven_oud)
            elif not plattegrond.grens_check(huis) or plattegrond.overlap_check(huis, amstel.huizen_lijst):
                amstel.plaats_huis(huis, linksboven_oud)
            else:
                oude_waarde = nieuwe_waarde
        elif not plattegrond.grens_check(huis) or plattegrond.overlap_check(huis, amstel.huizen_lijst):
            amstel.plaats_huis(huis, linksboven_oud)
        else:
            oude_waarde = nieuwe_waarde
            print(f"Totale wijk waarde is: {oude_waarde} euro")
        # De afkoeling moet doorgeven of het logaritmisch, exponentieel of linear is.
        temperatuur -= afkoeling(begin_temperatuur, temperatuur, iteraties, i)

        if temperatuur < 1:
            temperatuur = 1


    hillclimber(amstel, plattegrond)

    amstel.visualisatie()

    return amstel
