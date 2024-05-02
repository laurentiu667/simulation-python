import statistics
import time
from Timer import Timer
from tkinter import *
from abc import ABC, abstractmethod
from Biome import *
from Saison import *

#classe vu temporaire pour afficher les test sur l'environnement
class Vu:
    def __init__(self, environnement):
        self.env = environnement
        self.root = Tk()
        self.root.geometry("800x850")
        self.root.title("Environnement")
        self.frames = [[None]*3 for _ in range(4)]
        self.temperature_info = []
        self.humidite_info = []
        self.ensoleillementMax_info = []
        self.ensoleillementActuel_info = []

        for i in range(4):  # 4 lignes
          self.root.rowconfigure(i, weight=1)  # Ajoutez cette ligne
          for j in range(3):  # 3 colonnes
            self.root.columnconfigure(j, weight=1)  # Ajoutez cette ligne
            self.frames[i][j] = Frame(self.root, borderwidth=1, relief="solid")
            self.frames[i][j].grid(row=i, column=j, sticky="nsew")
        
        
    def afficher(self):
        y = 10
        Label(self.frames[0][1], text="Statistique Général ", bg="gray25", fg="white").place(x=45, y=y)
        y += 25
        Label(self.frames[0][1], text="Date :").place(x=0, y=y)
        self.date_info = Label(self.frames[0][1], text=self.env.dateHeure.get_date())
        self.date_info.place(x=60, y=y)
        y += 20
        Label(self.frames[0][1], text="Heure :").place(x=0, y=y)
        self.heure_info = Label(self.frames[0][1], text=self.env.dateHeure.date.time())
        self.heure_info.place(x=60, y=y)
        y += 20
        Label(self.frames[0][1], text="Saison :").place(x=0, y=y)
        self.saison_info = Label(self.frames[0][1], text=self.env.saison)
        self.saison_info.place(x=60, y=y)
        y += 20
        Label(self.frames[0][1], text="Soleil :").place(x=0, y=y)
        self.soleil_info = Label(self.frames[0][1], text="Levé" if self.env.soleil else "Couché")
        self.soleil_info.place(x=60, y=y)
        y += 20
        Label(self.frames[0][1], text="Heure du levée de Soleil :").place(x=0, y=y)
        self.leveeDuSoleil_info = Label(self.frames[0][1], text=self.env.dateHeure.get_time(self.env.leveeDuSoleil))
        self.leveeDuSoleil_info.place(x=170, y=y)
        y += 20
        Label(self.frames[0][1], text="Apogée du Soleil :").place(x=0, y=y)
        self.apogeeSolaire_info = Label(self.frames[0][1], text=self.env.dateHeure.get_time(self.env.apogeeSolaire))
        self.apogeeSolaire_info.place(x=170, y=y)
        y += 20
        Label(self.frames[0][1], text="Heure du couchée de Soleil :").place(x=0, y=y)
        self.coucheeDuSoleil_info = Label(self.frames[0][1], text=self.env.dateHeure.get_time(self.env.coucherDuSoleil))
        self.coucheeDuSoleil_info.place(x=170, y=y)
        
        n=0
        for i in range(1, 4): #self.root.grid_size()[1]
            for j in range(3):
                                    
                y = 10
                Label(self.frames[i][j], text=self.env.biomes[n].biome, bg="gray25", fg="white").place(x=45, y=y)
                y += 35
                Label(self.frames[i][j], text="Temperature :").place(x=0, y=y)
                self.temperature_info.append(Label(self.frames[i][j], text=self.env.biomes[n].temperatureActuel))
                self.temperature_info[-1].place(x=170, y=y)
                y += 25
                Label(self.frames[i][j], text="Humidite :").place(x=0, y=y)
                self.humidite_info.append(Label(self.frames[i][j], text=f"{self.env.biomes[n].humiditeActuel*100}" + " %"))
                self.humidite_info[-1].place(x=170, y=y)
                y += 25
                Label(self.frames[i][j], text="Ensoleillement Max :").place(x=0, y=y)
                self.ensoleillementMax_info.append(Label(self.frames[i][j], text=f"{self.env.biomes[n].ensoleillementMax*100}" + " %"))
                self.ensoleillementMax_info[-1].place(x=170, y=y)
                y += 25
                Label(self.frames[i][j], text="Ensoleillement  Actuel : ").place(x=0, y=y)
                self.ensoleillementActuel_info.append(Label(self.frames[i][j], text=f"{self.env.biomes[n].ensoleillementActuel*100}" + " %"))
                self.ensoleillementActuel_info[-1].place(x=170, y=y)
                n += 1

    def update(self):
        self.env.updateEnv() # peut etre placer dans la classe Timer peut etre
        
        
        self.saison_info.config(text=self.env.saison)
        self.date_info.config(text=self.env.dateHeure.get_date())
        self.heure_info.config(text=self.env.dateHeure.date.time())
        self.soleil_info.config(text= "Levée" if self.env.soleil else "Couchée")
        self.leveeDuSoleil_info.config(text=self.env.dateHeure.get_time(self.env.leveeDuSoleil))
        self.coucheeDuSoleil_info.config(text=self.env.dateHeure.get_time(self.env.coucherDuSoleil))
        self.apogeeSolaire_info.config(text=self.env.dateHeure.get_time(self.env.apogeeSolaire))
        
        for i in range(9):
            self.temperature_info[i].config(text=self.env.biomes[i].temperatureActuel)
            self.humidite_info[i].config(text=f"{self.env.biomes[i].humiditeActuel*100}" + " %")
            self.ensoleillementMax_info[i].config(text=f"{round(self.env.biomes[i].ensoleillementMax*100, 3)}" + " %")
            self.ensoleillementActuel_info[i].config(text=f"{round(self.env.biomes[i].ensoleillementActuel*100, 3)}" + " %")
        
        self.root.update()
        self.root.after(300, self.update)


class Environnement:
    def __init__(self):
        self.dateHeure = None 
        
        #general aux biomes
        self.tempDeBase = None
        self.humiditeMoyenne = None        
        self.ensoleillementMoyen = None
        self.precipitationMoyenne = None
        self.impactEnsoleillement = None
        
        self.soleil = False
        self.etatDuSoleil = None
        self.leveeDuSoleil = None
        self.coucherDuSoleil = None
        self.apogeeSolaire = None
        
        self.saison = None

        self.biomes = [] 

        self.statEnv()
        
        


    def statEnv(self):
        #selon stats moyenne de montreal
        self.tempDeBase = 6 #en degrés Celsius
        self.humiditeMoyenne = 0.73
        self.ensoleillementMoyen = 0.6
        self.precipitationMoyenne = 978 #en mm/an
        self.impactEnsoleillement = 5
        
    def baseValider(self,annee,mois,jours):#call dans vue
        Timer.reset_instance() # au cas ou une instance de timer est deja créer
        self.dateHeure = Timer(self,annee,mois,jours)
        self.liaisonSaisonMois()
        
    def assignerBiomes(self, biomeListe):
        for biome in biomeListe:
            self.biomes.append(self.Biotope(self,BIOMES_CLASS[biome]))
        self.updateEnv()
        
    def updateEnv(self):
        self.ajuster_tous_les_temps_soleil()  
        self.ajuster_EtatDuSoleil()
        for biome in self.biomes: biome.calculTemperature()
        
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
            
    def ajuster_temps_soleil(self, temps_soleil):
            # ((difference tranche d'heure)/ nb jours dans la saison) * jours actuel
            #permet au lever et coucher du soleil de s'ajuster selon les jours durant la saison
            diffTrancheHeure = self.dateHeure.total_seconds(temps_soleil[1]) - self.dateHeure.total_seconds(temps_soleil[0])
            diffParNbjours = diffTrancheHeure / self.dateHeure.nombreDeJoursDeLaSaison()
            return self.dateHeure.addTime(temps_soleil[0], Timer.convertirSecondeEnDuree(diffParNbjours * self.dateHeure.joursDepuisDebutSaison()))
    
    def ajuster_tous_les_temps_soleil(self):
        self.leveeDuSoleil = self.ajuster_temps_soleil(self.saison.leverDuSoleil)
        self.coucherDuSoleil = self.ajuster_temps_soleil(self.saison.coucherDuSoleil)
        self.apogeeSolaire = self.ajuster_temps_soleil(self.saison.apogeeSolaire)
        
    def ajuster_EtatDuSoleil(self):
        #ajuste la position du soleil en fonction de l'heure actuelle 
        #si l'heure actuelle est entre le lever et l'apogée du soleil
        if self.leveeDuSoleil <= self.dateHeure.date.time() < self.apogeeSolaire:
            totalHeure = self.dateHeure.total_seconds(self.apogeeSolaire) - self.dateHeure.total_seconds(self.leveeDuSoleil)
            heureCible = self.dateHeure.total_seconds(self.dateHeure.date.time()) - self.dateHeure.total_seconds(self.leveeDuSoleil)
            self.etatDuSoleil = (heureCible / totalHeure)
        #si l'heure actuelle est entre le coucher et l'apogée du soleil
        elif  self.apogeeSolaire <= self.dateHeure.date.time() < self.coucherDuSoleil :
            totalHeure = self.dateHeure.total_seconds(self.coucherDuSoleil) - self.dateHeure.total_seconds(self.apogeeSolaire)
            heureCible = self.dateHeure.total_seconds(self.dateHeure.date.time()) - self.dateHeure.total_seconds(self.apogeeSolaire)
            self.etatDuSoleil = (heureCible / totalHeure)
        else:
            self.etatDuSoleil = None
            
    def caclculerPrecipitation(self):
        pass

    def calculerPhotosynthese(self):
        pass  
    
    class Biotope():
        def __init__(self, env,biome):
            self.nom = biome.nom
            self.env = env
            self.biome = biome
            
            #specifique au biomes
            self.temperatureActuel = None
            self.humiditeActuel = None
            self.ensoleillementActuel = None
            self.ensoleillementMax = None
            
            
        def calculerHumidite(self):
            self.humiditeActuel = statistics.mean([self.env.humiditeMoyenne, self.biome.humidite])
            

        def calculerEnsoleillement(self):
            
            self.ensoleillementMax = statistics.mean([self.env.ensoleillementMoyen, self.biome.ensoleillement])
            self.ensoleillementActuel = 0
                
            if self.env.etatDuSoleil is not None:
                if self.env.dateHeure.date.time() < self.env.apogeeSolaire:
                    self.ensoleillementActuel = round(self.env.etatDuSoleil * self.ensoleillementMax,2)
                elif self.env.dateHeure.date.time() < self.env.coucherDuSoleil:    
                    self.ensoleillementActuel = round(self.ensoleillementMax - (self.env.etatDuSoleil * self.ensoleillementMax),2)
            else:
                self.ensoleillementActuel = 0
            
            if self.ensoleillementActuel >  0:
                self.soleil = True
            else:
                self.soleil = False
            
        def calculTemperature(self):
            self.calculerHumidite()
            self.calculerEnsoleillement()
            
            impactHumidite = self.humiditeActuel * statistics.mean([self.env.saison.impacteHumidite, self.biome.impacteHumidite])
            impactEnsoleillement = self.ensoleillementActuel * self.env.impactEnsoleillement

            self.temperatureActuel =  round(self.env.tempDeBase + self.env.saison.tempSaisonniere + self.biome.tempBiome + impactHumidite + impactEnsoleillement,2)
    
            
        def __str__(self) -> str:
            return self.nom

if __name__ == "__main__":
    e = Environnement()
    e.baseValider(2021,1,1)
    e.assignerBiomes(['Toundra', 'Forêts Boréales', 'Toundra', 'Prairies et Savanes', 'Prairies et Savanes', 'Forêts Boréales', 'Rivières et Lacs', 'Forêts Boréales', 'Rivières et Lacs'])
    vue = Vu(e)
    
    vue.afficher()
    
    e.dateHeure.Start_Time()
    vue.update()
    
    
    vue.root.mainloop()

    
    
