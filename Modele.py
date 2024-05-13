from Environnement import Environnement
import tkinter as tk
import random
from Animal import *
from Vegetal import *


class Modele:
    def __init__(self, parent, map):
        self.parent = parent
        self.map = map
        self.environnement = None
        self.animaux = []
        self.vegetaux = []
        self.env = Environnement()
        self.animal = Animal()

    def boucler_simulation(self):
        self.env.updateEnv()
        self.parent.view.simulation()

        # ACTION ANIMAUX


        self.parent.view.simroot.after(20, self.boucler_simulation)

    # GENERE TOUT LES VEGETAUX AVEC : NOM DES VEGETAUX + INDEX
    def creer_vegetaux(self):
        if self.map.Sapin.get() > 0:
            for i in range(self.map.Sapin.get()):
                sapin = Sapin(str(i), self.map.submap.ALL, self)
                sapin.check_position()
                self.vegetaux.append(sapin)
        if self.map.Bleuet.get() > 0:
            for i in range(self.map.Bleuet.get()):
                bleuet = Bleuet(str(i), self.map.submap.ALL, self)
                bleuet.check_position()
                self.vegetaux.append(bleuet)
        if self.map.Bouleau.get() > 0:
            for i in range(self.map.Bouleau.get()):
                bouleau = Bouleau(str(i), self.map.submap.ALL, self)
                bouleau.check_position()
                self.vegetaux.append(bouleau)
        if self.map.Erable.get() > 0:
            for i in range(self.map.Erable.get()):
                erable = Erable(str(i), self.map.submap.ALL, self)
                erable.check_position()
                self.vegetaux.append(erable)
        if self.map.Pomier.get() > 0:
            for i in range(self.map.Pomier.get()):
                pomier = Pomier(str(i), self.map.submap.ALL, self)
                pomier.check_position()
                self.vegetaux.append(pomier)
        if self.map.Pissenlit.get() > 0:
            for i in range(self.map.Pissenlit.get()):
                pissenlit = Pissenlit(str(i), self.map.submap.ALL, self)
                pissenlit.check_position()
                self.vegetaux.append(pissenlit)
                
    # GENERE TOUT LES ANIMAUX AVEC : NOM DE L'ANIMAL + INDEX
    def creer_animaux(self):
        if self.map.Cerf.get() > 0:
            for i in range(self.map.Cerf.get()):
                cerf = Cerf(str(i), self.map.submap.ALL)
                cerf.check_position()
                self.animaux.append(cerf)

        if self.map.Loup.get() > 0:
            for i in range(self.map.Loup.get()):
                loup = Loup(str(i), self.map.submap.ALL)
                loup.check_position()
                self.animaux.append(loup)

        if self.map.Raton.get() > 0:
            for i in range(self.map.Raton.get()):
                raton_laveur = Raton_laveur(str(i), self.map.submap.ALL)
                raton_laveur.check_position()
                self.animaux.append(raton_laveur)

        if self.map.Lynx.get() > 0:
            for i in range(self.map.Lynx.get()):
                lynx = Lynx(str(i), self.map.submap.ALL)
                lynx.check_position()
                self.animaux.append(lynx)

        if self.map.Ecureille.get() > 0:
            for i in range(self.map.Ecureille.get()):
                ecureuil = Ecureuil(str(i), self.map.submap.ALL)
                ecureuil.check_position()
                self.animaux.append(ecureuil)

        if self.map.Renard.get() > 0:
            for i in range(self.map.Renard.get()):
                renard = Renard(str(i), self.map.submap.ALL)
                renard.check_position()
                self.animaux.append(renard)

        if self.map.Castor.get() > 0:
            for i in range(self.map.Castor.get()):
                castor = Castor(str(i), self.map.submap.ALL)
                castor.check_position()
                self.animaux.append(castor)

        if self.map.Orignial.get() > 0:
            for i in range(self.map.Orignial.get()):
                orignal = Orignal(str(i), self.map.submap.ALL)
                orignal.check_position()
                self.animaux.append(orignal)

        if self.map.Lievre.get() > 0:
            for i in range(self.map.Lievre.get()):
                lievre = Lievre(str(i), self.map.submap.ALL)
                lievre.check_position()
                self.animaux.append(lievre)

        if self.map.Ours.get() > 0:
            for i in range(self.map.Ours.get()):
                ours = Ours(str(i), self.map.submap.ALL)
                ours.check_position()
                self.animaux.append(ours)
       
    def actionAnimaux(self):
        for animal in self.animaux:
            animal.isAssoife()
               
                  
           
    def deplacer(self, i):
       # self.animal.isAssoife() # C'est ca qui fait tout chier pcq pas capable de faire check_map_eau
        x = random.randint(1, 4)
        if x == 1:         
            i.x -= 5
            i.y -= 5
        elif x == 2:
            i.x += 5
            i.y -= 5
        elif x == 3:
            i.x -= 5
            i.y += 5
        elif x == 4:
            i.x += 5
            i.y += 5