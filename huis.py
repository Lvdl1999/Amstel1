from coord import Coord
import math

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
