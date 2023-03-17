#Tehtävä 1

class auto:
    def __init__(self, rekisteri, maxnopeus, nopeus, matka):
        self.rekisteri = rekisteri
        self.maxnopeus = maxnopeus
        self.noepus = nopeus
        self.matka = matka

auto = auto("ABC-123",142,0,0)

print(f"Auton rekisteri numero on {auto.rekisteri}, sen nopeus on {auto.noepus}/{auto.maxnopeus}"
      f" ja kuljettu matka on {auto.matka}km")



#Tehtävä 2

class auto:
    def __init__(self, rekisteri, maxnopeus, nopeus, matka):
        self.rekisteri = rekisteri
        self.maxnopeus = maxnopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihtyvyys(self,muutos):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.maxnopeus:
            self.nopeus = self.maxnopeus
        else:
            return

auto = auto("ABC-123",142,0,0)
auto.kiihtyvyys(30)
#print(f"Auton rekisteri numero on {auto.rekisteri}, sen nopeus on {auto.nopeus}/{auto.maxnopeus}"
#      f" ja kuljettu matka on {auto.matka}km")
auto.kiihtyvyys(70)
#print(f"Auton rekisteri numero on {auto.rekisteri}, sen nopeus on {auto.nopeus}/{auto.maxnopeus}"
#      f" ja kuljettu matka on {auto.matka}km")
auto.kiihtyvyys(50)
#print(f"Auton rekisteri numero on {auto.rekisteri}, sen nopeus on {auto.nopeus}/{auto.maxnopeus}"
#      f" ja kuljettu matka on {auto.matka}km")
auto.kiihtyvyys(-200)
print(f"Auton rekisteri numero on {auto.rekisteri}, sen nopeus on {auto.nopeus}/{auto.maxnopeus}"
      f" ja kuljettu matka on {auto.matka}km")



#Tehtävä 3

class auto:
    def __init__(self, rekisteri, maxnopeus, nopeus, matka):
        self.rekisteri = rekisteri
        self.maxnopeus = maxnopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihtyvyys(self,muutos):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.maxnopeus:
            self.nopeus = self.maxnopeus
        else:
            return

    def kulje(self,aika):
        self.matka += self.nopeus * aika

# auto = auto("ABC-123",142,60,0)
# auto.kulje(10)
# print(f"Auton rekisteri numero on {auto.rekisteri}, sen nopeus on {auto.nopeus}/{auto.maxnopeus}"
#      f" ja kuljettu matka on {auto.matka}km")



#Tehtävä 4

import random
class auto:
    def __init__(self, rekisteri, maxnopeus, nopeus, matka):
        self.rekisteri = rekisteri
        self.maxnopeus = maxnopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihtyvyys(self):
        muutos = random.randrange(-10, 15)
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.maxnopeus:
            self.nopeus = self.maxnopeus
        else:
            return

    def kulje(self,aika):
        self.matka += self.nopeus * aika


autot = []
for i in range(10):
    rekisteri = f"ABC-{i+1}"
    maxnopeus = random.randint(100,200)
    autot.append(auto(rekisteri,maxnopeus,0,0))



game = True

while game == True:
    for autoX in autot:
        autoX.kiihtyvyys()
        autoX.kulje(1)
        if autoX.matka >= 10000:
            game = False

if game == False:
    for autoX in autot:
        print(f"Auton {autoX.rekisteri} nopeus on {autoX.nopeus}/{autoX.maxnopeus} ja kuljettu matka on {autoX.matka}km")