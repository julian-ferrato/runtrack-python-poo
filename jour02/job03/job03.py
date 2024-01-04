class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self._titre = titre
        self._auteur = auteur
        self._nb_pages = nb_pages
        self._disponible = True

    def getTitre(self):
        return self._titre

    def setTitre(self, nouveau_titre):
        self._titre = nouveau_titre

    def getAuteur(self):
        return self._auteur

    def setAuteur(self, nouvel_auteur):
        self._auteur = nouvel_auteur

    def getNbPages(self):
        return self._nb_pages

    def setNbPages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self._nb_pages = nouveau_nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

    def vérification(self):
        return self._disponible

    def emprunter(self):
        if self._disponible:
            self._disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible.")

    def rendre(self):
        if not self._disponible:
            self._disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre était déjà disponible.")

mon_livre = Livre("Python for Beginners", "John Doe", 300)

print("Est-ce que le livre est disponible ?", mon_livre.vérification())

mon_livre.emprunter()

print("Est-ce que le livre est disponible après emprunt ?", mon_livre.vérification())

mon_livre.rendre()

print("Est-ce que le livre est disponible après rendu ?", mon_livre.vérification())
