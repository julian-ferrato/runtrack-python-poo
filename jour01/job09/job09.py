class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        infos = f"Nom : {self.nom}, Prix HT : {self.prixHT}, TVA : {self.TVA}%"
        return infos

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def obtenirNom(self):
        return self.nom

    def obtenirPrix(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA

produit1 = Produit("Red Bull", 10, 20)
produit2 = Produit("Mario", 20, 15)
produit3 = Produit("Burger King", 15, 25)

print("Red Bull:")
print("Infos :", produit1.afficher())
print("Prix TTC :", produit1.calculerPrixTTC())
produit1.modifierNom("Monster")
produit1.modifierPrix(15)
print("Nouveau nom :", produit1.obtenirNom())
print("Nouveau prix :", produit1.obtenirPrix())

print("\nMario:")
print("Infos :", produit2.afficher())
print("Prix TTC :", produit2.calculerPrixTTC())
produit2.modifierNom("Wario")
produit2.modifierPrix(25)
print("Nouveau nom :", produit2.obtenirNom())
print("Nouveau prix :", produit2.obtenirPrix())

print("\nBurger King")
print("Infos :", produit3.afficher())
print("Prix TTC :", produit3.calculerPrixTTC())
produit3.modifierNom("McDo")
produit3.modifierPrix(20)
print("Nouveau nom :", produit3.obtenirNom())
print("Nouveau prix :", produit3.obtenirPrix())
