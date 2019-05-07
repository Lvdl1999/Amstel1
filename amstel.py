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


    def vrijstandscalc1(self):
        pass
        # per huis kijken welk coordinaat is het dichtsbijzijnd
        # niet met jezelf vergelijken!
        # elk punt van een huis met elk punt van ander huis vergelijken
        # de kortste afstand opslaan
        # alle kortste afstanden tussen huizen vergelijken
        # vind optimala kortste afstand van hoekpunten
        # dan horizontaal en verticaal pas
        #
        for ander_huis in huizen_lijst:
            if huis is not ander_huis:
                afst_lblb = math.sqrt(((ander_huis.linksboven.x - huis.linksboven.x)**2) -((ander_huis.linksboven.y - huis.linksboven.y)**2))
                afst_lbrb = math.sqrt(((ander_huis.linksboven.x - huis.rechtsboven.x)**2) -((ander_huis.linksboven.y - huis.rechtsboven.y)**2))
                afst_lbro = math.sqrt(((ander_huis.linksboven.x - huis.rechtsonder.x)**2) -((ander_huis.linksboven.y - huis.rechtsonder.y)**2))
                afst_lblo = math.sqrt(((ander_huis.linksboven.x - huis.linksonder.x)**2) -((ander_huis.linksboven.y - huis.linksonder.y)**2))
                kortste_afstand_lb = min(float(afst_lblb), float(afst_lbrb), float(afst_lbro), float(afst_lblo))

                afst_rblb = math.sqrt(((ander_huis.rechtsboven.x - huis.linksboven.x)**2) -((ander_huis.rechtsboven.y - huis.linksboven.y)**2))
                afst_rbrb = math.sqrt(((ander_huis.rechtsboven.x - huis.rechtsboven.x)**2) -((ander_huis.rechtsboven.y - huis.rechtsboven.y)**2))
                afst_rbro = math.sqrt(((ander_huis.rechtsboven.x - huis.rechtsonder.x)**2) -((ander_huis.rechtsboven.y - huis.rechtsonder.y)**2))
                afst_rblo = math.sqrt(((ander_huis.rechtsboven.x - huis.linksonder.x)**2) -((ander_huis.rechtsboven.y - huis.linksonder.y)**2))
                kortste_afstand_rb = min(float(afst_rblb), float(afst_rbrb), float(afst_rbro), float(afst_rblo))

                afst_lolb = math.sqrt(((ander_huis.linksonder.x - huis.linksboven.x)**2) -((ander_huis.linksonder.y - huis.linksboven.y)**2))
                afst_lorb = math.sqrt(((ander_huis.linksonder.x - huis.rechtsboven.x)**2) -((ander_huis.linksonder.y - huis.rechtsboven.y)**2))
                afst_loro = math.sqrt(((ander_huis.linksonder.x - huis.rechtsonder.x)**2) -((ander_huis.linksonder.y - huis.rechtsonder.y)**2))
                afst_lolo = math.sqrt(((ander_huis.linksonder.x - huis.linksonder.x)**2) -((ander_huis.linksonder.y - huis.linksonder.y)**2))
                kortste_afstand_lo = min(float(afst_lolb), float(afst_lorb), float(afst_loro), float(afst_lolo))

                afst_rolb = math.sqrt(((ander_huis.rechtsonder.x - huis.linksboven.x)**2) -((ander_huis.rechtsonder.y - huis.linksboven.y)**2))
                afst_rorb = math.sqrt(((ander_huis.rechtsonder.x - huis.rechtsboven.x)**2) -((ander_huis.rechtsonder.y - huis.rechtsboven.y)**2))
                afst_roro = math.sqrt(((ander_huis.rechtsonder.x - huis.rechtsonder.x)**2) -((ander_huis.rechtsonder.y - huis.rechtsonder.y)**2))
                afst_rolo = math.sqrt(((ander_huis.rechtsonder.x - huis.linksonder.x)**2) -((ander_huis.rechtsonder.y - huis.linksonder.y)**2))
                kortste_afstand_ro = min(float(afst_rolb), float(afst_rorb), float(afst_roro), float(afst_rolo))

                korste_afstand = min(kortste_afstand_lb, kortste_afstand_rb, kortste_afstand_lo, kortste_afstand_ro)


    # Voor dinsdag (07-04-19)
    #
    # Functie vrijstandsberekening maken
    #
    # Constraints wijk (incl minimale vrijstand elk huis)
    # —> valide oplossing
    #
    # Waarde wijk berekenen
    # Random
    #
    #
    # Optioneel
    # Visualitie verbetering met vrijstand
    # Nadenken over Algoritmes

    # def vrijstandscalc(self):
    #
    #
    #     ander_huis.linksboven.x = A1
    #     ander_huis.rechtsboven.x = A2
    #     ander_huis.rechtsonder.x = A3
    #     ander_huis.linksonder.x = A4
    #
    #     ander_huis.linksboven.y = A5
    #     ander_huis.rechtsboven.y = A6
    #     ander_huis.rechtsonder.y = A7
    #     ander_huis.linksonder.y = A8
    #
    #     # VOOR LINKSBOVEN A1 en A5
    #     # (en vervolgens ook A2, A3, A4 A6, A7 en A8)
    #     afst_lblb = math.sqrt(((A1 - huis.linksboven.x)**2) -((A5 - huis.linksboven.y)**2))
    #     afst_lbrb = math.sqrt(((A1 - huis.rechtsboven.x)**2) -((A5 - huis.rechtsboven.y)**2))
    #     afst_lbro = math.sqrt(((A1 - huis.rechtsonder.x)**2) -((A5 - huis.rechtsonder.y)**2))
    #     afst_lblo = math.sqrt(((A1 - huis.linksonder.x)**2) -((A5 - huis.linksonder.y)**2))
    #     kortste_afstand_lb = min(float(afst_lblb), float(afst_lbrb), float(afst_lbro), float(afst_lblo))

        # Voor elk hoekpunt de formule aanroepen dus A1, A2, A3, A4 en A5, A6, A7, A8
        # Variabele meegeven en telkens aanpassen?
        # Uiteindelijk kleinste afstand returnen (dat is de vrijstand)

        def vrijstandscalc3(self, ander):
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
    def dichtsbijzijnde_huis(self):
        dichtstbij = None
        kortste_afstand = None
        # afstand alleen berekenen voor andere huizen en niet de zelfde
        for ander_huis in huizen_lijst:
            if huis is ander_huis:
                continue
            else:
                afstand = vrijstandscalc3(self)
                # save if closest yet
                if not dichtstbij and not kortste_afstand:
                    dichtstbij = ander_huis
                    kortste_afstand = afstand
                # als de afstand korter is dan de kortste_afstand zal de kortste_afstand moeten worden aangepast
            elif afstand < kortste_afstand:
                    dichtstbij = ander_huis
                    kortste_afstand = afstand
        return dichtstbij, kortste_afstand




    # Loop over de huizen_lijst om het dichtstbijzijnde buurhuis te vinden
    for huis in huizen_lijst:
        dichtstbij, kortste_afstand = dichtsbijzijnde_huis(self)
        print("Het dichtstbijzijnde buurhuis is huis.id", huis, "is house.id", dichtsbij,
            "op afstand", kortste_afstand)

    def nieuwe_huiswaarde(self, amstel):

        # itereer over lijst met huizen . zoek per huis prijs op
        # en tel daarbij vrijstandscalc* waardevermeerdering per huis op
        # om nieuwe waarde te krijgen
        nieuwe_huiswaarde_lijst = []

        for huis in amstel.huizen_lijst:
            oude_huisprijs= amstel.huizen_lijst["prijs"]
            waardevermeerdering = amstel.huizen_lijst["prijsverbetering"]
            nieuwe_huiswaarde = oude_huisprijs + waardevermeerdering*(vrijstandscalc3 - amstel.huizen_lijst["min_vrijstand"])
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
                # huizen op plattegrond inclusief hun minimale vrijstand
                if huis.breedte is 8 and kortste_afstand < 2
                    huis.reset_huis()
                if huis.breedte is 7.5 and kortste_afstand < 3
                    huis.reset_huis()
                if huis.breedte is 10.5 and kortste_afstand < 6
                    huis.reset_huis()
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
