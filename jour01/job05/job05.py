class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Coordonnée horizontale (x) : {self.x}")

    def afficherY(self):
        print(f"Coordonnée verticale (y) : {self.y}")

    def changerX(self, nouvelle_valeur):
        self.x = nouvelle_valeur

    def changerY(self, nouvelle_valeur):
        self.y = nouvelle_valeur

point = Point(3, 5)

point.afficherLesPoints()
point.afficherX()
point.afficherY()

point.changerX(4)
point.changerY(9)

point.afficherLesPoints()
point.afficherX()
point.afficherY()
