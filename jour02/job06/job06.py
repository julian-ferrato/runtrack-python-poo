class Commande:
    def __init__(self, numero_commande):
        self._numero_commande = numero_commande
        self._plats_commandes = {}
        self._statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        self._plats_commandes[nom_plat] = {"prix": prix_plat, "statut": self._statut_commande}
        print(f"Le plat '{nom_plat}' a été ajouté à la commande.")

    def annuler_commande(self):
        self._statut_commande = "annulée"
        print("La commande a été annulée.")

    def _calculer_total(self):
        total = sum(plat["prix"] for plat in self._plats_commandes.values())
        return total

    def afficher_commande(self):
        total = self._calculer_total()
        print(f"Numéro de commande : {self._numero_commande}")
        print("Plats commandés :")
        for plat, details in self._plats_commandes.items():
            print(f"- {plat} : {details['prix']} $ - Statut : {details['statut']}")
        print(f"Total à payer : {total} $")

    def calculer_tva(self):
        total = self._calculer_total()
        tva = total * 0.15  
        print(f"Le montant de la TVA est de : {tva} $")

ma_commande = Commande("CMD001")

ma_commande.ajouter_plat("Pizza", 12)
ma_commande.ajouter_plat("Pâtes", 10)
ma_commande.ajouter_plat("Salade", 8)

ma_commande.annuler_commande()

ma_commande.afficher_commande()

ma_commande.calculer_tva()
