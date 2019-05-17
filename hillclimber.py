from amstel import Amstel
from plattegrond import Plattegrond


def hillclimber():
    amstel = Amstel()
    plattegrond = Plattegrond(160, 180)
    amstel.plaats_huizen(plattegrond)

    # Loop over de huizen_lijst om het dichtstbijzijnde buurhuis te vinden
    # for huis in amstel.huizen_lijst:
    #     dichtstbij, kortste_afstand = huis.dichtsbijzijnde_huis(amstel.huizen_lijst)
        # print(f"Voor {huis.id} is het dichtstbijzijnde huis {dichtstbij.id}. Met afstand van {kortste_afstand}m.")
    oude_waarde = int(amstel.totale_nieuwe_huiswaarde())
    print(f"Totale wijk waarde is: {oude_waarde} euro")

    amstel.visualisatie()

    for i in range(1000):
        # geen coord nodig want huis weet zn eigen coords
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



# lowerbound alle huizen aan elkaar
# upperbound alle huizen alleen op de plattegrond
