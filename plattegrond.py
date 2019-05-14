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
