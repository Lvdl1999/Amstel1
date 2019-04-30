"""
Amstel1
Heuristieken
amstel.py
Build and optimize our neighbourhood.
"""


import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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

    def visualisatie(self):
        fig, ax = plt.subplots()

        for huis in self.huizen_lijst:
            rect = patches.Rectangle(huis.linksonder.coords(), huis.breedte,
                huis.hoogte, linewidth=1,edgecolor='r',facecolor='none')
            ax.add_patch(rect)

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

    def totale_nieuwe_huiswaarde(self, Huis):
        pass


class Coord():
    def __init__(self, x, y):

        self.x = x
        self.y = y

    def coords(self):
        return (self.x, self.y)


class Huis():
    def __init__(self, id, min_vrijstand, prijs, prijsverbetering, breedte, hoogte):

        self.id= int(id)
        self.min_vrijstand = int(min_vrijstand)
        self.prijs = int(prijs)
        self.prijsverbetering = float(prijsverbetering)
        self.breedte= breedte
        self.hoogte = hoogte
        self.linksboven = Coord(None, None)
        self.rechtsboven = Coord(None, None)
        self.linksonder = Coord(None, None)
        self.rechtsonder = Coord(None, None)

    def coords(self):
        return (self.linksboven, self.rechtsboven, self.linksonder, self.rechtsonder)


    def vrijstandscalc(self):
        # per huis kijken welk coordinaat is het dichtsbijzijnd
        # niet met jezelf vergelijken!
        


    def nieuwe_huiswaarde(self, amstel):

        # itereer over lijst met huizen . zoek per huis prijs op
        # en tel daarbij vrijstandscalc* waardevermeerdering per huis op
        # om nieuwe waarde te krijgen
        nieuwe_huiswaarde_lijst = []

        for i in range(amstel.huizen_lijst):
            oude_huisprijs= amstel.huizen_lijst["prijs"]
            waardevermeerdering = amstel.huizen_lijst["prijsverbetering"]
            nieuwe_huiswaarde = oude_huisprijs + waardevermeerdering*vrijstandscalc
            nieuwe_huiswaarde_lijst.append(nieuwe_huiswaarde)

    def reset_huis(self):

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


    def grens_check(self, coord):
        if coord.x < 0 or coord.x > self.breedte:
            return False
        if coord.y < 0 or coord.y > self.hoogte:
            return False
        return True


    def overlap_check(self, huis, huizen_lijst):
    # hoe gaan we dit vergelijken met alle eerder geplaatste huizen?
    # forloop in een forloop??
        for ander_huis in huizen_lijst:
            # kijken of de huizen die je vergelijkt al coordinaten hebben
            if ander_huis.linksboven.x != None and huis is not ander_huis:
                # if one rectangle is on the left side of the other:
                if (huis.linksboven.x >= ander_huis.rechtsonder.x or ander_huis.linksboven.x >= huis.rechtsonder.x ):
                    continue
                # if one rectangle is above the other:
                if (huis.linksboven.y <= ander_huis.rechtsonder.y or ander_huis.linksboven.y <= huis.rechtsonder.y ):
                    continue
                return True
        return False


class Water():
    def __init__(self, oppervlakte, aantal_sloten):

        self.oppervlakte= oppervlakte
        self.aantal_sloten = aantal_sloten

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
                huis.reset_huis()


if __name__ == '__main__':
    amster = Amstel()
    print(amster.huizen_lijst[13])
    plattegrond = Plattegrond(160, 180)
    plaats_huizen(amster, plattegrond)
    amster.visualisatie()

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
