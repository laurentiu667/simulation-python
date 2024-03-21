#import time serait utile pour effecteuer des updates de l'envrionnement
from time import time
import Animal
import Vegetal
from helper import Helper as hp

from abc import ABC, abstractmethod
class Environnement:
    def __init__(self):
        self.biome = None
        self.saison = None
        self.temperature = None
        self.isPrecipitation = None
        self.chance_precipitations = None
        self.humidite = None
        self.isOrages = None
        self.isTornades = None
        self.isTempetes_tropicale = None
        self.isNuageux = None
        self.isSoleil = None
        self.testAnimaux = [Animal.Cerf, Animal.Castor]
        self.testVegetaux = [Vegetal.Sapin, Vegetal.Sapin]


    def CatastropheMeteorologique(self):
   


        def orages(self):
            pass

        def tornades(self):
            pass

        def tempeteTropicales(self):
            pass


class Biome:
    def __init__(self, name, orage, night,climate, average_temperature, precipitation, dominant_flora, dominant_fauna):
        self.name = name  # Nom du biome, par exemple "Forêt tropicale", "Toundra", etc.
        self.climate = climate  # Type de climat, par exemple "Tropical", "Aride", etc.
        self.average_temperature = average_temperature  # Température moyenne en degrés Celsius
        self.precipitation = precipitation  # Précipitations annuelles moyennes en mm
        self.dominant_flora = dominant_flora  # Les formes de vie végétales dominantes
        self.dominant_fauna = dominant_fauna
        self.orage = orage
        self.night = night


class Saison:
    def __init__(self, name, temperature, precipitation, humdite, dominant_flora, dominant_fauna):
        self.name = name  # Nom de la saison, par exemple "Hiver", "Mousson", etc.
        self.temperature = temperature  # Température moyenne en degrés Celsius
        self.precipitation = precipitation  # Précipitations moyennes en mm
        self.dominant_flora = dominant_flora  # Les formes de vie végétales dominantes
        self.dominant_fauna = dominant_fauna  # Les formes de vie animales dominantes
        self.humidite = humdite
        


class Ete(Saison, Environnement, Biome):
    def __init__(self):
        self.saison = Saison("Ete", 0, 0, "incounnu", "incounnu")
        self.biome = Biome("Ete", False, "incounnu", 0, 0, "incounnu", "incounnu")
    def comportement_estivale(self, temp, precip, humidite):
     
        if self.saison.temperature > 30:
            if self.saison.precipitation != 0: 
                for animal in self.testAnimaux:
                    animal.soif -= animal.soif * 0.15
                    animal.energie -= animal.energie * 0.05
                if self.saison.humidite > 50:
                    for vegetal in self.testVegetaux:
                        vegetal.humidite += 20
                else:
                    pass
            elif self.saison.precipitation > 0:  # Avec précipitation
                for animal in self.testAnimaux:
                    animal.soif -= animal.soif * 0.05
                for vegetal in self.testVegetaux:
                    vegetal.humidite += 0.15  
                if self.saison.humidite > 75:
                    for vegetal in self.testVegetaux:
                        vegetal.photosynthese += 10 
                else:
                    pass
            elif self.biome.orage:
                for animal in self.testAnimaux:
                    # doit trouver la cachette la plus proche
                    if animal.cacher is True:
                        # doit faire en sorte de se deplacer vers la cachete
                        pass
            elif self.saison.precipitation == 0 and self.biome.night:
                #Rentre dans la fonction seDeplacer de la classe Animaux
                # for animal in self.testAnimaux:
                #     animal.deplacer()
                # ???????
                for animal in self.testAnimaux:
                    animal


        
                
    

class Hiver(Saison):
    def __init__(self):
        self.saison = Saison("Hiver", 0, 0, "incounnu", "incounnu")

class Printemps(Saison):
    def __init__(self):
        self.saison = Saison("Printemps", 0, 0, "incounnu", "incounnu")

class Automne(Saison):
    def __init__(self):
        self.saison = Saison("Automne", 0, 0, "incounnu", "incounnu")


if  __name__ == "__main__":
    e = Environnement()
    e.CatastropheMeteorologique()


# la generation des animaux pourrait dependre du dominant fauna de la saison en cours et du biome
# en fonction des methodes propre au saison et aux biomes je rajouterais des sousclasse de saison et biomes