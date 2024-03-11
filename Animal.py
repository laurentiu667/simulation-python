import math
from abc import ABC, abstractmethod  # biblioteque pour les classes abstraites defini
from helper import Helper as hp
import random
import tkinter as tk
from PIL import Image, ImageTk

# classe et methode abstraite

class Animal(ABC):
    def __init__(self, canvas, vitesse):
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
        self.canvas = canvas
        self.vitesse = vitesse
        self.x = random.randint(0, 500)  # changer les valeurs de déplacement en fonction de la map
        self.y = random.randint(0, 500)
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
    def deplacer(self):
        if self.isMoving:
            dest_x = self.x + random.choice([-self.vitesse, self.vitesse])
            dest_y = self.y + random.randint(-self.vitesse, self.vitesse)
            self.canvas.move(self.rect, dest_x - self.x, dest_y - self.y)
            self.x, self.y = dest_x, dest_y
            self.canvas.update()

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
    def __init__(self, canvas):
        super().__init__(canvas, self.vitesse)
        self.image = Image.open("ours.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

        canvas = tk.Canvas()
        ours = Ours(canvas)
        ours.deplacer()

    def hibernation(self):
        pass

    def deplacer(self):
        super(Ours, self).deplacer()


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