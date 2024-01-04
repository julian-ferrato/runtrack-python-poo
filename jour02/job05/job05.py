class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = False
        self._reservoir = 50

    def getMarque(self):
        return self._marque

    def setMarque(self, nouvelle_marque):
        self._marque = nouvelle_marque

    def getModele(self):
        return self._modele

    def setModele(self, nouveau_modele):
        self._modele = nouveau_modele

    def getAnnee(self):
        return self._annee

    def setAnnee(self, nouvelle_annee):
        self._annee = nouvelle_annee

    def getKilometrage(self):
        return self._kilometrage

    def setKilometrage(self, nouveau_kilometrage):
        self._kilometrage = nouveau_kilometrage

    def getEnMarche(self):
        return self._en_marche

    def demarrer(self):
        if self._verifier_plein():
            self._en_marche = True
            print("La voiture démarre.")
        else:
            print("La voiture ne peut pas démarrer, le réservoir est trop bas.")

    def arreter(self):
        self._en_marche = False
        print("La voiture s'arrête.")

    def _verifier_plein(self):
        return self._reservoir > 5

    def _get_reservoir(self):
        return self._reservoir

ma_voiture = Voiture("Toyota", "Corolla", 2020, 20000)

ma_voiture.demarrer()

print("La voiture est en marche :", ma_voiture.getEnMarche())

print("Niveau de réservoir :", ma_voiture._get_reservoir())

ma_voiture.arreter()
