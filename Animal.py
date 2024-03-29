import math
from abc import ABC, abstractmethod  # biblioteque pour les classes abstraites defini
from helper import Helper as hp
import random
import tkinter as tk
from PIL import Image, ImageTk
import datetime
import time


# classe et methode abstraite

class Animal(ABC):
    # canvas, vitesse, heightMap
    def __init__(self):
        self.y1 = None
        self.x1 = None
        self.x2 = None
        self.y2 = None
        self.champDeVision = None
        self.cacher = False
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
        # self.canvas = canvas
        # self.vitesse = vitesse
        self.x = random.randint(0, 500)  # changer les valeurs de déplacement en fonction de la map
        self.y = random.randint(0, 500)
        self.isMoving = True
        self.minute = 0
        # self.heightMap = heightMap  # Permet de savoir si il y a de l'eau, Recoit le heightmap dans MAPGENERATOR -> Sub_Section_Generator -> self.UpscaledMap

    def manger(self):
        self.energie += 2

    def boire(self):
        self.soif += 2

    def mourir(self):
        self.isAlive = False

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

    def motivation(self):
        rnd = random.Random()
        if self.faim <= 50:
            self.isStarvings = True
            return self.isStarvings
        elif self.soif <= 50:
            self.isAssoife = True
            return self.isAssoife
        elif rnd <= 0.25:
            self.isHorny = True
            return self.isHorny
        elif rnd > 0.25 and rnd <= 0.50:
            self.isStarvings = True
            return self.isStarvings
        elif rnd > 0.50 and rnd <= 0.75:
            self.isAssoife = True
            return self.isAssoife
        # motivation pour dormir

    def deplacer(self, vitesse):
        if self.isMoving:
            dest_x = self.x + random.uniform(-vitesse, vitesse)
            dest_y = self.y + random.uniform(-vitesse, vitesse)
            self.canvas.move(self.rect, dest_x - self.x, dest_y - self.y)
            self.x, self.y = dest_x, dest_y
            self.canvas.update()

    def repro(self):
        pass

    def isStarving(self):
        self.faim -= 0.05
        if self.faim <= 70:
            self.isStarvings = True
            self.energie -= 0.005
            self.vie -= 0.005
            if self.vie == 0:
                self.isAlive = False

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

    def calculerDureDeVie(self):
        vieMoyen = 30
        marge_erreur = 15
        erreur = random.randint(-marge_erreur, marge_erreur)
        self.dureDeVie = vieMoyen - erreur
        print(self.dureDeVie)

    def gererTick(self):
        pass

    def perceptionTemps(self):
        start_time = time.time()

        while True:
            current_time = time.time() - start_time
            minutes, secondes = divmod(current_time, 60)

            print("Minutes :", int(minutes))
            print("Secondes :", int(secondes))

            if minutes >= 4:
                minutes = 0

            if int(secondes) == 0:
                minutes += 1

            if int(secondes) >= 0 and int(secondes) <= 20:

                self.isStarving

                # deplacer(self);
                # chasser
                # manger
                # boire

            elif int(secondes) > 20 and int(secondes) < 60:
                pass
                # deplacer(self);
                # reproduction
                # trouver femme
            elif minutes == 1 and int(secondes) <= 20:
                pass
                # deplacer(self);
                # chasser
                # manger
                # boire
            elif minutes == 1 and int(secondes) > 20 and int(secondes) < 60:
                pass
                # deplacer(self);
                # reproduction
                # trouver femme
            elif minutes >= 2 and minutes <= 4:
                pass
                # dort

    def chasser(self):
        pass


class Ours(Animal):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.image = Image.open("zone_test/animaux_pillow/bear.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def hibernation(self):
        pass

    def deplacer(self):
        super().deplacer(vitesse=5)


class Cerf(Animal):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.image = Image.open("zone_test/animaux_pillow/cerf.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)


class Loup(Animal):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.image = Image.open("zone_test/animaux_pillow/loup.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)

    def meute(self):
        pass


class Raton_laveur(Animal):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.image = Image.open("zone_test/animaux_pillow/laveur.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)


class Lynx(Animal):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.image = Image.open("zone_test/animaux_pillow/lynx.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)


class Ecureuil(Animal):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.image = Image.open("zone_test/animaux_pillow/ecureuil.png")
        self.image = self.image.resize((25, 25))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)


class Renard(Animal):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.image = Image.open("zone_test/animaux_pillow/renard.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)


class Achigan(Animal):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.image = Image.open("zone_test/animaux_pillow/poisson.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)


class Castor(Animal):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.image = Image.open("zone_test/animaux_pillow/castord.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)


class Orignal(Animal):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.image = Image.open("zone_test/animaux_pillow/orignal.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)


class Lievre(Animal):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.image = Image.open("zone_test/animaux_pillow/lapin.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)