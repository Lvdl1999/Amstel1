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

class Amstel():
    """
    This is the Amstel neighbourhood class. It contains necessary
    attributes and methods to build and optimize a neighbourhood.
    """


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
        self.totaalwaarde = 0

        # self.sloten_lijst = []

        # elk huis object toevoegen aan lijst en daarbij behorend id elke keer met 1 verhogen.
        # je wilt dat elk huis een ander id heeft
        counter = 0
        for i in range(self.aantal_eengezinswoning):
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


        # rechtonder punt binnen de grid?
        # overlap checken

        if x < 0 or x > huis.breedte:
            return False
        if y < 0 or y > huis.hoogte:
            return False
        return True

    def plaats_huis(self, huis, coord):

        x = coord.x
        y = coord.y

        huis.linksboven = Coord(x, y)

        x = x + huis.breedte
        huis.rechtsboven = Coord(x, y)

        y = y - huis.hoogte
        huis.rechtsonder= Coord(x, y)

        x = x - huis.breedte
        huis.linksonder = Coord(x,y)

    #
    # def herplaats_huis(self, huis, coord):
    #
    #     print(random.self.huizen_lijst([0]))
    #
    #
    #     # random.huis.id()
    #
    #     x = coord.x + 2
    #     y = coord.y + 3
    #
    #     huis.linksboven = Coord(x, y)
    #
    #     x = x + huis.breedte
    #     huis.rechtsboven = Coord(x, y)
    #
    #     y = y - huis.hoogte
    #     huis.rechtsonder= Coord(x, y)
    #
    #     x = x - huis.breedte
    #     huis.linksonder = Coord(x,y)




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


class Coord():
    def __init__(self, x, y):

        self.x = x
        self.y = y

    def coords(self):
        return (self.x, self.y)


class Huis():
    def __init__(self, id, min_vrijstand, prijs, prijsverbetering, breedte, hoogte):

        self.id = int(id)
        self.min_vrijstand = int(min_vrijstand)
        self.prijs = int(prijs)
        self.prijsverbetering = float(prijsverbetering)
        self.breedte = breedte
        self.hoogte = hoogte
        self.linksboven = Coord(None, None)
        self.rechtsboven = Coord(None, None)
        self.linksonder = Coord(None, None)
        self.rechtsonder = Coord(None, None)
        self.nieuwe_huiswaarde = 0


    def coords(self):
        return (self.linksboven, self.rechtsboven, self.linksonder, self.rechtsonder)


    def vrijstandscalc(self, ander):
        # berekenen van de afstand tussen huizen
        #ik kijk naar de lijnen ! ipv de hoekpunten

        #     x1    x2
        # y1__|_____|
        #     |     |
        # y2__|_____|

        dx = 0
        dy = 0

        links = self.linksboven.x
        rechts = self.rechtsboven.x

        ander_links = ander.linksboven.x
        ander_rechts = ander.rechtsboven.x

        boven = self.linksboven.y
        onder = self.linksonder.y

        ander_boven = ander.linksboven.y
        ander_onder = ander.linksonder.y

        if links > ander_rechts or rechts < ander_links:
            dx = min([abs(links - ander_rechts), abs(rechts - ander_links)])

        if boven < ander_onder or onder > ander_boven:
            dy = min([abs(boven - ander_onder), abs(onder - ander_boven)])

        return math.sqrt(dx**2 + dy**2)



    # zoekt de dichtstbijzijnde buurman door met alle huizen te vergelijken uit de huizen_lijst
    def dichtsbijzijnde_huis(self, huizen_lijst):
        dichtstbij = None
        kortste_afstand = float('inf')
        # afstand alleen berekenen voor andere huizen en niet de zelfde
        for ander_huis in huizen_lijst:
            if self is ander_huis:
                continue
            else:
                afstand = self.vrijstandscalc(ander_huis)

                # als de afstand korter is dan de kortste_afstand zal de kortste_afstand moeten worden aangepast
                if afstand < kortste_afstand:
                    dichtstbij = ander_huis
                    kortste_afstand = afstand

        return dichtstbij, kortste_afstand

    def nieuwe_huiswaarde_calc(self, kortste_afstand):

        # itereer over lijst met huizen . zoek per huis prijs op
        # en tel daarbij vrijstandscalc* waardevermeerdering per huis op
        # om nieuwe waarde te krijgen

        oude_huisprijs = float(self.prijs)
        waardevermeerdering = float(self.prijsverbetering)
        min_vrijstand = float(self.min_vrijstand)
        self.nieuwe_huiswaarde = (((oude_huisprijs + waardevermeerdering) * kortste_afstand) - min_vrijstand)

        return self.nieuwe_huiswaarde


    def reset(self):

        self.linksboven = Coord(None, None)
        self.rechtsboven = Coord(None, None)
        self.linksonder = Coord(None, None)
        self.rechtsonder = Coord(None, None)


    def __str__(self):
        return f"id = {self.id},min_vrijstand = {self.min_vrijstand}, prijs = {self.prijs}, prijsverbetering = {self.prijsverbetering}"


class Plattegrond():
    def __init__(self, breedte, hoogte):

        self.breedte= 180
        self.hoogte= 160
        self.oppervlakte = 160*180


    def grens_check(self, coord):
        if coord.x < 0 or coord.x > self.breedte:
            return False
        if coord.y < 0 or coord.y > self.hoogte:
            return False
        return True

    # def sloot_verhouding_check(self, coord):
    #
    #     if sloot.breedte > 4 * sloot.hoogte:
    #         return False
    #     else:
    #         return True


    def overlap_check(self, huis, huizen_lijst):
    # hoe gaan we dit vergelijken met alle eerder geplaatste huizen?
    # forloop in een forloop??
        for ander_huis in huizen_lijst:
            # kijken of de huizen die je vergelijkt al coordinaten hebben
            if ander_huis.linksboven.x != None and huis is not ander_huis:
                # huizen op plattegrond inclusief hun minimale vrijstand
                afstand = huis.vrijstandscalc(ander_huis)
                if afstand > huis.min_vrijstand:
                    continue

                return True
        return False


# def herplaats_huizen(amstel):
#
#     for huis in amstel.huizen_lijst:
#         huis.reset()
#
#     plaats_huizen(amstel, plattegrond)


class Water():
    def __init__(self, id, aantal_sloten, slootopp):

        self.id = int(id)
        self.linksboven = Coord(None, None)
        self.rechtsboven = Coord(None, None)
        self.linksonder = Coord(None, None)
        self.rechtsonder = Coord(None, None)
        self.aantal_sloten = aantal_sloten
        self.slootopp = float(plattegrond.oppervlakte * 0.2)

        self.hoogte = hoogte
        self.breedte <= 4 * self.hoogte


def plaats_huizen(amstel, plattegrond):

     #huizen op de plattegrond plaatsen met 4 punten (x en y)  en soort huis

    for huis in amstel.huizen_lijst:
        # Als een huis niet geplaatst is heeft het geen x waarde
        while huis.linksboven.x == None:
            x = random.randint(0, plattegrond.breedte)
            y = random.randint(0, plattegrond.hoogte)
            coordinaat = Coord(x, y)
            amstel.plaats_huis(huis, coordinaat)
            if not plattegrond.grens_check(huis.rechtsonder) or plattegrond.overlap_check(huis, amstel.huizen_lijst):
                huis.reset()

def herplaats_huis(amstel, plattegrond, huizen_lijst):

    huis.id = random.huizen_lijst([0])
    while huis.id != None:
        huis.reset()

    # Als een huis niet geplaatst is heeft het geen x waarde
    while huis.linksboven.x == None:
        x = random.randint(0, plattegrond.breedte)
        y = random.randint(0, plattegrond.hoogte)
        coordinaat = Coord(x + 5, y + 5)
        amstel.plaats_huis(huis, coordinaat)
        if not plattegrond.grens_check(huis.rechtsonder) or plattegrond.overlap_check(huis, amstel.huizen_lijst):
            huis.reset()




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


if __name__ == '__main__':
    amster = Amstel()
    print(amster.huizen_lijst[13])
    plattegrond = Plattegrond(160, 180)
    plaats_huizen(amster, plattegrond)

    # Loop over de huizen_lijst om het dichtstbijzijnde buurhuis te vinden
    for huis in amster.huizen_lijst:
        dichtstbij, kortste_afstand = huis.dichtsbijzijnde_huis(amster.huizen_lijst)
        print(f"Voor {huis.id} is het dichtstbijzijnde huis {dichtstbij.id}. Met afstand van {kortste_afstand}m.")

    print(f"Totale wijk waarde is: {int(amster.totale_nieuwe_huiswaarde())} euro")

    amster.visualisatie()

    while True:
        antwoord = input("Wil je random een huis verplaatsen?:  ")
        if antwoord not in ["ja", "nee"]:
            print("Beantwoord vraag met ja of nee")
        elif antwoord == "ja":
            herplaats_huis(amster, plattegrond)
            print(f"Totale wijk waarde is: {int(amster.totale_nieuwe_huiswaarde())} euro")
        else:
            break

    #huis = amster.huizen_lijst[0]
    #huis.linksboven = (0, 160)
    #huis.rechtsboven =


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
