class Personne:
    def __init__(self, nom = "", age = 0):
        self.nom = nom
        self.age = age
        if nom == "":
            self.DemanderNom()
        print(f"Constructeur personne {self.nom}")

    def SePresenter(self):
        info_persone = "Bonjour, je m appelle " + self.nom
        if self.age == 0:
            print(info_persone)
        else:
            print(info_persone + ", j'ai " + str(self.age) + " ans.")

            if self.estMajeur():
                print("je suis majeur")
            else:
                print("je ne suis pas majeur")

    def estMajeur(self):
        return self.age >= 18 #sa revient au meme que se qu il y a en dessou
        #if self.age < 18:
        #    return False
        #else:
        #    return True

    def DemanderNom(self):
        self.nom = input("Votre nom:")

personne1 = Personne("Jean", 30)
personne2 = Personne("Paul", 15)
personne3 = Personne()
personne4 = Personne(age = 20)

personne1.SePresenter()
personne2.SePresenter()
personne3.SePresenter()
personne4.SePresenter()

#print("estMajeur1 : ", personne1.estMajeur())
#print("estMajeur2 : ", personne2.estMajeur())