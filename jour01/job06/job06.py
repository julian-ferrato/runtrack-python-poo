class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom


animal = Animal()

animal.nommer("Panthéon")

print("L'âge de l'animal", animal.age,"ans")

animal.vieillir()
print("L'âge de l'animal", animal.age,"ans")

print("Nom de l'animal :", animal.prenom)