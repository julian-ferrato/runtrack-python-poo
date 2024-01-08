class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def marquerCommeFinie(self):
        self.statut = "terminée"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)
        print(f"Tâche '{tache.titre}' ajoutée à la liste.")

    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                print(f"Tâche '{titre}' supprimée de la liste.")
                return
        print(f"Tâche '{titre}' non trouvée dans la liste.")

    def afficherListe(self):
        for tache in self.taches:
            print(f"Tâche : {tache.titre}, Description : {tache.description}, Statut : {tache.statut}")

    def filterListe(self, statut):
        filtered_list = [tache for tache in self.taches if tache.statut == statut]
        return filtered_list

liste_taches = ListeDeTaches()

tache1 = Tache("Faire les courses", "Acheter du lait et du pain")
tache2 = Tache("Répondre aux e-mails", "Répondre aux e-mails professionnels")
tache3 = Tache("Appeler le plombier", "Prendre rendez-vous pour la réparation")

liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

liste_taches.afficherListe()

liste_taches.supprimerTache("Faire les courses")

tache2.marquerCommeFinie()

taches_a_faire = liste_taches.filterListe("à faire")
print("\nTâches à faire :")
for tache in taches_a_faire:
    print(f"Tâche : {tache.titre}, Description : {tache.description}, Statut : {tache.statut}")
