from abc     import ABC, abstractmethod  # biblioteque pour les classes abstraites defini
import random
import time


class Vegetal(ABC):
    def __init__(self):
        self.fruits = []
        self.croissance = None
        self.capaciteFruit = None
        self.coefCroissance = None
        

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
    
    @abstractmethod   
    def ajoutFruit(self):
        None
    
    @abstractmethod
    def fruitMange(self):
        None
    
    @abstractmethod
    def croitre(self):
        None
        
    @abstractmethod
    def updateCapaciteFruit(self):
        None
        
class Plante(Vegetal):
    def __init__(self):
        super().__init__()
        self.capaciteFruit = 5
        self.croissance = True
        self.coefCroissance = random.uniform(1.005, 1.075)
        self.esperanceVie = random.randint(100, 120)
        self.age = 1
        
    def ajoutFruit(self):
        if (len(self.fruits) < self.capaciteFruit):
            fruit = PlanteFruit()
            self.fruits.append(fruit)
        
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
            
class Fruit(ABC):
    def __init__(self):
        self.energie = None
        
        
class PlanteFruit(Fruit):
    def __init__(self):
        super().__init__()
        self.energie = random.randint(10, 20)

   