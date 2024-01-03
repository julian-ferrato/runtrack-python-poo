class Operation:
    def __init__(self, nombre1=13, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print("Résultat de l'addition :", resultat)

operation_instance = Operation()

operation_instance.addition()
