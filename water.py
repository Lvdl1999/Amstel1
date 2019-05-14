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
