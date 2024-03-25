import time
import statistics
import Timer
from tkinter import *
from abc import ABC, abstractmethod
from Biome import *
from Saison import *


class Vu:
    def __init__(self, environnement):
        self.env = environnement
        self.root = Tk()
        self.root.title("Environnement")
        self.canvas = Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        
    def afficher(self):
        
        self.biome_frame = Frame(self.root, background="red")
        self.biome_frame.pack()
        self.biome_titre = Label(self.biome_frame, text="Biomes :")
        self.biome_titre.pack(side='left')
        self.biome_info = Label(self.biome_frame, text=self.env.biome)
        self.biome_info.pack(side='left')

        self.date_frame = Frame(self.root)
        self.date_frame.pack()
        self.date_titre = Label(self.date_frame, text="Date :")
        self.date_titre.pack(side='left')
        self.date_info = Label(self.date_frame, text=self.env.date.get_date())
        self.date_info.pack(side='left')

        self.heure_frame = Frame(self.root)
        self.heure_frame.pack()
        self.heure_titre = Label(self.heure_frame, text="Heure :")
        self.heure_titre.pack(side='left')
        self.heure_info = Label(self.heure_frame, text=self.env.date.get_time())
        print(self.env.date.get_time())
        self.heure_info.pack(side='left')

        self.isSoleil_frame = Frame(self.root)
        self.isSoleil_frame.pack()
        self.isSoleil_titre = Label(self.isSoleil_frame, text="Soleil :")
        self.isSoleil_titre.pack(side='left')
        self.isSoleil_info = Label(self.isSoleil_frame, text=None)
        self.isSoleil_info.pack(side='left')

        self.temperature_frame = Frame(self.root)
        self.temperature_frame.pack()
        self.temperature_titre = Label(self.temperature_frame, text="Temperature :")
        self.temperature_titre.pack(side='left')
        self.temperature_info = Label(self.temperature_frame, text=self.env.temperatureActuel)
        self.temperature_info.pack(side='left')

        self.humidite_frame = Frame(self.root)
        self.humidite_frame.pack()
        self.humidite_titre = Label(self.humidite_frame, text="Humidite :")
        self.humidite_titre.pack(side='left')
        self.humidite_info = Label(self.humidite_frame, text=f"{self.env.humiditeActuel*100}" + " %")
        self.humidite_info.pack(side='left')

    def update(self):
        self.env.updateEnv()
        
        self.biome_info.config(text=self.env.biome)
        self.date_info.config(text=self.env.date.get_date())
        self.heure_info.config(text=self.env.date.get_time())
        self.temperature_info.config(text=self.env.temperatureActuel)
        self.humidite_info.config(text=f"{self.env.humiditeActuel*100}" + " %")
        
        self.root.update()
        self.root.after(1000, self.update)
        
    


class Environnement:
    def __init__(self):
        self.tempDeBase = None
        self.temperatureActuel = None
        self.humiditeMoyenne = None
        self.humiditeActuel = None
        self.ensoleillementMoyen = None
        self.precipitationMoyenne = None
        self.biome = PrairiesEtSavanes()
        self.saison = Ete()
        self.statEnv()
        self.date = Timer.Timer()
        
    def statEnv(self):
        #selon stats moyenne de montreal
        self.tempDeBase = 6 #en degrés Celsius
        self.humiditeMoyenne = 0.73
        self.ensoleillementMoyen = 0.6
        self.precipitationMoyenne = 978 #en mm/an
        self.calculTemperature()
        
    def updateEnv(self):
        self.calculTemperature()
        
        
    def calculerHumidite(self):
        self.humiditeActuel = statistics.mean([self.humiditeMoyenne, self.biome.humidité])
    
    def calculTemperature(self):
        self.calculerHumidite()
        impactHumidite = self.humiditeActuel * statistics.mean([self.saison.impacteHumidite, self.biome.impacteHumidite])
        
        self.temperatureActuel = int (self.tempDeBase + self.saison.tempSaisonniere + self.biome.tempBiome + impactHumidite)
            
        
        # #variable
        # self.biome = None
        # self.saison = None
        # self.temperature = None
        # self.isPrecipitation = None
        # self.chance_precipitations = None
        # self.humidite = None
        # self.isOrages = None
        # self.isTornades = None
        # self.isTempetes_tropicale = None
        # self.isNuageux = None
        # self.isSoleil = None
    
        # self.montreal_temperatures = {
        #     "Janvier": -9.3,  # en degrés Celsius
        #     "Février": -7.7,
        #     "Mars": -2.3,
        #     "Avril": 6.0,
        #     "Mai": 14.0,
        #     "Juin": 19.2,
        #     "Juillet": 22.3,
        #     "Août": 21.1,
        #     "Septembre": 16.0,
        #     "Octobre": 9.6,
        #     "Novembre": 2.5,
        #     "Décembre": -5.4,
        # }
        # self.testAnimaux = [Animal.Cerf, Animal.Castor]
        # self.testVegetaux = [Vegetal.Sapin, Vegetal.Sapin]

    # def CatastropheMeteorologique(self):
    #     def orages(self):
    #         pass

    #     def tornades(self):
    #         pass

    #     def tempeteTropicales(self):
    #         pass

if __name__ == "__main__":
    e = Environnement()
    vue = Vu(e)
        
    vue.afficher()
    vue.update()
    vue.root.mainloop()

    
    
