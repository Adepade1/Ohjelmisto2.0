class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self,nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print("Kirjan Tiedot")
        print(f"Nimi: {self.nimi}, kirjoittaja: {self.kirjoittaja}, sivuja: {self.sivumäärä}")
        return


ekakirja = Kirja("Aku Ankka","Aki Hyyppä",50)
tokakirja = Kirja("Hytti n:o 6","Rosa Liksom",200)

ekakirja.tulosta_tiedot()
tokakirja.tulosta_tiedot()





class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.

    def kiihdytä(self,muutos):

    def Kulhe(self,aika):


class Sähköauto(auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti)
        self.akkukapasiteetti = akkukapasiteetti


sähköauto1 = Sähköauto("ABC-15",180,52.5)
sähköauto1.nopeus = 95
sähköauto1.kulje(3)

#TODO: tulosta kuljettu matka