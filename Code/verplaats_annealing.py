"""
Amstel1
Heuristieken
annealing.py
Het simulated annealing algoritme.
"""

from .verplaats_hillclimber import verplaats_hillclimber
import math
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def acceptatie_kans(nieuwe, oude, temperatuur):
    """
        Binnen de functie 'acceptatie_kans' wordt aan de hand van de temperatuur
        berekend met hoeveel kans het annealing algoritme een verslechtering
        toe kan laten.
    """

    acceptatie = (nieuwe - oude)/temperatuur

    acckans = math.exp(acceptatie)

    return acckans


def lineair_afkoeling(begin_temperatuur, temperatuur, iteraties, i):
    """
        Hierbij neemt de temperatuur gedurende het runnen van simulated
        annealing lineair af, afhankelijk van de huidige iteratie.
    """

    afname_temp = temperatuur/iteraties

    return afname_temp


def log_afkoeling(begin_temperatuur, temperatuur, iteraties, i):
    """
        Bij een logaritmisch afkoelschema neemt de temperatuur gedurende het
        runnen van simulated annealing logaritmisch af.

    """

    huidige_temperatuur = begin_temperatuur/(math.log(i + 1) + 1)

    afname_temp = temperatuur - huidige_temperatuur

    return afname_temp


def exp_afkoeling(begin_temperatuur, temperatuur, iteraties, i):
    """
        Bij een exponentieel afkoelschema neemt de temperatuur gedurende het
        runnen van simulated annealing exponentieel af met een bepaalde factor.
    """

    eind_temperatuur = 1

    huidige_temperatuur = begin_temperatuur * (eind_temperatuur/begin_temperatuur)**(i/iteraties)

    afname_temp = temperatuur - huidige_temperatuur

    return afname_temp


def verplaats_annealing(amstel, plattegrond, afkoeling, begin_temperatuur):
    """
        Beginnend met de schuif_hillclimber om vervolgens met een bepaalde kans een
        verslechtering toe te laten. Bij een verslechtering moet de kans op
        toelating kleiner zijn dan bij een verbetering van de waarde. Dit is
        bedoelt om uit het lokaal optimum te komen en een betere oplossing te
        vinden.
    """

    amstel.plaats_huizen(plattegrond)
    temperatuur = begin_temperatuur

    oude_waarde = int(amstel.totale_nieuwe_huiswaarde())
    print(f"Totale wijk waarde is: {oude_waarde} euro")

    iteraties = 1000
    for i in range(iteraties):

        huis, linksboven_oud = amstel.schuif_huis()
        nieuwe_waarde = int(amstel.totale_nieuwe_huiswaarde())

        if nieuwe_waarde < 0.95 * amstel.hoogste_waarde:
            amstel.plaats_huis(huis, linksboven_oud)
        elif oude_waarde > nieuwe_waarde:
            if random.random() > acceptatie_kans(nieuwe_waarde, oude_waarde, temperatuur):
                amstel.plaats_huis(huis, linksboven_oud)
            elif not plattegrond.grens_check(huis) or plattegrond.overlap_check(huis, amstel.wijk_lijst):
                amstel.plaats_huis(huis, linksboven_oud)
            else:
                oude_waarde = nieuwe_waarde
        elif not plattegrond.grens_check(huis) or plattegrond.overlap_check(huis, amstel.wijk_lijst):
            amstel.plaats_huis(huis, linksboven_oud)
        else:
            oude_waarde = nieuwe_waarde
            if oude_waarde > amstel.hoogste_waarde:
                amstel.hoogste_waarde = oude_waarde
            print(f"Totale wijk waarde is: €{oude_waarde},-, temperatuur: {temperatuur}")
        # De afkoeling moet doorgeven of het logaritmisch, exponentieel of lineair is.
        temperatuur -= afkoeling(begin_temperatuur, temperatuur, iteraties, i)
        amstel.waardes_lijst.append(oude_waarde)
        if temperatuur < 1:
            temperatuur = 1

    verplaats_hillclimber(amstel, plattegrond)

    return amstel


def visualisatie_verplaats_annealing(amstel):
    """
        Plot een grafiek om een kijkje in het oplossingslandschap te geven.
    """
    fig, ax = plt.subplots()

    x = [i for i in range(len(amstel.waardes_lijst))]
    y = amstel.waardes_lijst


    plt.xlabel('Iteratie')
    plt.ylabel('Wijkwaarde ')
    plt.title('Simulated annealing')

    plt.plot(x,y)
    plt.show()
