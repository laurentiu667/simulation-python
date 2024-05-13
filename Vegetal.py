from abc import ABC, abstractmethod  # biblioteque pour les classes abstraites defini
import random
import time
import math
from PIL import Image, ImageTk



class Vegetal(ABC):
    def __init__(self, parent):
        self.parent = parent
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
        else:
            self.croissance = False
    
    def updateCapaciteFruit(self):
        facteur = 1+ self.age * random.uniform(0.1, 0.15)
        self.capaciteFruit = self.capaciteFruit * facteur
            
class Sapin(Vegetal):
    def __init__(self, index, map, parent):
        super().__init__(parent)
        self.nom = ("Sapin" + index)
        self.terrain = map
        if self.parent.env.saison.nom == "été":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/sapin.png")
        elif self.parent.env.saison.nom == "automne" or self.parent.env.saison.nom == "printemps":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/sapin-automne_printemps.png")
        elif self.parent.env.saison.nom == "hiver":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/sapin-hiver.png")
        self.image = self.image.resize((280, 280))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)

class Bleuet(Vegetal):
    def __init__(self, index, map, parent):
        super().__init__(parent)
        self.nom = ("Bleuet" + index)
        self.terrain = map
        if self.parent.env.saison.nom == "été":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/bleuet.png")
        elif self.parent.env.saison.nom == "automne":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/bleuet-automne.png")
        elif self.parent.env.saison.nom == "printemps":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/bleuet-printemps.png")
        elif self.parent.env.saison.nom == "hiver":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/bleuet-hiver.png")
        self.image = self.image.resize((60, 60))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)

class Bouleau(Vegetal):
    def __init__(self, index, map, parent):
        super().__init__(parent)
        self.nom = ("Bouleau" + index)
        self.terrain = map
        if self.parent.env.saison.nom == "été":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/bouleaujaune.png")
        elif self.parent.env.saison.nom == "automne":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/bouleaujaune-automne.png")
        elif self.parent.env.saison.nom == "printemps":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/bouleaujaune-printemps.png")
        elif self.parent.env.saison.nom == "hiver":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/bouleaujaune-hiver.png")
        self.image = self.image.resize((265, 265))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)
        
class Erable(Vegetal):
    def __init__(self, index, map, parent):
        super().__init__(parent)
        self.nom = ("Erable" + index)
        self.terrain = map
        if self.parent.env.saison.nom == "été":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/erable_de_sucre.png")
        elif self.parent.env.saison.nom == "automne":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/erable_de_sucre-automne.png")
        elif self.parent.env.saison.nom == "printemps":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/erable_de_sucre-printemps.png")
        elif self.parent.env.saison.nom == "hiver":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/erable_de_sucre-hiver.png")
        self.image = self.image.resize((265, 265))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)
        
class Pomier(Vegetal):
    def __init__(self, index, map, parent):
        super().__init__(parent)
        self.nom = ("Pomier" + index)
        self.terrain = map
        if self.parent.env.saison.nom == "été":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/pommiersauvage.png")
        elif self.parent.env.saison.nom == "automne":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/pommiersauvage-automne.png")
        elif self.parent.env.saison.nom == "printemps":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/pommiersauvage-printemps.png")
        elif self.parent.env.saison.nom == "hiver":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/pommiersauvage-hiver.png")
        self.image = self.image.resize((265, 265))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)

class Pissenlit(Vegetal):
    def __init__(self, index, map, parent):
        super().__init__(parent)
        self.nom = ("Pissenlit" + index)
        self.terrain = map
        if self.parent.env.saison.nom == "été":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/pissenlit.png")
        elif self.parent.env.saison.nom == "automne" or self.parent.env.saison.nom == "printemps" or self.parent.env.saison.nom == "hiver":
            self.image = Image.open("Images_Végétaux/Végétaux (images, code)/Végétaux/pissenlit-automne_hiver_printemps.png")
        self.image = self.image.resize((15, 15))  # checker la grosseur de l'image
        self.photo = ImageTk.PhotoImage(self.image)
        self.region = random.randint(1, 9)