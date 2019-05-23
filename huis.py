"""
Amstel1
Heuristieken
huis.py
Deze class bevat de instantie van een huis en alle functies die een huis
voor zichzelf kan uitrekenen.
"""

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
        """
            Coords returnt vier coordinaten die een huis representeren.
        """
        return (self.linksboven, self.rechtsboven, self.linksonder, self.rechtsonder)


    def vrijstandscalc(self, ander):
        """
            In de vrijstandscalc wordt de afstand tussen twee huizen berekent.
            Er wordt gekeken naar de lijnen in de breedte en hoogte tussen
            de huizen.
        """

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

        # Huizen liggen naast elkaar dus horizontale afstand wordt
        # berekent en dx blijft 0.
        if links > ander_rechts or rechts < ander_links:
            dx = min([abs(links - ander_rechts), abs(rechts - ander_links)])

        # Huizen liggen boven elkaar dus horizontale afstand wordt
        # berekent en dy blijft 0.
        if boven < ander_onder or onder > ander_boven:
            dy = min([abs(boven - ander_onder), abs(onder - ander_boven)])

        # Ligt een huis niet op dezelfde hoogte of breedte dan wordt de afstand
        # gemeten door een schuine lijn met behulp van pythagoras.
        return math.sqrt(dx**2 + dy**2)



    # zoekt de dichtstbijzijnde buurman door met alle huizen te vergelijken uit de huizen_lijst
    def dichtsbijzijnde_huis(self, huizen_lijst):
        """
            De functie 'dichtstbijzijnde_huis vergelijkt alle afstanden tussen
            zichzelf en huizen eromheen en returnt het dichtstbijzijnde huis en
            de kortste afstand ertussen'
        """
        # Zodra de functie begint zijn deze waardes nog onbekend.
        dichtstbij = None
        kortste_afstand = float('inf')

        # De afstand van een huis wordt niet met zichzelf berekent.
        for ander_huis in huizen_lijst:
            if self is ander_huis or ander_huis.id >=1000:
                continue
            else:
                afstand = self.vrijstandscalc(ander_huis)

                # Als een gevonden afstand tussen twee huizen kleiner is dan
                # de huidige kleinste afstand wordt deze vervangen.
                if afstand < kortste_afstand:
                    dichtstbij = ander_huis
                    kortste_afstand = afstand

        return dichtstbij, kortste_afstand

    def nieuwe_huiswaarde_calc(self, kortste_afstand):
        """
            Bij de functie 'nieuwe_huiswaarde_calc' berekent en returnt een huis
            z'n eigen nieuwe huiswaarde met de berekende vrijstand in de wijk.
        """
        oude_huisprijs = float(self.prijs)
        waardevermeerdering = float(self.prijsverbetering)
        min_vrijstand = float(self.min_vrijstand)
        self.nieuwe_huiswaarde = (oude_huisprijs + ((oude_huisprijs *
                                waardevermeerdering) * (kortste_afstand
                                - min_vrijstand)))

        return self.nieuwe_huiswaarde

    def reset(self):
        """
            De functie 'reset' verwijdert de xy-coordinaten en zet ze op 'None'.
        """
        self.linksboven = Coord(None, None)
        self.rechtsboven = Coord(None, None)
        self.linksonder = Coord(None, None)
        self.rechtsonder = Coord(None, None)


    def __str__(self):
        """
            'str' is een toString methode die returnt het id, min_vrijstand,
            prijs en prijsverbetering van een huis in stringvorm ipv als object.
        """
        return f"id = {self.id},min_vrijstand = {self.min_vrijstand}, prijs = {self.prijs}, prijsverbetering = {self.prijsverbetering}"
