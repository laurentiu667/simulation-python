#import time serait utile pour effecteuer des updates de l'envrionnement
from time import time
import Animal
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
        self.animal = Animal.Cerf()




    def CatastropheMeteorologique(self):
        print(self.animal.soif)


        def orages(self):
            pass

        def tornades(self):
            pass

        def tempeteTropicales(self):
            pass


class Biome:
    def __init__(self, name, climate, average_temperature, precipitation, dominant_flora, dominant_fauna):
        self.name = name  # Nom du biome, par exemple "Forêt tropicale", "Toundra", etc.
        self.climate = climate  # Type de climat, par exemple "Tropical", "Aride", etc.
        self.average_temperature = average_temperature  # Température moyenne en degrés Celsius
        self.precipitation = precipitation  # Précipitations annuelles moyennes en mm
        self.dominant_flora = dominant_flora  # Les formes de vie végétales dominantes
        self.dominant_fauna = dominant_fauna


class Saison:
    def __init__(self, name, temperature, precipitation, dominant_flora, dominant_fauna):
        self.name = name  # Nom de la saison, par exemple "Hiver", "Mousson", etc.
        self.temperature = temperature  # Température moyenne en degrés Celsius
        self.precipitation = precipitation  # Précipitations moyennes en mm
        self.dominant_flora = dominant_flora  # Les formes de vie végétales dominantes
        self.dominant_fauna = dominant_fauna  # Les formes de vie animales dominantes

class Hiver(Saison):
    def __init__(self):
        self.saison = Saison("Hiver", 0, 0, "incounnu", "incounnu")


class Printemps(Saison):
    def __init__(self):
        self.saison = Saison("Printemps", 0, 0, "incounnu", "incounnu")

class Ete(Saison):
    def __init__(self):
        self.saison = Saison("Ete", 0, 0, "incounnu", "incounnu")

class Automne(Saison):
    def __init__(self):
        self.saison = Saison("Automne", 0, 0, "incounnu", "incounnu")


if  __name__ == "__main__":
    e = Environnement()
    e.CatastropheMeteorologique()


# la generation des animaux pourrait dependre du dominant fauna de la saison en cours et du biome
# en fonction des methodes propre au saison et aux biomes je rajouterais des sousclasse de saison et biomes