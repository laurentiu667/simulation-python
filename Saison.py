from abc import ABC
from Timer import Timer


class Saison(ABC):
    def __init__(self, temp, nom, impHum, leverDuSoleil, coucherDuSoleil, apogeeSolaire):
        self.nom = nom
        self.tempSaisonniere = temp
        self.impacteHumidite = impHum
        self.leverDuSoleil = leverDuSoleil
        self.coucherDuSoleil = coucherDuSoleil
        self.apogeeSolaire = apogeeSolaire

    def __str__(self):
        return self.nom
       



class Ete(Saison):
    mois =(6,7,8)
    def __init__(self):
        leverDuSoleil = [Timer.obtenirUneHeure(5),Timer.obtenirUneHeure(5,30)]
        coucherDuSoleil = [Timer.obtenirUneHeure(20,30),Timer.obtenirUneHeure(21)]
        apogeeSolaire = [Timer.obtenirUneHeure(12),Timer.obtenirUneHeure(13)]
        super().__init__(15, 'été', -7, leverDuSoleil, coucherDuSoleil, apogeeSolaire)
    
        
        
class Hiver(Saison):
    mois = (12,1,2)
    def __init__(self):
        leverDuSoleil = [Timer.obtenirUneHeure(7,15),Timer.obtenirUneHeure(7,30)]
        coucherDuSoleil = [Timer.obtenirUneHeure(16),Timer.obtenirUneHeure(17,30)]
        apogeeSolaire = [Timer.obtenirUneHeure(11,45),Timer.obtenirUneHeure(12,30)]
        super().__init__(-15, 'hiver', -2, leverDuSoleil, coucherDuSoleil, apogeeSolaire)
        
class Printemps(Saison):
    mois = (3,4,5)
    def __init__(self):
        leverDuSoleil = [Timer.obtenirUneHeure(6),Timer.obtenirUneHeure(7,15)]
        coucherDuSoleil = [Timer.obtenirUneHeure(17,30),Timer.obtenirUneHeure(20,30)]
        apogeeSolaire = [Timer.obtenirUneHeure(12,15),Timer.obtenirUneHeure(13,15)]
        super().__init__(5, 'printemps', -4, leverDuSoleil, coucherDuSoleil, apogeeSolaire)

class Automne(Saison):
    mois = (9,10,11)
    def __init__(self):
        leverDuSoleil = [Timer.obtenirUneHeure(6,30),Timer.obtenirUneHeure(7,30)]
        coucherDuSoleil = [Timer.obtenirUneHeure(16),Timer.obtenirUneHeure(17,30)]
        apogeeSolaire = [Timer.obtenirUneHeure(11,45),Timer.obtenirUneHeure(12,30)]
        super().__init__(5, 'automne', -3, leverDuSoleil, coucherDuSoleil, apogeeSolaire)
        
    # def __init__(self, name, temperature, precipitation, humdite, dominant_flora, dominant_fauna):
    #     self.name = name
    #     self.temperature = temperature
    #     self.precipitation = precipitation
    #     self.dominant_flora = dominant_flora
    #     self.dominant_fauna = dominant_fauna
    #     self.humidite = humdite
    
    # def __init__(self):
    #     self.saison = Saison("Ete", 0, 0, "incounnu", "incounnu")
    #     self.biome = Biome("Ete", False, "incounnu", 0, 0, "incounnu", "incounnu")

    # def comportement_estivale(self, temp, precip, humidite):
    #     if self.saison.temperature > 30:
    #         if self.saison.precipitation != 0: 
    #             for animal in self.testAnimaux:
    #                 animal.soif -= animal.soif * 0.15
    #                 animal.energie -= animal.energie * 0.05
    #             if self.saison.humidite > 50:
    #                 for vegetal in self.testVegetaux:
    #                     vegetal.humidite += 20
    #         elif self.saison.precipitation > 0:
    #             for animal in self.testAnimaux:
    #                 animal.soif -= animal.soif * 0.05
    #             for vegetal in self.testVegetaux:
    #                 vegetal.humidite += 15  
    #             if self.saison.humidite > 75:
    #                 for vegetal in self.testVegetaux:
    #                     vegetal.photosynthese += 10 
    