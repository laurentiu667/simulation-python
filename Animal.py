import math
from abc import ABC, abstractmethod  # biblioteque pour les classes abstraites defini
from helper import Helper as hp
import random
import tkinter as tk


# classe et methode abstraite

# Attribus respectif chercher specificitÃ© de l'animal en question
class CarreRouge:
    def __init__(self, canvas, x, y, size):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(x, y, x + size, y + size, fill="red")
        self.x = x
        self.y = y
        self.size = size

    def deplacer(self, x, y):
        dx = x - self.x
        dy = y - self.y
        self.canvas.move(self.rect, dx, dy)
        self.x = x
        self.y = y


class Animal(ABC):
    def __init__(self):
        self.y1 = None
        self.x1 = None
        self.x2 = None
        self.y2 = None
        self.champDeVision = None
        self.faim = 100
        self.soif = 100
        self.vie = 100
        self.Vitesse = None
        self.energie = 100
        self.sexe = None
        self.isAlive = None
        self.IsSleeping = False
        self.isStarvings = False
        self.isFucking = False
        self.isRunning = False
        self.canFuck = [2]  # les 2 date entre
        self.dureDeVie = None
        self.age = None
        self.endurance = None
        self.tempsGestation = None
        self.diete = None
        self.social = None
        self.position = None
        self.canvas = self.canvas
        self.isMoving = True

    @abstractmethod
    def manger(self):
        self.energie += 2

    @abstractmethod
    def boire(self):
        self.soif += 2

    @abstractmethod
    def mourir(self):
        self.isAlive = False

    @abstractmethod
    def dormir(self):
        # PAS OBULIER DE METTRE SOI DANS LE TICK OU A UNE AUTRE PLACE: IsSleeping = False
        self.IsSleeping = True
        if self.IsSleeping == True:
            self.faim -= 1.67
            self.soif -= 1.67
            self.isMoving = False
            if self.energie < 100:
                self.energie += 1.67
            elif self.energie == 100:
                self.energie += 0
        else:
            self.isMoving = True
            self.IsSleeping = False

    @abstractmethod
    def deplacer(self, carre, step=1):
        if self.isMoving == True:
            start_x, start_y = carre.x, carre.y
            dest_x = random.randint(0, 300 - carre.size)
            dest_y = random.randint(0, 300 - carre.size)
            dx = dest_x - start_x
            dy = dest_y - start_y
            steps = max(abs(dx), abs(dy)) // step
            for _ in range(steps):
                carre.deplacer(start_x + dx * (_ + 1) // steps, start_y + dy * (_ + 1) // steps)
                carre.canvas.update()
                carre.canvas.after(2)
        else:
            pass

    @abstractmethod
    def repro(self):
        pass

    @abstractmethod
    def isStarving(self):
        self.faim -= 0.05
        if self.faim <= 70:
            self.isStarvings = True
            self.energie -= 0.005
            self.vie -= 0.005
            if self.vie == 0:
                self.isAlive = False

    @abstractmethod
    def calculerEndurance(self):
        if self.isMoving == True:
            if self.isRunning == True:
                self.endurance -= 6.68
                self.energie -= 3.34
                self.soif -= 5
                self.faim -= 1
            elif self.isRunning == False:
                self.soif -= 1
                self.faim -= 0.5
                self.endurance -= 3.34
                self.energie -= 1.67
        else:
            pass

    @abstractmethod
    def calculerDureDeVie(self):
        vieMoyen = 30
        marge_erreur = 15
        erreur = random.randint(-marge_erreur, marge_erreur)
        self.dureDeVie = vieMoyen - erreur
        print(self.dureDeVie)

    @abstractmethod
    def perceptionTemps(self):
        pass


class Ours(Animal):
    def __init__(self):
        super().__init__(self)

    def hibernation(self):
        pass


class Cerf(Animal):
    def __init__(self):
        super().__init__(self)

        # Attribus respectif


class Loup(Animal):
    def __init__(self):
        super().__init__(self)

    def meute(self):
        pass


class Raton_laveur(Animal):
    def __init__(self):
        super().__init__(self)

        # Attribus respectif


class Lynx(Animal):
    def __init__(self):
        super().__init__(self)

        # Attribus respectif


class Ecureuil(Animal):
    def __init__(self):
        super().__init__(self)

        # Attribus respectif


class Renard(Animal):
    def __init__(self):
        super().__init__(self)

        # Attribus respectif


class Achigan(Animal):
    def __init__(self):
        super().__init__(self)

        # Attribus respectif


class Castor(Animal):
    def __init__(self):
        super().__init__(self)

        # Attribus respectif


class Orignal(Animal):
    def __init__(self):
        super().__init__(self)

        # Attribus respectif


class Lievre(Animal):
    def __init__(self):
        super().__init__(self)

    # Attribus respectif