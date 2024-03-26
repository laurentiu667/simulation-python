import Environnement
from Timer import Timer
import tkinter as tk
import random
import Animal
from Animal import Ours, Cerf, Loup, Raton_laveur, Lynx, Ecureuil, Renard, Achigan, Castor, Orignal, Lievre
import time


class Modele:
    def __init__(self, parent, map):
        self.parent = parent
        self.map = map
        self.environnement = None
        self.date = None
        self.animaux = []

        # self.debuterTemps() #initialisation du temps seulement si c'est le model final

    def debuterTemps(self):
        self.date = Timer()  # class codé en sorte qu'il n'y ai qu'un seul repere temporelle

    def stopperTemps(self):
        self.date.thread.stop()  # stopper la mise a jour du repere temporelle pour pouvoir en creer un autre plus tard
        self.date.thread.join()  # Attendre que le thread se termine proprement

    def creer_animaux(self, canvas):

        cerf = Cerf(canvas)
        self.animaux.append(cerf)

        loup = Loup(canvas)
        self.animaux.append(loup)

        raton_laveur = Raton_laveur(canvas)
        self.animaux.append(raton_laveur)

        lynx = Lynx(canvas)
        self.animaux.append(lynx)

        ecureuil = Ecureuil(canvas)
        self.animaux.append(ecureuil)

        renard = Renard(canvas)
        self.animaux.append(renard)

        achigan = Achigan(canvas)
        self.animaux.append(achigan)

        castor = Castor(canvas)
        self.animaux.append(castor)

        orignal = Orignal(canvas)
        self.animaux.append(orignal)

        lievre = Lievre(canvas)
        self.animaux.append(lievre)

        ours = Ours(canvas)
        self.animaux.append(ours)

    def deplacement_animaux(self):
        while True:
            for animal in self.animaux:
                animal.deplacer()