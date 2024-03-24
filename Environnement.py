import time
import Timer
from tkinter import *
from abc import ABC, abstractmethod


class Vu:
    def __init__(self):
        self.root = Tk()
        self.root.title("Environnement")
        self.canvas = Canvas(self.root, width=500, height=500)
        self.canvas.pack()
    
        
    def afficher(self):
        
        biome_frame = Frame(self.root, background="red")
        biome_frame.pack()
        biome_titre = Label(biome_frame, text="Biomes :")
        biome_titre.pack(side='left')
        biome_info = Label(biome_frame, text="Temple")
        biome_info.pack(side='left')

        date_frame = Frame(self.root)
        date_frame.pack()
        date_titre = Label(date_frame, text="Date :")
        date_titre.pack(side='left')
        date_info = Label(date_frame, text="2024-04-22")
        date_info.pack(side='left')

        heure_frame = Frame(self.root)
        heure_frame.pack()
        heure_titre = Label(heure_frame, text="Heure :")
        heure_titre.pack(side='left')
        heure_info = Label(heure_frame, text="11:52")
        heure_info.pack(side='left')

        isSoleil_frame = Frame(self.root)
        isSoleil_frame.pack()
        isSoleil_titre = Label(isSoleil_frame, text="Soleil :")
        isSoleil_titre.pack(side='left')
        isSoleil_info = Label(isSoleil_frame, text="Nuageux")
        isSoleil_info.pack(side='left')

        temperature_frame = Frame(self.root)
        temperature_frame.pack()
        temperature_titre = Label(temperature_frame, text="Temperature :")
        temperature_titre.pack(side='left')
        temperature_info = Label(temperature_frame, text="23")
        temperature_info.pack(side='left')

        humidite_frame = Frame(self.root)
        humidite_frame.pack()
        humidite_titre = Label(humidite_frame, text="Humidite :")
        humidite_titre.pack(side='left')
        humidite_info = Label(humidite_frame, text="36%")
        humidite_info.pack(side='left')

        isOrage_frame = Frame(self.root)
        isOrage_frame.pack()
        isOrage_titre = Label(isOrage_frame, text="Orage :")
        isOrage_titre.pack(side='left')
        isOrage_info = Label(isOrage_frame, text="Il faut nuageux")
        isOrage_info.pack(side='left')

        isTornade_frame = Frame(self.root)
        isTornade_frame.pack()
        isTornade_titre = Label(isTornade_frame, text="Tornade :")
        isTornade_titre.pack(side='left')
        isTornade_info = Label(isTornade_frame, text="Une tornade en approche")
        isTornade_info.pack(side='left')

        isTempetes_tropicale_frame = Frame(self.root)
        isTempetes_tropicale_frame.pack()
        isTempetes_tropicale_titre = Label(isTempetes_tropicale_frame, text="Tempetes tropicale :")
        isTempetes_tropicale_titre.pack(side='left')
        isTempetes_tropicale_info = Label(isTempetes_tropicale_frame, text="Tempetes tropicale")
        isTempetes_tropicale_info.pack(side='left')

    def actualiser(self):
        self.root.mainloop()

class Environnement:
    def __init__(self):
        self.tempDeBase = None
        self.humiditeMoyenne = None
        self.ensoleillementMoyen = None
        self.precipitationMoyenne = None
        self.statEnv()
        
        
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
        
    def statEnv(self):
        #selon stats moyenne de montreal
        self.tempDeBase = 6 #en degrés Celsius
        self.humiditeMoyenne = 0.73
        self.ensoleillementMoyen = 0.6
        self.precipitationMoyenne = 978 #en mm/an

    # def CatastropheMeteorologique(self):
    #     def orages(self):
    #         pass

    #     def tornades(self):
    #         pass

    #     def tempeteTropicales(self):
    #         pass

if __name__ == "__main__":
    e = Environnement()
    vue = Vu()
    
    
    vue.afficher()
    vue.actualiser()

    
    
