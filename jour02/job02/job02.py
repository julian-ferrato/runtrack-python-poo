class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self._titre = titre
        self._auteur = auteur
        self._nb_pages = nb_pages

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

mon_livre = Livre("Python for Beginners", "John Doe", 300)

mon_livre.setTitre("Python Advanced")
mon_livre.setAuteur("Jane Smith")
mon_livre.setNbPages(400) 

print("Titre :", mon_livre.getTitre())
print("Auteur :", mon_livre.getAuteur())
print("Nombre de pages :", mon_livre.getNbPages())

mon_livre.setNbPages("500") 
