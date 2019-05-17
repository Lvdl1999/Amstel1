from amstel import Amstel
from plattegrond import Plattegrond


def annealing():
    amstel = Amstel()
    print(amstel.huizen_lijst[13])
    plattegrond = Plattegrond(160, 180)
    amstel.plaats_huizen(plattegrond)

    # Loop over de huizen_lijst om het dichtstbijzijnde buurhuis te vinden
    # for huis in amstel.huizen_lijst:
    #     dichtstbij, kortste_afstand = huis.dichtsbijzijnde_huis(amstel.huizen_lijst)
        # print(f"Voor {huis.id} is het dichtstbijzijnde huis {dichtstbij.id}. Met afstand van {kortste_afstand}m.")
    oude_waarde = int(amstel.totale_nieuwe_huiswaarde())
    print(f"Totale beginwaarde wijk is: {oude_waarde} euro")
    # begin toestand van de wijk opslaan zodat ie altijd ernaar terug kan

    start_waarde = amstel.opslaan_wijk()
    top_waarde = (oude_waarde, start_waarde)
    for i in range(10):
        for j in range(1000):
            huis, linksboven = amstel.herplaats_huis(plattegrond)

        nieuwe_waarde = int(amstel.totale_nieuwe_huiswaarde())
        if oude_waarde > nieuwe_waarde:
            amstel.herplaats_wijk(start_waarde)
        else:
            top_waarde = (nieuwe_waarde, amstel.opslaan_wijk())

    print(f"Uiteindelijke wijk waarde is: {top_waarde[0]} euro")
    amstel.herplaats_wijk(top_waarde[1])



# lowerbound alle huizen aan elkaar
# upperbound alle huizen alleen op de plattegrond
