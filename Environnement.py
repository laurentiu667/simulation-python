import statistics
import math
from Timer import Timer
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
        
        self.saison_frame = Frame(self.root, background="red")
        self.saison_frame.pack()
        self.saison_titre = Label(self.saison_frame, text="Saison :")  # Change here
        self.saison_titre.pack(side='left')
        self.saison_info = Label(self.saison_frame, text=self.env.saison)  # And here
        self.saison_info.pack(side='left')

        self.date_frame = Frame(self.root)
        self.date_frame.pack()
        self.date_titre = Label(self.date_frame, text="Date :")
        self.date_titre.pack(side='left')
        self.date_info = Label(self.date_frame, text=self.env.dateHeure.get_date())
        self.date_info.pack(side='left')

        self.heure_frame = Frame(self.root)
        self.heure_frame.pack()
        self.heure_titre = Label(self.heure_frame, text="Heure :")
        self.heure_titre.pack(side='left')
        self.heure_info = Label(self.heure_frame, text=self.env.dateHeure.date.time())
        self.heure_info.pack(side='left')

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
        
        self.soleil_frame = Frame(self.root)
        self.soleil_frame.pack()
        self.soleil_titre = Label(self.soleil_frame, text="Soleil :")
        self.soleil_titre.pack(side='left')
        self.soleil_info = Label(self.soleil_frame, text= self.env.soleil)
        self.soleil_info.pack(side='left')
        
        self.leveeDuSoleil_frame = Frame(self.root)
        self.leveeDuSoleil_frame.pack()
        self.leveeDuSoleil_titre = Label(self.leveeDuSoleil_frame, text="Heure du levée de Soleil :")
        self.leveeDuSoleil_titre.pack(side='left')
        self.leveeDuSoleil_info = Label(self.leveeDuSoleil_frame, text=self.env.dateHeure.get_time(self.env.leveeDuSoleil))
        self.leveeDuSoleil_info.pack(side='left')
        
        self.apogeeSolaire_frame = Frame(self.root)
        self.apogeeSolaire_frame.pack()
        self.apogeeSolaire_titre = Label(self.apogeeSolaire_frame, text="Apogée du Soleil :")
        self.apogeeSolaire_titre.pack(side='left')
        self.apogeeSolaire_info = Label(self.apogeeSolaire_frame, text=self.env.dateHeure.get_time(self.env.apogeeSolaire))
        self.apogeeSolaire_info.pack(side='left')
        
        self.coucheeDuSoleil_frame = Frame(self.root)
        self.coucheeDuSoleil_frame.pack()
        self.coucheeDuSoleil_titre = Label(self.coucheeDuSoleil_frame, text="Heure du couchée de Soleil :")
        self.coucheeDuSoleil_titre.pack(side='left')
        self.coucheeDuSoleil_info = Label(self.coucheeDuSoleil_frame, text=self.env.dateHeure.get_time(self.env.coucherDuSoleil))
        self.coucheeDuSoleil_info.pack(side='left')
        
        self.ensoleillementMax_frame = Frame(self.root)
        self.ensoleillementMax_frame.pack()
        self.ensoleillementMax_titre = Label(self.ensoleillementMax_frame, text="Ensoleillement Max :")
        self.ensoleillementMax_titre.pack(side='left')
        self.ensoleillementMax_info = Label(self.ensoleillementMax_frame, text=f"{self.env.ensoleillementMax*100}" + " %")
        self.ensoleillementMax_info.pack(side='left')
        
        self.ensoleillementActuel_frame = Frame(self.root)
        self.ensoleillementActuel_frame.pack()
        self.ensoleillementActuel_titre = Label(self.ensoleillementActuel_frame, text="Ensoleillement  Actuel : ")
        self.ensoleillementActuel_titre.pack(side='left')
        self.ensoleillementActuel_info = Label(self.ensoleillementActuel_frame, text=f"{self.env.ensoleillementActuel*100}" + " %")
        self.ensoleillementActuel_info.pack(side='left')
        
        

    def update(self):
        self.env.updateEnv()
        
        self.biome_info.config(text=self.env.biome)
        self.saison_info.config(text=self.env.saison)
        self.date_info.config(text=self.env.dateHeure.get_date())
        self.heure_info.config(text=self.env.dateHeure.date.time())
        self.temperature_info.config(text=self.env.temperatureActuel)
        self.humidite_info.config(text=f"{self.env.humiditeActuel*100}" + " %")
        self.ensoleillementMax_info.config(text=f"{self.env.ensoleillementMax*100}" + " %")
        self.ensoleillementActuel_info.config(text=f"{self.env.ensoleillementActuel*100}" + " %")
        self.leveeDuSoleil_info.config(text=self.env.dateHeure.get_time(self.env.leveeDuSoleil))
        self.coucheeDuSoleil_info.config(text=self.env.dateHeure.get_time(self.env.coucherDuSoleil))
        self.apogeeSolaire_info.config(text=self.env.dateHeure.get_time(self.env.apogeeSolaire))
        self.soleil_info.config(text= "Levée" if self.env.soleil else "Couchée")
        
        self.root.update()
        self.root.after(1000, self.update)


class Environnement:
    def __init__(self):
        self.tempDeBase = None
        self.temperatureActuel = None
        
        self.humiditeMoyenne = None
        self.humiditeActuel = None
        
        self.soleil = False
        self.ensoleillementMoyen = None
        self.ensoleillementActuel = None
        self.ensoleillementMax = None
        self.precipitationMoyenne = None
        self.impactEnsoleillement = None
        self.leveeDuSoleil = None
        self.coucherDuSoleil = None
        self.apogeeSolaire = None
        
        self.biome = PrairiesEtSavanes()
        self.saison = Ete()
        self.dateHeure = Timer(self) # definit init ici ou dans le modele
        self.statEnv()


    def statEnv(self):
        #selon stats moyenne de montreal
        self.tempDeBase = 6 #en degrés Celsius
        self.humiditeMoyenne = 0.73
        self.ensoleillementMoyen = 0.6
        self.precipitationMoyenne = 978 #en mm/an
        self.impactEnsoleillement = 5
        self.calculTemperature()
        
    def updateEnv(self):
        self.liaisonSaisonMois()
        self.calculTemperature()

    def ajuster_temps_soleil(self, temps_soleil):
        # ((difference tranche d'heure)/ nb jours dans la saison) * jours actuel
        #permet au lever et coucher du soleil de s'ajuster selon les jours durant la saison
        diffTrancheHeure = self.dateHeure.total_seconds(temps_soleil[1]) - self.dateHeure.total_seconds(temps_soleil[0])
        diffParNbjours = diffTrancheHeure / self.dateHeure.nombreDeJoursDeLaSaison()
        return self.dateHeure.addTime(temps_soleil[0], Timer.convertirSecondeEnDuree(diffParNbjours * self.dateHeure.date.day))

    def calculerEnsoleillement(self):
        
        self.ensoleillementMax = statistics.mean([self.ensoleillementMoyen, self.biome.ensoleillement])
        self.ensoleillementActuel = 0
        etatDuSoleil = None
        # si opti doit vrm etre faite ajuster soleil pour levee,couchee,apogee sera appeler une seule fois par jour
        self.leveeDuSoleil = self.ajuster_temps_soleil(self.saison.leverDuSoleil)
        self.coucherDuSoleil = self.ajuster_temps_soleil(self.saison.coucherDuSoleil)
        self.apogeeSolaire = self.ajuster_temps_soleil(self.saison.apogeeSolaire)
        
        #ajuste la position du soleil en fonctionde l'heure actuelle 
        if self.leveeDuSoleil <= self.dateHeure.date.time() < self.apogeeSolaire:
            totalHeure = self.dateHeure.total_seconds(self.apogeeSolaire) - self.dateHeure.total_seconds(self.leveeDuSoleil)
            heureCible = self.dateHeure.total_seconds(self.dateHeure.date.time()) - self.dateHeure.total_seconds(self.leveeDuSoleil)
            etatDuSoleil = (heureCible / totalHeure)
        elif  self.apogeeSolaire <= self.dateHeure.date.time() < self.coucherDuSoleil :
            totalHeure = self.dateHeure.total_seconds(self.coucherDuSoleil) - self.dateHeure.total_seconds(self.apogeeSolaire)
            heureCible = self.dateHeure.total_seconds(self.dateHeure.date.time()) - self.dateHeure.total_seconds(self.apogeeSolaire)
            etatDuSoleil = (heureCible / totalHeure)
        
            
        if etatDuSoleil is not None:
            if self.dateHeure.date.time() < self.apogeeSolaire:
                self.ensoleillementActuel = round(etatDuSoleil * self.ensoleillementMax,2)
            else:
                self.ensoleillementActuel = round(1 - (etatDuSoleil * self.ensoleillementMax),2)
        else:
            self.ensoleillementActuel = 0
        
        if self.ensoleillementActuel >  0:
            self.soleil = True
        elif self.ensoleillementActuel <= 0:
            self.soleil = False
            
        
    def caclculerPrecipitation(self):
        pass

    def calculerPhotosynthese(self):
        pass
     
        
    def calculerHumidite(self):
        self.humiditeActuel = statistics.mean([self.humiditeMoyenne, self.biome.humidite])
        
    def liaisonSaisonMois(self):
        mois = self.dateHeure.date.month 
        if(mois in Hiver.mois):
            self.saison = Hiver()
        elif(mois in Printemps.mois):
            self.saison = Printemps()
        elif(mois in Ete.mois):
            self.saison = Ete()
        elif(mois in Automne.mois):
            self.saison = Automne()
    
    def calculTemperature(self):
        self.calculerHumidite()
        self.calculerEnsoleillement()
        
        impactHumidite = self.humiditeActuel * statistics.mean([self.saison.impacteHumidite, self.biome.impacteHumidite])
        impactEnsoleillement = self.ensoleillementActuel * self.impactEnsoleillement

        self.temperatureActuel =  round(self.tempDeBase + self.saison.tempSaisonniere + self.biome.tempBiome + impactHumidite + impactEnsoleillement,2)


        
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

    
    
