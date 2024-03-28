from abc import ABC

class Biome(ABC):
    def __init__(self, nom, temp, humidite, impHum, ensoleillementBiome):
        self.nom = nom
        self.tempBiome = temp
        self.humidite = humidite
        self.impacteHumidite = impHum
        self.ensoleillement = ensoleillementBiome

        
        
        # def __init__(self, name, orage, night,climate, average_temperature, precipitation, dominant_flora, dominant_fauna):
    #     self.climate = climate
    #     self.average_temperature = average_temperature
    #     self.precipitation = precipitation
    #     self.dominant_flora = dominant_flora
    #     self.dominant_fauna = dominant_fauna
    #     self.orage = orage
    #     self.night = night
    

    def __str__(self):
        return self.nom

class ForetsBoreales(Biome):
    def __init__(self):
        super().__init__('Forêts Boréales', -5, 0.7, -0.05,0.4)

class Toundra(Biome):
    def __init__(self):
        super().__init__('Toundra', -8, 0.6, -0.02, 0.5)

class RivieresEtLacs(Biome):
    def __init__(self):
        super().__init__('Rivières et Lacs', 0, 0.8, -0.03, 0.60)

class MontagnesEtPlateaux(Biome):
    def __init__(self):
        super().__init__('Montagnes et Plateaux', -0.6, 0.5, -0.06, 0.70)

class PrairiesEtSavanes(Biome):
    def __init__(self):
        super().__init__('Prairies et Savanes', 2, 0.5, -0.05,0.8)