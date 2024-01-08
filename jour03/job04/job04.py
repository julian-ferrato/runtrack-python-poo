class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom} (Joueur n°{self.numero}) - Position : {self.position}")
        print(f"Buts marqués : {self.buts_marques}")
        print(f"Passes décisives : {self.passes_decisives}")
        print(f"Cartons jaunes : {self.cartons_jaunes}")
        print(f"Cartons rouges : {self.cartons_rouges}\n")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)
        print(f"Le joueur {joueur.nom} a été ajouté à l'équipe {self.nom}.")

    def AfficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.liste_joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()
                print(f"Statistiques de {joueur.nom} mises à jour.\n")
                return
        print(f"Joueur {nom_joueur} non trouvé dans l'équipe.")


joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Neymar", 11, "Attaquant")
joueur4 = Joueur("Mbappé", 7, "Attaquant")

equipe1 = Equipe("Barcelona")
equipe2 = Equipe("PSG")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur4)

equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()

equipe1.mettreAJourStatistiquesJoueur("Messi", "but")
equipe1.mettreAJourStatistiquesJoueur("Ronaldo", "passe")
equipe2.mettreAJourStatistiquesJoueur("Neymar", "jaune")
equipe2.mettreAJourStatistiquesJoueur("Mbappé", "rouge")

equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()
