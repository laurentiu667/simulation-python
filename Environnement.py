#import time serait utile pour effecteuer des updates de l'envrionnement
from time import time
import Animal
import Vegetal
from helper import Helper as hp
from tkinter import *
import Time
from abc import ABC, abstractmethod
from Animal import Cerf, Castor
from Vegetal import Sapin

class Vu:
    def __init__(self):
        self.root = Tk()
        self.root.title("Environnement")
        self.canvas = Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        self.afficher()
        
        
        
    def afficher(self):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        taille_plante = 50
        x1 = (canvas_width - taille_plante) / 2
        y1 = (canvas_height - taille_plante) / 2
        x2 = x1 + taille_plante
        y2 = y1 + taille_plante

        self.canvas.create_text(x1, y1, text="Plante")

    def actualiser(self):
        self.root.mainloop()

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
        self.name = name
        self.climate = climate
        self.average_temperature = average_temperature
        self.precipitation = precipitation
        self.dominant_flora = dominant_flora
        self.dominant_fauna = dominant_fauna
        self.orage = orage
        self.night = night


class Saison:
    def __init__(self, name, temperature, precipitation, humdite, dominant_flora, dominant_fauna):
        self.name = name
        self.temperature = temperature
        self.precipitation = precipitation
        self.dominant_flora = dominant_flora
        self.dominant_fauna = dominant_fauna
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
            elif self.saison.precipitation > 0:
                for animal in self.testAnimaux:
                    animal.soif -= animal.soif * 0.05
                for vegetal in self.testVegetaux:
                    vegetal.humidite += 15  
                if self.saison.humidite > 75:
                    for vegetal in self.testVegetaux:
                        vegetal.photosynthese += 10 


if __name__ == "__main__":
    e = Environnement()
    vue = Vu()
    
    vue.actualiser()

    
    
