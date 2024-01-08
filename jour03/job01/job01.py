class Ville:
    def __init__(self, nom, nb_habitants):
        self._nom = nom
        self._nb_habitants = nb_habitants

    def get_nb_habitants(self):
        return self._nb_habitants


class Personne:
    def __init__(self, nom, age, ville):
        self._nom = nom
        self._age = age
        self._ville = ville

    def ajouterPopulation(self):
        self._ville._nb_habitants += 1

ville_paris = Ville("Paris", 1000000)
print("Population de la ville de Paris :", ville_paris.get_nb_habitants())

ville_marseille = Ville("Marseille", 861635)
print("Population de la ville de Marseille :", ville_marseille.get_nb_habitants())

john = Personne("John", 45, ville_paris)
myrtille = Personne("Myrtille", 4, ville_paris)
chloe = Personne("Chloé", 18, ville_marseille)

john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

print("Mise à jours de la population de la ville de Paris :", ville_paris.get_nb_habitants())
print("Mise à jours de la population de la ville de Marseille :", ville_marseille.get_nb_habitants())
