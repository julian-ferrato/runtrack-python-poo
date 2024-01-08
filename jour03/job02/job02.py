class CompteBancaire:
    def __init__(self, num_compte, nom, prenom, solde, decouvert=False):
        self._num_compte = num_compte
        self._nom = nom
        self._prenom = prenom
        self._solde = solde
        self._decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte : {self._num_compte}")
        print(f"Titulaire du compte : {self._prenom} {self._nom}")
        print(f"Solde du compte : {self._solde}")
        print(f"Autorisation de découvert : {self._decouvert}")

    def afficherSolde(self):
        print(f"Le solde du compte est de : {self._solde}")

    def versement(self, montant):
        self._solde += montant
        print(f"Versement de {montant} $ effectué. Nouveau solde : {self._solde}")

    def retrait(self, montant):
        if self._decouvert or self._solde >= montant:
            self._solde -= montant
            print(f"Retrait de {montant} $ effectué. Nouveau solde : {self._solde}")
        else:
            print("Fonds insuffisants. Opération annulée.")

    def agios(self):
        if self._solde < 0:
            frais = abs(self._solde) * 0.1      
            self._solde -= frais
            print(f"Des agios de {frais} $ ont été appliqués. Nouveau solde : {self._solde}")

    def virement(self, compte_destinataire, montant):
        if self._solde >= montant:
            self._solde -= montant
            compte_destinataire._solde += montant
            print(f"Virement de {montant} $ effectué vers le compte {compte_destinataire._num_compte}.")
        else:
            print("Fonds insuffisants pour effectuer le virement.")

compte1 = CompteBancaire("12345", "FERRATO", "Julian", 1000)
compte1.afficher()
compte1.versement(500)
compte1.retrait(200)
compte1.agios()
compte1.afficherSolde()

compte2 = CompteBancaire("54321", "TOKISAKI", "Kurumi", -200, decouvert=True)
compte2.afficher()
compte2.retrait(100)
compte2.afficherSolde()

compte1.virement(compte2, 700)
compte2.afficherSolde()
