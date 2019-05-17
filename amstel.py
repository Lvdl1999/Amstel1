"""
Amstel1
Heuristieken
amstel.py
Build and optimize our neighbourhood.
"""


import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

from coord import Coord
from huis import Huis
from plattegrond import Plattegrond
from water import Water

class Amstel():
    """
    This is the Amstel neighbourhood class. It contains necessary
    attributes and methods to build and optimize a neighbourhood.
    """
# elke functie : wat doet het, welke input en welke output krijg je.

    def __init__(self):

        while True:
            self.aantal_huizen = int(input("Aantal huizen: "))
            if self.aantal_huizen not in [20, 40, 60]:
                print("Alleen keuze uit 20, 40 of 60 huizen")
            else:
                break

        self.aantal_eengezinswoning = int(self.aantal_huizen * 0.6)
        self.aantal_bungalow = int(self.aantal_huizen * 0.25)
        self.aantal_maison = int(self.aantal_huizen * 0.15)


        while True:
            self.aantal_sloten = int(input("Aantal sloten:  "))
            if self.aantal_sloten not in [1, 2, 3, 4]:
                print("Minimaal 1 sloot en maximaal 4")
            else:
                break
        # aanmaken lijst met alle huis objecten
        self.huizen_lijst = []
        self.waardes_random = []
        self.totaalwaarde = 0

        # self.sloten_lijst = []

        # elk huis object toevoegen aan lijst en daarbij behorend id elke keer met 1 verhogen.
        # je wilt dat elk huis een ander id heeft
        counter = 0
        for i in range(self.aantal_eengezinswoning):
            # magic numbers toelichten!!
            huis = Huis(counter, 2, 285000, 0.03, 8, 8)
            counter += 1
            self.huizen_lijst.append(huis)

        counter = 100
        for i in range(self.aantal_bungalow):
            huis = Huis(counter, 3, 399000, 0.06, 10, 7.5)
            counter += 1
            self.huizen_lijst.append(huis)

        counter = 200
        for i in range(self.aantal_maison):
            huis = Huis(counter, 6, 610000, 0.12, 11, 10.5)
            counter += 1
            self.huizen_lijst.append(huis)

        # counter = 300
        # for i in range(self.aantal_sloten):
        #     sloot = Water(counter, self.aantal_sloten, 10)
        #     counter += 1
        #     self.sloten_lijst.append(sloot)

    def huis_check(self, huis, x, y):

        if x < 0 or x > huis.breedte:
            return False
        if y < 0 or y > huis.hoogte:
            return False
        return True

    def plaats_huis(self, huis, coord):

        x = coord.x
        y = coord.y

        #  logica uitleggen van startpunt linksboven en
        # vanuit daar naar andere hoekpunten vormt huis
        huis.linksboven = Coord(x, y)

        x = x + huis.breedte
        huis.rechtsboven = Coord(x, y)

        y = y - huis.hoogte
        huis.rechtsonder= Coord(x, y)

        x = x - huis.breedte
        huis.linksonder = Coord(x,y)

    # def plaats_sloot(self, sloot, coord):
    #
    #     x = coord.x
    #     y = coord.y
    #
    #     sloot.linksboven = Coord(x, y)
    #
    #     x = x + sloot.breedte
    #     sloot.rechtsboven = Coord(x, y)
    #
    #     y = y - sloot.hoogte
    #     sloot.rechtsonder= Coord(x, y)
    #
    #     x = x - sloot.breedte
    #     sloot.linksonder = Coord(x,y)

    def visualisatie(self):
        fig, ax = plt.subplots()

        for huis in self.huizen_lijst:
            if huis.id < 300:
                rect = patches.Rectangle(huis.linksonder.coords(), huis.breedte,
                huis.hoogte, linewidth=1,edgecolor='black',facecolor='none')
            else:
                rect = patches.Rectangle(huis.linksonder.coords(), huis.breedte,
                huis.hoogte, linewidth=1,edgecolor='blue',facecolor='none')

            ax.add_patch(rect)
            rx, ry = rect.get_xy()
            cx = rx + rect.get_width()/2.0
            cy = ry + rect.get_height()/2.0

            if huis.id < 100:
                ax.annotate(huis.id, (cx, cy), color='red', weight='bold',
                    fontsize=6, ha='center', va='center')
            elif 100 <= huis.id < 200:
                ax.annotate(huis.id, (cx, cy), color='black', weight='bold',
                    fontsize=6, ha='center', va='center')
            elif 200 <= huis.id < 300:
                ax.annotate(huis.id, (cx, cy), color='green', weight='bold',
                    fontsize=6, ha='center', va='center')
            # Voor water blauw!
            # else:
            #     ax.annotate(huis.id, (cx, cy), color='blue', weight='bold',
            #         fontsize=6, ha='center', va='center')


        ax.set_xlim([0, 180])
        ax.set_ylim([0, 160])

        plt.xlabel('Breedte in meters')
        plt.ylabel('Hoogte in meters ')
        plt.title('Plattegrond AmstelHaege')

        plt.show()


    def ondergrens(self):
        # Geen waarde vermeerderingen door extra vrijstand. Onder voorbehoudt dat alle huizen kunnen worden geplaats.
        # In huizen_lijst opzoeken prijs per soort woning * aantal dat soort woning
        self.aantal_eengezinswoning * self.huizen_lijst["prijs"]

    def bovengrens(self):
        pass


    def totale_nieuwe_huiswaarde(self):

        self.totaalwaarde = 0

        # elk huis heeft nu zn eigen waarde die die kan berekenen
        # dus we lopen over de huizenlijst en vragen van elk huis zn waarde en tel bij elkaar op
        for huis in self.huizen_lijst:
            # voor we de nieuwe huiswaarde aanroepen eerst zekerweten dat
            # dichtstbijzijnde afstand is berekend en opgeslagen in self.korststeafstand
            ander, afstand = huis.dichtsbijzijnde_huis(self.huizen_lijst)
            self.totaalwaarde += huis.nieuwe_huiswaarde_calc(afstand)

        return self.totaalwaarde

    def plaats_random(self, huis, plattegrond):
        # Als een huis niet geplaatst is heeft het geen x waarde
        while huis.linksboven.x == None:
            x = random.randint(0, plattegrond.breedte)
            y = random.randint(0, plattegrond.hoogte)
            coordinaat = Coord(x, y)
            self.plaats_huis(huis, coordinaat)
            if not plattegrond.grens_check(huis.rechtsonder) or plattegrond.overlap_check(huis, self.huizen_lijst):
                huis.reset()

    def plaats_huizen(self, plattegrond):
        ''' plaats_huizen calls the function plaats_huis to place houses in the
            grid. it takes in an argument called plattegrond wich describes the size\
            of the neighbourhood.
        '''

         #huizen op de plattegrond plaatsen met 4 punten (x en y)  en soort huis
        for huis in self.huizen_lijst:
            self.plaats_random(huis, plattegrond)


    def herplaats_huis(self, plattegrond):

        huis = random.choice(self.huizen_lijst)
        linksboven = huis.linksboven
        huis.reset()
        self.plaats_random(huis, plattegrond)

        return huis, linksboven


    def schuif_huis(self):
        # we halen een huis op en onthouden zn oude coords
        huis = random.choice(self.huizen_lijst)
        linksboven_oud = huis.linksboven

        schuifx = random.randint(-10, 10)
        schuify = random.randint(-10, 10)

        linksboven_nieuw = Coord(linksboven_oud.x + schuifx, linksboven_oud.y + schuify)
        self.plaats_huis(huis, linksboven_nieuw)

        #grens_check en overlap_check nog maken voor deze functie

        return huis, linksboven_oud

    def opslaan_wijk(self):
        # we maken een dict aan en slaan voor elk huis zn coords erin op
        # zodat die terug kan worden geplaatst
        beginwijk_dict = {}
        for huiscoord in self.huizen_lijst:
            beginwijk_dict[huiscoord] = huiscoord.linksboven
        return beginwijk_dict

    def herplaats_wijk(self, beginwijk_dict):

        for huiscoord in beginwijk_dict.keys():
            linksboven = beginwijk_dict[huiscoord]
            for huis in self.huizen_lijst:
                self.plaats_huis(huis, linksboven)


# def plaats_sloten(amstel, plattegrond):
#
#     while sloot.linksboven.x == None:
#         x = random.randint(0, plattegrond.breedte)
#         y = random.randint(0, plattegrond.hoogte)
#         coordinaat = Coord(x, y)
#         amstel.plaats_sloot(sloot, coordinaat)
#
#         if not sloot.grens_check(sloot.rechtsonder) or not sloot.sloot_verhouding_check:
#             sloot.reset()


#voor donderdag:

#methode om te plaatsen
#methode/functie die huizen random indeeld zonder rekening te houden met overlap (algoritme)
#kleine structuur voor het kijken naar overlap
#begin aan visualisatie met matplotlip
#scatterplot met rectangles

#voor volgende week
#plattegrond en amstel linken
# huis grens linksboven en rechtsonder check voor het plaatsen
# oplossingen genereren op een willekeurige manier
# plaats_huizen moet werken. ook zonder overlap
# vrijstand berekenen
# waarde bepalen van de wijk die we op dat moment hebben
