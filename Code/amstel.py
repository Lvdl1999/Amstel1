"""
Amstel1
Heuristieken
amstel.py
bouw en optimalizeer de wijk
"""


import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

from .coord import Coord
from .huis import Huis
from .plattegrond import Plattegrond


class Amstel():
    """
    Dit is de 'Amstel' class. Het bevat alle nodige attributen en methodes
    om onze wijk te bouwen en optimalizeren.
    """


    def __init__(self):

        # De wijk kan 20, 40 of 60 huizen bevatten afhankelijk van de
        # gebruikers keuze.
        while True:
            print("\nGeef aan hoeveel huizen (20, 40 of 60) en sloten (tussen 1 en 4) er in de wijk worden geplaatst.\n")
            self.aantal_huizen = int(input("Aantal huizen: "))
            if self.aantal_huizen not in [20, 40, 60]:
                print("Alleen keuze uit 20, 40 of 60 huizen")
            else:
                break

        self.oppervlakte_wijk = int(160*180)
        self.aantal_eengezinswoning = int(self.aantal_huizen * 0.6)
        self.aantal_bungalow = int(self.aantal_huizen * 0.25)
        self.aantal_maison = int(self.aantal_huizen * 0.15)

        # De wijk kan maximaal 4 sloten bevatten afhankelijk van de gebruikers
        # keuze.

        while True:
            self.aantal_sloten = int(input("Aantal sloten:  "))
            if self.aantal_sloten not in [1, 2, 3, 4]:
                print("Minimaal 1 sloot en maximaal 4")
            else:
                break

        self.wijk_lijst = []
        self.waardes_random = []
        self.totaalwaarde = 0
        self.waardes_lijst = []
        self.hoogste_waarde= 0

        self.resultaten_random_walk = []
        self.resultaten_log = []
        self.resultaten_exp = []
        self.resultaten_lin = []
        self.resultaten_schuif_hillclimber = []
        self.resultaten_verplaats_hillclimber = []

        """
            Elk huis heeft een verschillende attributen: (id, minimale vrijstand
            , prijs, prijvermeerdering, breedte, hoogte). Deze worden
            opgeslagen in de wijk_lijst. Ook water wordt aan deze lijst
            toegevoegd. Elk ander huis en water dat wordt toegevoegd aan de
            lijst krijgt een eigen id. Water heeft verder geen minimale minimale vrijstand
            , prijs, prijvermeerdering.
        """

        # De oppervlakte per sloot is 20% van de wijk gedeeld door
        # het aantal sloten.
        oppervlakte_per_sloot = int((self.oppervlakte_wijk * 0.2)/self.aantal_sloten)


        if self.aantal_huizen <= 40:
            self.breedte_sloot = math.sqrt(oppervlakte_per_sloot)
            self.hoogte_sloot = math.sqrt(oppervlakte_per_sloot)
        else:
            self.hoogte_sloot = math.sqrt(oppervlakte_per_sloot / 4)
            self.breedte_sloot = 4 * self.hoogte_sloot

        # De sloten toevoegen aan de wijk met een unieke ID vanaf 1000.
        counter = 1000
        for i in range(self.aantal_sloten):
            huis = Huis(counter, 0, 0, 0, self.breedte_sloot, self.hoogte_sloot)
            counter += 1
            # if self.aantal_huizen <= 40:
            self.wijk_lijst.append(huis)

        # Maisons toevoegen aan de wijk
        counter = 200
        for i in range(self.aantal_maison):
            huis = Huis(counter, 6, 610000, 0.12, 11, 10.5)
            counter += 1
            self.wijk_lijst.append(huis)

        # Bungalows toevoegen aan de wijk
        counter = 100
        for i in range(self.aantal_bungalow):
            huis = Huis(counter, 3, 399000, 0.06, 10, 7.5)
            counter += 1
            self.wijk_lijst.append(huis)

        # Eengezinswoningen toevoegen aan de wijk
        counter = 0
        for i in range(self.aantal_eengezinswoning):
            huis = Huis(counter, 2, 285000, 0.03, 8, 8)
            counter += 1
            self.wijk_lijst.append(huis)




    def huis_check(self, huis, x, y):
        """
            De functie 'huis_check' zorgt ervoor dat elk huis voldoet aan z'n
            eigen afmetingen.
        """
        if x < 0 or x > huis.breedte:
            return False
        if y < 0 or y > huis.hoogte:
            return False
        return True

    def plaats_huis(self, huis, coord):
        """
            De functie 'plaats_huis' begint voor elk huis met een
            linksboven-coordinaat. Vanuit daar wordt per huis gekeken naar de
            breedte en de hoogte en zo worden de andere 3 coordinaten berekend.
        """
        x = coord.x
        y = coord.y

        huis.linksboven = Coord(x, y)

        x = x + huis.breedte
        huis.rechtsboven = Coord(x, y)

        y = y - huis.hoogte
        huis.rechtsonder= Coord(x, y)

        x = x - huis.breedte
        huis.linksonder = Coord(x,y)


    def visualisatie(self):
        fig, ax = plt.subplots()

        for huis in self.wijk_lijst:
            if huis.id < 300:
                rect = patches.Rectangle(huis.linksonder.coords(), huis.breedte,
                huis.hoogte, linewidth=1,edgecolor='black',facecolor='none')
            else:
                # Id >= 1000 staat voor water. Water heeft een blauwe omlijning
                # om verschil aan te geven met huizen.
                rect = patches.Rectangle(huis.linksonder.coords(), huis.breedte,
                huis.hoogte, linewidth=1,edgecolor='blue',facecolor='none')

            ax.add_patch(rect)
            rx, ry = rect.get_xy()
            cx = rx + rect.get_width()/2.0
            cy = ry + rect.get_height()/2.0

            # Afhankelijk van het soort huis en sloot krijgt ie een eigen kleur
            # in de visualisatie.
            if huis.id < 100:
                ax.annotate(huis.id, (cx, cy), color='red', weight='bold',
                    fontsize=6, ha='center', va='center')
            elif 100 <= huis.id < 200:
                ax.annotate(huis.id, (cx, cy), color='black', weight='bold',
                    fontsize=6, ha='center', va='center')
            elif 200 <= huis.id < 300:
                ax.annotate(huis.id, (cx, cy), color='green', weight='bold',
                    fontsize=6, ha='center', va='center')
            elif huis.id >= 1000:
                ax.annotate(huis.id, (cx, cy), color='blue', weight='bold',
                    fontsize=6, ha='center', va='center')

        ax.set_xlim([0, 180])
        ax.set_ylim([0, 160])

        plt.xlabel('Breedte in meters')
        plt.ylabel('Hoogte in meters ')
        plt.title('Plattegrond AmstelHaege')

        plt.show()


    def totale_nieuwe_huiswaarde(self):
        """
            Door de 'totale_nieuwe_huiswaarde' functie worden alle nieuwe
            prijzen per huis ('nieuwe_huiswaarde_calc') worden bij elkaar
            opgeteld om de totale waarde van de wijk te krijgen.
        """

        self.totaalwaarde = 0

        for huis in self.wijk_lijst:
            ander, afstand = huis.dichtsbijzijnde_huis(self.wijk_lijst)
            self.totaalwaarde += huis.nieuwe_huiswaarde_calc(afstand)

        return self.totaalwaarde

    def plaats_random(self, huis, plattegrond):
        """
            Elk huis krijgt een random linksboven coordinaat binnen de
            plattegrond bij plaats huis word het huis door middel van de
            coordinaat opgebouwd.
            De huizen mogen elkaar niet overlappen.
        """

        # Als een huis niet geplaatst is heeft het geen x waarde
        while huis.linksboven.x == None:
            x = random.randint(0, plattegrond.breedte)
            y = random.randint(0, plattegrond.hoogte)
            coordinaat = Coord(x, y)
            self.plaats_huis(huis, coordinaat)
            if not plattegrond.grens_check(huis) or plattegrond.overlap_check(huis, self.wijk_lijst):
                huis.reset()

    def plaats_huizen(self, plattegrond):
        """
            'Plaats_huizen' roept de functie 'plaats_huis' aan om huizen op de
            plattegrond te zetten. Het maakt gebruik van de plattegrond welk de
            oppervlakte van de wijk weergeeft.
        """

        for huis in self.wijk_lijst:
            self.plaats_random(huis, plattegrond)


    def herplaats_huis(self, plattegrond):
        """
            Een random huis word gekozen uit de wijk_lijst om vervolgens op
            een andere random plek te worden geplaatst.
            Het huis met het nieuwe linksboven coordinaat word gereturnd.
        """

        huis = random.choice(self.wijk_lijst)
        linksboven = huis.linksboven
        huis.reset()

        self.plaats_random(huis, plattegrond)

        return huis, linksboven


    def schuif_huis(self):
        """
            Een huis word verschoven naar een nieuwe plek en het oude
            linksboven coordinaat word opgeslagen. Wanneer het huis naar een plek
            wordt verschoven dat niet binnen de grenzen ligt of voor overlap
            zorgt wordt het terug geplaats.
        """

        huis = random.choice(self.wijk_lijst)
        linksboven_oud = huis.linksboven

        schuifx = random.randint(-10, 10)
        schuify = random.randint(-10, 10)

        linksboven_nieuw = Coord(linksboven_oud.x + schuifx, linksboven_oud.y
                            + schuify)
        self.plaats_huis(huis, linksboven_nieuw)

        return huis, linksboven_oud

    # 
    # def opslaan_wijk(self):
    #     """
    #         In een dictionary worden alle coordinaten van elk huis dat zich in
    #         de huidige wijk bevindt opgeslagen.
    #         Deze dictionary wordt vervolgens gereturnd.
    #     """
    #
    #     beginwijk_dict = {}
    #     for huiscoord in self.wijk_lijst:
    #         beginwijk_dict[huiscoord] = huiscoord.linksboven
    #     return beginwijk_dict
    #
    #
    # def herplaats_wijk(self, beginwijk_dict):
    #     """
    #         Met behulp van de opgeslagen beginwijk door 'opslaan_wijk' kan de
    #         wijk indien nodig herplaatst worden naar die oplossing. De vorige
    #         linksboven-coordinaat wordt namelijk gebruikt om het huis terug
    #         te plaatsen.
    #     """
    #
    #     for huiscoord in beginwijk_dict.keys():
    #         linksboven = beginwijk_dict[huiscoord]
    #         for huis in self.wijk_lijst:
    #             self.plaats_huis(huis, linksboven)
    #             if not plattegrond.grens_check(huis) or plattegrond.overlap_check(huis, self.wijk_lijst):
    #                 huis.herplaats_huis()
