import math
from abc import ABC, abstractmethod  # biblioteque pour les classes abstraites defini
from helper import Helper as hp
import random
import tkinter as tk
from PIL import Image, ImageTk
import time
import Modele as m1

# classe et methode abstraite

class Animal(ABC):
    # canvas, vitesse, heightMap
    def __init__(self):
        self.modele = m1
        self.y1 = None
        self.x1 = None
        self.x2 = None
        self.y2 = None
        self.champDeVision = None
        self.cacher = False
        self.faim = 100
        self.soif = 70
        self.vie = 100
        self.Vitesse = None
        self.energie = 100
        self.sexe = None
        self.isAssoifee = None
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
        self.terrain = None
        self.dest_x = 0
        self.dest_y = 0
        # self.canvas = canvas
        # self.vitesse = vitesse
        self.x = random.randint(0, 800)  # changer les valeurs de déplacement en fonction de la map
        self.y = random.randint(0, 800)
        self.region = None  #Region dans la carte
        self.isMoving = True
        self.minute = 0
        self.nom = None
        
        #VARIABLE POUR LES MOTIVATION ET DEPLACEMENT DES ANIMAUX ET LEUR ACTION
        self.isHorny = False
        self.trouverFemme = False
        self.trouverBouffe = False
        self.proieTuer = False
        self.trouverEau = False
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
        self.faim -= 1.67
        self.soif -= 1.67
        self.isMoving = False
        if self.energie < 100:
            self.energie += 1.67
        elif self.energie == 100:
            self.energie += 0
            
    def reveil(self):
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
            
            while self.x != self.dest_x:
                self.x += vitesse
            
            while self.y != self.dest_y:
                self.y +=vitesse
            
            dest_x = self.x + random.uniform(-vitesse, vitesse)
            dest_y = self.y + random.uniform(-vitesse, vitesse)
            self.canvas.move(self.rect, dest_x - self.x, dest_y - self.y)
            self.calculerEndurance()
           
            self.x, self.y = dest_x, dest_y
            self.canvas.update()


    def check_map_eau(self):
        for i in range(len(self.terrain[0])):
            for v in range(len(self.terrain[0])):

                if(self.terrain[0][i][v] > -1 and self.terrain[0][i][v] < 50 ):
                    self.dest_x = i
                    self.dest_y = v
                    
    def check_position(self):
        ratio = 801 / len(self.terrain[0][0])

        pos_x = math.floor(self.x / ratio)
        pos_y = math.floor(self.y / ratio)

        while self.terrain[self.region - 1][pos_x][pos_y] < 50:
            self.x = random.randint(0, 801)  # changer les valeurs de déplacement en fonction de la map
            self.y = random.randint(0, 801)
            self.region = random.randint(1, 9)
            pos_x = math.floor(self.x / ratio)
            pos_y = math.floor(self.y / ratio)

       # if self.terrain[self.region-1][pos_x][pos_y] <= 50:
        #    print("BUG")
        #else:
           # print(self.x,self.y)

    def repro(self):
        if self.isFucking == True:
            pass

    def isStarving(self):
        self.faim -= 0.05
        if self.faim <= 70:
            self.isStarvings = True
            self.energie -= 0.005
            self.vie -= 0.005
            if self.vie == 0:
                self.isAlive = False
                
    def isAssoife(self):
        self.soif -= 10
        if self.soif <= 70:
            self.isAssoifee = True
            self.energie -= 0.005
            self.vie -= 0.005
            if self.isAssoifee:
                self.deplacementVersEau()
            if self.vie == 0:
                self.isAlive = False
                
    def isNotAssoife(self):
        if self.isAssoifee == False:
            self.soif += 0.5
            self.energie += 0.05
                
    def deplacementVersEau(self):
           if self.isAssoifee == True:
                self.check_map_eau()
                self.isNotAssoife()
       
            
    def calculerEndurance(self):
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

    def calculerDureDeVie(self):
        vieMoyen = 30
        marge_erreur = 15
        erreur = random.randint(-marge_erreur, marge_erreur)
        self.dureDeVie = vieMoyen - erreur

    def gererTick(self):
        pass

    def perceptionTemps(self):
        start_time = time.time()

        while True:
            current_time = time.time()#Timer().time() classe simgleton ou (si acces) evironnement.dateHeure.time() les 2 se valent
            minutes, secondes = divmod(current_time, 60)

            if minutes >= 4:
                minutes = 0

            if int(secondes) == 0:
                minutes += 1

            if int(secondes) >= 0 and int(secondes) <= 20:
                self.reveil()
                self.motivation()
                if self.isStarvings == True:
                    self.deplacer()
                    if self.trouverBouffe == True:
                        self.chasser
                        if self.proieTuer == True:
                            self.manger()
                            
                if self.isAssoife == True:
                    self.deplacer()
                    if self.trouverEau == True:
                        self.boire()

            elif int(secondes) > 20 and int(secondes) < 60:
                self.motivation()
                if self.isHorny == True:
                    self.deplacer()
                    if self.trouverFemme == True:
                        self.isFucking == True
                        self.repro()
            elif minutes == 1 and int(secondes) <= 20:
                self.motivation()
                if self.isStarvings == True:
                    self.deplacer()
                    if self.trouverBouffe == True:
                        self.chasser
                        if self.proieTuer == True:
                            self.manger()
                            
                if self.isAssoife == True:
                    self.deplacer()
                    if self.trouverEau == True:
                        self.boire()
            elif minutes == 1 and int(secondes) > 20 and int(secondes) < 60:
                self.motivation()
                if self.isHorny == True:
                    self.deplacer()
                    if self.trouverFemme == True:
                        self.isFucking == True
                        self.repro()
            elif minutes >= 2 and minutes <= 4:
                self.dormir()

    def chasser(self):
        pass

    def trouverFemelle(self):
        pass


class Ours(Animal):
    def __init__(self, index, map):
        super().__init__()
        self.nom = ("Ours" + index)
        self.terrain = map
        #self.check_map_eau()
        self.image = Image.open("zone_test/animaux_pillow/bear.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)
        #self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)
    def hibernation(self):
        pass

    def deplacer(self):
        super().deplacer(vitesse=5)


class Cerf(Animal):
    def __init__(self, index, map):
        super().__init__()
        self.nom = ("Cerf" + index)
        self.terrain = map
        self.image = Image.open("zone_test/animaux_pillow/cerf.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)
        #self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)


class Loup(Animal):
    def __init__(self, index, map):
        super().__init__()
        self.nom = ("Loup" + index)
        self.terrain = map
        self.image = Image.open("zone_test/animaux_pillow/loup.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)
        #self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)

    def meute(self):
        pass


class Raton_laveur(Animal):
    def __init__(self, index,map):
        super().__init__()
        self.nom = ("Raton" + index)
        self.terrain = map
        self.image = Image.open("Images_Végétaux\Végétaux (images, code)\Animaux\laveur2.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)
        #self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)


class Lynx(Animal):
    def __init__(self, index, map ):
        super().__init__()
        self.nom = ("Lynx" + index)
        self.terrain = map
        self.image = Image.open("zone_test/animaux_pillow/lynx.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)
        #self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)


class Ecureuil(Animal):
    def __init__(self, index, map):
        super().__init__()
        self.nom = ("Ecureille" + index)
        self.terrain = map
        self.image = Image.open("Images_Végétaux\Végétaux (images, code)\Animaux\ecureuil2.png")
        self.image = self.image.resize((25, 25))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)
        #self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)


class Renard(Animal):
    def __init__(self, index, map):
        super().__init__()
        self.nom = ("Renard" + index)
        self.terrain = map
        self.image = Image.open("zone_test/animaux_pillow/renard.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)
        #self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)


class Achigan(Animal):
    def __init__(self, index, map):
        super().__init__()
        self.nom = ("Achigan" + index)
        self.terrain = map
        self.image = Image.open("zone_test/animaux_pillow/poisson.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)
        #self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)


class Castor(Animal):
    def __init__(self, index, map):
        super().__init__()
        self.nom = ("Castor" + index)
        self.terrain = map
        self.image = Image.open("zone_test/animaux_pillow/castord.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)
        #self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)


class Orignal(Animal):
    def __init__(self, index, map):
        super().__init__()
        self.nom = ("Orignial" + index)
        self.terrain = map
        self.image = Image.open("zone_test/animaux_pillow/orignal.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)
        #self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)


class Lievre(Animal):
    def __init__(self, index, map):
        super().__init__()
        self.nom = ("Lievre" + index)
        self.terrain = map
        self.image = Image.open("zone_test/animaux_pillow/lapin.png")
        self.image = self.image.resize((50, 50))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)
        #self.rect = canvas.create_image(self.x, self.y, image=self.photo, anchor=tk.CENTER)

    def deplacer(self):
        super().deplacer(vitesse=5)