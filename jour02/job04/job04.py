class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self._nom = nom
        self._prenom = prenom
        self._numero_etudiant = numero_etudiant
        self._credits = 0
        self._level = self._studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self._credits += credits
            self._level = self._studentEval()
        else:
            print("La valeur des crédits doit être supérieure à zéro.")

    def _studentEval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print(f"Informations de l'étudiant - Nom = {self._nom}, Prénom = {self._prenom}, "
              f"Identifiant = {self._numero_etudiant}, Niveau = {self._level}")

john_doe = Student("John", "Doe", 145)

john_doe.add_credits(30)
john_doe.add_credits(20)
john_doe.add_credits(25)

john_doe.studentInfo()
