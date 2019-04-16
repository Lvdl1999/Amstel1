"""
Amstel1
Heuristieken
amstel.py
Build and optimize our neighbourhood.
"""


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
        self.aantal_sloten = input("Aantal sloten:  ") # dit doen we voorlopig om zelf water in te richten

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


    def ondergrens(self):
        # Geen waarde vermeerderingen door extra vrijstand. Onder voorbehoudt dat alle huizen kunnen worden geplaats.
        # In huizen_lijst opzoeken prijs per soort woning * aantal dat soort woning
        self.aantal_eengezinswoning * self.huizen_lijst["prijs"]

    def bovengrens(self):
        pass

    def totale_nieuwe_huiswaarde(self, Huis):
        pass


class Huis():
    def __init__(self, id, min_vrijstand, prijs, prijsverbetering, breedte, hoogte):

        self.id= int(id)
        self.min_vrijstand = int(min_vrijstand)
        self.prijs = int(prijs)
        self.prijsverbetering = float(prijsverbetering)
        self.breedte= breedte
        self.hoogte = hoogte
        self.linksboven= None
        self.rechtsboven= None
        self.linksonder= None
        self.rechtsonder= None


    def vrijstandscalc(self):
        # extra vrijstand per huis
        pass

    def nieuwe_huiswaarde(self, amstel):

        # itereer over lijst met huizen . zoek per huis prijs op
        # en tel daarbij vrijstandscalc* waardevermeerdering per huis op
        # om nieuwe waarde te krijgen
        nieuwe_huiswaarde_lijst = []

        for i in range(amstel.huizen_lijst):
            oude_huisprijs= amstel.huizen_lijst["prijs"]
            waardevermeerdering = amstel.huizen_lijst["prijsverbetering"]
            nieuwe_huiswaarde =oude_huisprijs + waardevermeerdering*vrijstandscalc
            nieuwe_huiswaarde_lijst.append(nieuwe_huiswaarde)

    def __str__(self):
        return f"id = {self.id},min_vrijstand = {self.min_vrijstand}, prijs = {self.prijs}, prijsverbetering = {self.prijsverbetering}"


class Plattegrond():
    def __init__(self, breedte, hoogte):

        X = int(180)
        Y = int(160)

        self.breedte= int(X)
        self.hoogte= int(Y)


    # Structuur om te kijken naar overlap
    # X en Y van twee huizen mogen niet hetzelfde zijn
    # &
    # 4 punten moeten minimale vrijstand van elkaar verwijderd zijn





def plaats_huis():

     #huizen op de plattegrond plaatsen met 4 punten (x en y)  en soort huis
     for i in range range(amstel.huizen_lijst):
         huis = amstel.huizen_lijst[i]


class Water():
    def __init__(self, oppervlakte, aantal_sloten):

        self.oppervlakte= oppervlakte
        self.aantal_sloten = aantal_sloten

if __name__ == '__main__':
    amster = Amstel()
    print(amster.huizen_lijst[13])
    huis = amster.huizen_lijst[0]
    huis.linksboven = (0, 160)
    huis.rechtsboven =


#voor donderdag:

#methode om te plaatsen
#methode/functie die huizen random indeeld zonder rekening te houden met overlap (algoritme)
#kleine structuur voor het kijken naar overlap
#begin aan visualisatie met matplotlip
#scatterplot met rectangles
