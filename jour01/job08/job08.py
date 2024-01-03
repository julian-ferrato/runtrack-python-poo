import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"Informations du cercle - Rayon : {self.rayon}")

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)

    def diametre(self):
        return 2 * self.rayon

cercle1 = Cercle(4)
cercle2 = Cercle(7)

cercle1.afficherInfos()
print("Circonférence du cercle 1 :", cercle1.circonference())
print("Diamètre du cercle 1 :", cercle1.diametre())
print("Aire du cercle 1 :", cercle1.aire())

print("\n")

cercle2.afficherInfos()
print("Circonférence du cercle 2 :", cercle2.circonference())
print("Diamètre du cercle 2 :", cercle2.diametre())
print("Aire du cercle 2 :", cercle2.aire())
