class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    def getLongueur(self):
        return self._longueur

    def setLongueur(self, nouvelle_longueur):
        self._longueur = nouvelle_longueur

    def getLargeur(self):
        return self._largeur

    def setLargeur(self, nouvelle_largeur):
        self._largeur = nouvelle_largeur

mon_rectangle = Rectangle(10, 5)

mon_rectangle.setLongueur(15)
mon_rectangle.setLargeur(7)

print("Longueur du rectangle :", mon_rectangle.getLongueur())
print("Largeur du rectangle :", mon_rectangle.getLargeur())
