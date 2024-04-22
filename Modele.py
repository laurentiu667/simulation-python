from Environnement import Environnement
from Timer import Timer
import tkinter as tk
import random
import Animal
from Animal import Ours, Cerf, Loup, Raton_laveur, Lynx, Ecureuil, Renard, Achigan, Castor, Orignal, Lievre
from Vegetal import Sapin, Bleuet, Bouleau, Erable, Pissenlit, Pomier
import time


class Modele:
    def __init__(self, parent, map):
        self.parent = parent
        self.map = map
        self.environnement = None
        self.date = None
        self.animaux = []
        self.vegetaux = []
        self.env = Environnement()

    def boucler_simulation(self):
        self.env.updateEnv()
        print("boucle")
        self.parent.view.simulation()
        self.parent.view.simroot.after(500, self.boucler_simulation)
    
        # self.debuterTemps() #initialisation du temps seulement si c'est le model final

    def debuterTemps(self):
        self.date = Timer()  # class codé en sorte qu'il n'y ai qu'un seul repere temporelle

    def stopperTemps(self):
        self.date.thread.stop()  # stopper la mise a jour du repere temporelle pour pouvoir en creer un autre plus tard
        self.date.thread.join()  # Attendre que le thread se termine proprement

    # GENERE TOUT LES VEGETAUX AVEC : NOM DES VEGETAUX + INDEX
    def creer_vegetaux(self):
        if int(self.map.Sapin):
            for i in range(int(self.map.Sapin)):
                sapin = Sapin(str(i))
                self.vegetaux.append(sapin)
        if int(self.map.Bleuet):
            for i in range(int(self.map.Bleuet)):
                bleuet = Bleuet(str(i))
                self.vegetaux.append(bleuet)
        if int(self.map.Bouleau):
            for i in range(int(self.map.Bouleau)):
                bouleau = Bouleau(str(i))
                self.vegetaux.append(bouleau)
        if int(self.map.Erable):
            for i in range(int(self.map.Erable)):
                erable = Erable(str(i))
                self.vegetaux.append(erable)
        if int(self.map.Pomier):
            for i in range(int(self.map.Pomier)):
                pomier = Pomier(str(i))
                self.vegetaux.append(pomier)
        if int(self.map.Pissenlit):
            for i in range(int(self.map.Pissenlit)):
                pissenlit = Pissenlit(str(i))
                self.vegetaux.append(pissenlit)
    # GENERE TOUT LES ANIMAUX AVEC : NOM DE L'ANIMAL + INDEX
    def creer_animaux(self):
        if int(self.map.Cerf) > 0:
            for i in range(int(self.map.Cerf), self.map.submap.ALL):
                cerf = Cerf(str(i))
                self.animaux.append(cerf)

        if int(self.map.Loup) > 0:
            for i in range(int(self.map.Loup), self.map.submap.ALL):
                loup = Loup(str(i))
                self.animaux.append(loup)

        if int(self.map.Raton) > 0:
            for i in range(int(self.map.Raton)):
                raton_laveur = Raton_laveur(str(i), self.map.submap.ALL)
                self.animaux.append(raton_laveur)

        if int(self.map.Lynx) > 0:
            for i in range(int(self.map.Lynx)):
                lynx = Lynx(str(i), self.map.submap.ALL)
                self.animaux.append(lynx)

        if int(self.map.Ecureille) > 0:
            for i in range(int(self.map.Ecureille)):
                ecureuil = Ecureuil(str(i), self.map.submap.ALL)
                self.animaux.append(ecureuil)

        if int(self.map.Renard) > 0:
            for i in range(int(self.map.Renard)):
                renard = Renard(str(i), self.map.submap.ALL)
                self.animaux.append(renard)

        if int(self.map.Castor) > 0:
            for i in range(int(self.map.Castor)):
                castor = Castor(str(i), self.map.submap.ALL)
                self.animaux.append(castor)

        if int(self.map.Orignial) > 0:
            for i in range(int(self.map.Orignial)):
                orignal = Orignal(str(i), self.map.submap.ALL)
                self.animaux.append(orignal)

        if int(self.map.Lievre) > 0:
            for i in range(int(self.map.Lievre)):
                lievre = Lievre(str(i), self.map.submap.ALL)
                self.animaux.append(lievre)

        if int(self.map.Ours) > 0:
            for i in range(int(self.map.Ours)):
                ours = Ours(str(i), self.map.submap.ALL)
                self.animaux.append(ours)