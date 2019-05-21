"""
Amstel1
Heuristieken
plattegrond.py
Deze class bevat de instantie van de plattegrond en alle functies die de
plattegrond zal uitvoeren met de huizen.
"""

class Plattegrond():
    def __init__(self, breedte, hoogte):
        """
        De 'init' functie geeft weer welke afmetingen de plattegrond heeft.
        """
        self.breedte= 180
        self.hoogte= 160
        self.oppervlakte = 160*180


    def grens_check(self, huis):
        """
        De plattegrond berekent met behulp van de 'grens_check' of alle huizen
        binnen de toegekende afmetingen liggen.
        """
        if huis.linksboven.x < 0 or huis.rechtsboven.x > self.breedte:
            return False
        if huis.linksonder.y < 0 or huis.rechtsboven.y > self.hoogte:
            return False
        return True

    # def sloot_verhouding_check(self, coord):
    #
    #     if sloot.breedte > 4 * sloot.hoogte:
    #         return False
    #     else:
    #         return True


    def overlap_check(self, huis, huizen_lijst):
        """
        De plattegrond berekent met behulp van de 'overlap_check' of huizen
        elkaar niet overlappen. Er wordt false gereturnt als dit het geval is
        en dit betekent dat het huis niet goed is geplaatst.
        """

        for ander_huis in huizen_lijst:
            # Check of huizen die de functie wil vergelijken al coordinaten
            # hebben oftewel, zijn geplaatst.
            if ander_huis.linksboven.x != None and huis is not ander_huis:
                # Elk huis heeft op de plattegrond zijn minimale vrijstand.
                afstand = huis.vrijstandscalc(ander_huis)
                if afstand > huis.min_vrijstand:
                    continue

                return True
        return False
