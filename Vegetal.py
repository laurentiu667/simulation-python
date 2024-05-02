from abc import ABC, abstractmethod  # biblioteque pour les classes abstraites defini
import random
import time
import math
from PIL import Image, ImageTk



class Vegetal(ABC):
    def __init__(self):
        self.fruits = []
        self.croissance = None
        self.capaciteFruit = None
        self.coefCroissance = None
        self.humidite = 0
        self.photosynthese  = 0
        self.nom = None
        self.region = None
        self.terrain = None
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 800)

    def perceptionTemps():
        starttime = time.time()

        while True:
            currenttime = time.time() - starttime
            heures, reste = divmod(currenttime, 3600)
            minutes, secondes = divmod(reste, 60)

            time.sleep(1)
            print("Minutes :", int(minutes))
            print("Secondes :", int(secondes))

            if minutes >= 4:
                minutes = 0

            if int(secondes) == 0:
                minutes += 1

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

        if self.terrain[self.region - 1][pos_x][pos_y] <= 50:
            print("BUG")
        else:
            print(self.x, self.y)
   
    def ajoutFruit(self):
        None
    
   
    def fruitMange(self):
        None
    
  
    def croitre(self):
        None
 
    def updateCapaciteFruit(self):
        None
        
class PlanteComestible(Vegetal):
    def __init__(self):
        super().__init__()
        self.capaciteFruit = 5
        self.croissance = True
        self.coefCroissance = random.uniform(1.005, 1.075)
        self.esperanceVie = random.randint(100, 120)
        self.age = 1
        
    # def ajoutFruit(self):
    #     if (len(self.fruits) < self.capaciteFruit):
    #         fruit = PlanteFruit()
    #         self.fruits.append(fruit)
        
    def fruitMange(self):
        if len(self.fruits) > 0:
            self.fruits.pop()

    def croitre(self):
        if self.age < self.esperanceVie:
            self.age *= self.coefCroissance
            print(self.age)
        else:
            self.croissance = False
            print(self.age)
    
    def updateCapaciteFruit(self):
        facteur = 1+ self.age * random.uniform(0.1, 0.15)
        self.capaciteFruit = self.capaciteFruit * facteur
            
class Sapin(Vegetal):
    def __init__(self, index, map):
        super().__init__()
        self.nom = ("Sapin" + index)
        self.terrain = map
        self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/sapin.png")
        self.image = self.image.resize((280, 280))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)

class Bleuet(Vegetal):
    def __init__(self, index, map):
        super().__init__()
        self.nom = ("Bleuet" + index)
        self.terrain = map
        self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/bleuet.png")
        self.image = self.image.resize((60, 60))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)

class Bouleau(Vegetal):
    def __init__(self, index, map):
        super().__init__()
        self.nom = ("Bouleau" + index)
        self.terrain = map
        self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/bouleaujaune.png")
        self.image = self.image.resize((265, 265))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)
        
class Erable(Vegetal):
    def __init__(self, index, map):
        super().__init__()
        self.nom = ("Erable" + index)
        self.terrain = map
        self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/erable_de_sucre.png")
        self.image = self.image.resize((265, 265))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)
        
class Pomier(Vegetal):
    def __init__(self, index, map):
        super().__init__()
        self.nom = ("Pomier" + index)
        self.terrain = map
        self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/pommiersauvage.png")
        self.image = self.image.resize((265, 265))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)

class Pissenlit(Vegetal):
    def __init__(self, index, map):
        super().__init__()
        self.nom = ("Pissenlit" + index)
        self.terrain = map
        self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/pissenlit.png")
        self.image = self.image.resize((15, 15))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)