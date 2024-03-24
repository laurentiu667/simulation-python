from abc import ABC

class Biome(ABC):
    def __init__(self, nom, temp, ensoleillement, precipitation, humidité):
        self.nom = nom
        self.tempBiome = temp
        self.ensoleillement = ensoleillement
        self.precipitation = precipitation
        self.humidité = humidité
        
        
        # def __init__(self, name, orage, night,climate, average_temperature, precipitation, dominant_flora, dominant_fauna):
    #     self.name = name
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
        super().__init__('Forêts Boréales', -5, 0.4, 0.7, 0.7)

class Toundra(Biome):
    def __init__(self):
        super().__init__('Toundra', -8, 0.5, 0.3, 0.6)

class MilieuxHumides(Biome):
    def __init__(self):
        super().__init__('Milieux Humides', -1, 0.5, 0.9, 0.9)

class RivieresEtLacs(Biome):
    def __init__(self):
        super().__init__('Rivières et Lacs', 0, 0.6, 0.8, 0.8)

class MontagnesEtPlateaux(Biome):
    def __init__(self):
        super().__init__('Montagnes et Plateaux', -0.6, 0.7, 0.6, 0.5)

class PrairiesEtSavanes(Biome):
    def __init__(self):
        super().__init__('Prairies et Savanes', 2, 0.8, 0.4, 0.5)