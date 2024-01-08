import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, cible):
        degats = random.randint(5, 15)
        print(f"{self.nom} attaque {cible.nom} et lui inflige {degats} points de dégâts.")
        cible.vie -= degats

class Jeu:
    def __init__(self):
        self.niveau = None

    def choisirNiveau(self):
        print("Choisissez votre niveau de difficulté :")
        print("1. Facile")
        print("2. Moyen")
        print("3. Difficile")
        choix = input("Entrez le numéro correspondant au niveau : ")
        if choix == "1":
            self.niveau = "Facile"
        elif choix == "2":
            self.niveau = "Moyen"
        elif choix == "3":
            self.niveau = "Difficile"
        else:
            print("Choix invalide. Niveau par défaut : Moyen.")
            self.niveau = "Moyen"

    def lancerJeu(self):
        self.choisirNiveau()
        if self.niveau == "Facile":
            joueur = Personnage("Joueur", 100)
            ennemi = Personnage("Ennemi", 50)
        elif self.niveau == "Moyen":
            joueur = Personnage("Joueur", 80)
            ennemi = Personnage("Ennemi", 80)
        else:
            joueur = Personnage("Joueur", 60)
            ennemi = Personnage("Ennemi", 100)

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"{ennemi.nom} a été vaincu ! Vous avez gagné !")
                break
            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"{joueur.nom} a été vaincu ! Vous avez perdu.")
                break

jeu = Jeu()
jeu.lancerJeu()
