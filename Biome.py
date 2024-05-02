from abc import ABC

class Biome(ABC):
    
    BIOMES_NAME = {0: "Forêts Boréales", 1: "Toundra", 2: "Rivières et Lacs", 3: "Montagnes et Plateaux", 4: "Prairies et Savanes"}

    
    def __init__(self, nom, temp, humidite, impHum, ensoleillementBiome, precipitation):
        self.nom = nom
        self.tempBiome = temp
        self.humidite = humidite
        self.impacteHumidite = impHum
        self.ensoleillement = ensoleillementBiome
        self.precipitation = precipitation
    
    def __str__(self) -> str:
        return self.nom

        
        # def __init__(self, name, orage, night,climate, average_temperature, precipitation, dominant_flora, dominant_fauna):
    #     self.climate = climate
    #     self.average_temperature = average_temperature
    #     self.precipitation = precipitation
    #     self.dominant_flora = dominant_flora
    #     self.dominant_fauna = dominant_fauna
    #     self.orage = orage
    #     self.night = night

class ForetsBoreales(Biome):
    def __init__(self):
        temperature = -5
        humidite = 0.7
        coefHumidité = -0.5
        ensoleillement = 0.4
        precipitaion = 0.7
        super().__init__('Forêts Boréales', temperature, humidite, coefHumidité, ensoleillement, precipitaion)

class Toundra(Biome):
    def __init__(self):
        temperature = -8
        humidite = 0.6
        coefHumidité = -0.2
        ensoleillement = 0.5
        precipitaion = 0.3
        super().__init__('Toundra', temperature, humidite, coefHumidité, ensoleillement,precipitaion)

class RivieresEtLacs(Biome):
    def __init__(self):
        temperature = 0
        humidite = 0.8
        coefHumidité = -0.3
        ensoleillement = 0.60
        precipitaion = 0.8
        super().__init__('Rivières et Lacs', temperature, humidite, coefHumidité, ensoleillement,precipitaion)

class MontagnesEtPlateaux(Biome):
    def __init__(self):
        temperature = -4
        humidite = 0.5
        coefHumidité = -0.6
        ensoleillement = 0.70
        precipitaion = 0.75
        super().__init__('Montagnes et Plateaux', temperature, humidite, coefHumidité, ensoleillement, precipitaion)

class PrairiesEtSavanes(Biome):
    def __init__(self):
        temperature = 2
        humidite = 0.5
        coefHumidité = -0.5
        ensoleillement = 0.8
        precipitaion = 0.5
        super().__init__('Prairies et Savanes', temperature, humidite, coefHumidité,ensoleillement, precipitaion)
        
BIOMES_CLASS = {Biome.BIOMES_NAME[0]: ForetsBoreales(), Biome.BIOMES_NAME[1]: Toundra(), Biome.BIOMES_NAME[2]: RivieresEtLacs(), Biome.BIOMES_NAME[3]: MontagnesEtPlateaux(), Biome.BIOMES_NAME[4]: PrairiesEtSavanes()}
