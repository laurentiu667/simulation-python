from abc import ABC
from Timer import Timer


class Saison(ABC):
    def __init__(self, temp, nom, impHum, leverDuSoleil, coucherDuSoleil, apogeeSolaire, precipitation):
        self.nom = nom
        self.tempSaisonniere = temp
        self.impacteHumidite = impHum
        self.leverDuSoleil = leverDuSoleil
        self.coucherDuSoleil = coucherDuSoleil
        self.apogeeSolaire = apogeeSolaire
        self.precipitation = precipitation

class Ete(Saison):
    mois =(6,7,8)
    def __init__(self):
        temperature = 15
        impacteHumidite = -7
        leverDuSoleil = [Timer.obtenirUneHeure(5),Timer.obtenirUneHeure(5,35)]
        coucherDuSoleil = [Timer.obtenirUneHeure(20,45),Timer.obtenirUneHeure(17,45)]
        apogeeSolaire = [Timer.obtenirUneHeure(12),Timer.obtenirUneHeure(13,15)]
        precipitation = 0.35
        super().__init__(temperature, 'été', impacteHumidite, leverDuSoleil, coucherDuSoleil, apogeeSolaire, precipitation)
    
        
        
class Hiver(Saison):
    mois = (12,1,2)
    def __init__(self):
        temperature = -15
        impacteHumidite = -2
        leverDuSoleil = [Timer.obtenirUneHeure(7,22),Timer.obtenirUneHeure(6,45)]
        coucherDuSoleil = [Timer.obtenirUneHeure(16),Timer.obtenirUneHeure(17,45)]
        apogeeSolaire = [Timer.obtenirUneHeure(11,45),Timer.obtenirUneHeure(12,30)]
        precipitation = 0.15
        super().__init__(temperature, 'hiver', impacteHumidite, leverDuSoleil, coucherDuSoleil, apogeeSolaire, precipitation)
        
class Printemps(Saison):
    mois = (3,4,5)
    def __init__(self):
        temperature = 5
        impacteHumidite = -4
        leverDuSoleil = [Timer.obtenirUneHeure(6),Timer.obtenirUneHeure(5)]
        coucherDuSoleil = [Timer.obtenirUneHeure(17,35),Timer.obtenirUneHeure(20,35)]
        apogeeSolaire = [Timer.obtenirUneHeure(12),Timer.obtenirUneHeure(13,20)]
        precipitation = 0.25
        super().__init__(temperature, 'printemps', impacteHumidite, leverDuSoleil, coucherDuSoleil, apogeeSolaire, precipitation)

class Automne(Saison):
    mois = (9,10,11)
    def __init__(self):
        temperature = 5
        impacteHumidite = -3
        leverDuSoleil = [Timer.obtenirUneHeure(6,15),Timer.obtenirUneHeure(7,15)]
        coucherDuSoleil = [Timer.obtenirUneHeure(17,30),Timer.obtenirUneHeure(16,15)]
        apogeeSolaire = [Timer.obtenirUneHeure(12,45),Timer.obtenirUneHeure(11,45)]
        precipitation = 0.25
        super().__init__(temperature, 'automne', impacteHumidite, leverDuSoleil, coucherDuSoleil, apogeeSolaire, precipitation)
        
    # def __init__(self, name, temperature, precipitation, humdite, dominant_flora, dominant_fauna):

    #     self.precipitation = precipitation
    #     self.dominant_flora = dominant_flora
    #     self.dominant_fauna = dominant_fauna

    
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
    