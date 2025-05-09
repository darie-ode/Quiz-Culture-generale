class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def gets_internship(self):
        self.internship = True


class Chair:
    def __init__(self, color):
        self.color = color


darie = Personne("darie", 70)
print(darie.nom)
print(darie.age)
darie.gets_internship()
print(darie.internship)
alexandre = Personne("alexandre", 4)
print(alexandre.nom)
print(alexandre.age)
