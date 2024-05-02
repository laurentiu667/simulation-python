import random
import math
from tkinter import font
import time
from Biome import Biome
class Vue():
    def __init__(self, root):
        self.root = root
        self.width = None

    def generate_square(self, size, array, biomes, res, genBiome):
        self.width = res
        square_size = res / size
        x1 = 0
        y1 = 0
        x2 = square_size
        y2 = square_size
        color = "green2"
        for i in range(size):
            row = array[i]
            for j in range(size):
                if -1 < row[j] < 25:
                    color = "blue"
                elif 25 < row[j] < 50:
                    color = "royalBlue"
                elif 50 < row[j] < 75:
                    color = "yellowGreen"
                elif 75 < row[j] < 100:
                    color = "green2"
                elif 100 < row[j] < 125:
                    color = "green"
                elif 125 < row[j] < 150:
                    color = "green"
                elif 150 < row[j] < 175:
                    color = "forestGreen"
                elif 175 < row[j] < 200:
                    color = "forestGreen"
                elif 200 < row[j] < 225:
                    color = "darkgreen"
                elif 225 < row[j] < 250:
                    color = "darkgreen"
                elif 250 < row[j]:
                    color = "gray80"

                self.root.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
                x1 += square_size
                x2 += square_size
                limit = round(size * square_size)
                if round(x1, 0) == limit:
                    y1 += square_size
                    y2 += square_size
                    x2 = square_size
                    x1 = 0

        if(genBiome):
            self.draw_biome_limitaion(biomes)
        self.root.pack()

    def generate_square_winter(self, size, array, biomes, res, genBiome):
        self.width = res
        square_size = res / size
        x1 = 0
        y1 = 0
        x2 = square_size
        y2 = square_size
        color = "green2"
        for i in range(size):
            row = array[i]
            for j in range(size):
                if -1 < row[j] < 25:
                    color = "lightSkyBlue"
                elif 25 < row[j] < 50:
                    color = "cornflowerBlue"
                elif 50 < row[j] < 75:
                    color = "palegreen"
                elif 75 < row[j] < 100:
                    color = "snow"
                elif 100 < row[j] < 125:
                    color = "lavender"
                elif 125 < row[j] < 150:
                    color = "lavender"
                elif 150 < row[j] < 175:
                    color = "lightblue"
                elif 175 < row[j] < 200:
                    color = "lightblue"
                elif 200 < row[j] < 225:
                    color = "lightSteelBlue"
                elif 225 < row[j] < 250:
                    color = "lightSteelBlue"
                elif 250 < row[j]:
                    color = "gray80"

                self.root.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
                x1 += square_size
                x2 += square_size
                limit = round(size * square_size)
                if round(x1, 0) == limit:
                    y1 += square_size
                    y2 += square_size
                    x2 = square_size
                    x1 = 0

        if(genBiome):
            self.draw_biome_limitaion(biomes)
        self.root.pack()

    def generate_square_autumn(self, size, array, biomes, res, genBiome):
        self.width = res
        square_size = res / size
        x1 = 0
        y1 = 0
        x2 = square_size
        y2 = square_size
        color = "green2"
        for i in range(size):
            row = array[i]
            for j in range(size):
                if -1 < row[j] < 25:
                    color = "cornflowerBlue"
                elif 25 < row[j] < 50:
                    color = "royalBlue"
                elif 50 < row[j] < 75:
                    color = "olive"
                elif 75 < row[j] < 100:
                    color = "yellowgreen"
                elif 100 < row[j] < 125:
                    color = "yellowgreen"
                elif 125 < row[j] < 150:
                    color = "darkolivegreen"
                elif 150 < row[j] < 175:
                    color = "darkolivegreen"
                elif 175 < row[j] < 200:
                    color = "darkolivegreen"
                elif 200 < row[j] < 225:
                    color = "darkgreen"
                elif 225 < row[j] < 250:
                    color = "darkgreen"
                elif 250 < row[j]:
                    color = "gray80"

                self.root.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
                x1 += square_size
                x2 += square_size
                limit = round(size * square_size)
                if round(x1, 0) == limit:
                    y1 += square_size
                    y2 += square_size
                    x2 = square_size
                    x1 = 0

        if(genBiome):
            self.draw_biome_limitaion(biomes)
        self.root.pack()

    def draw_biome_limitaion(self, biomes):
        limits = (self.width/3)
        for i in range(1, 3, 1):
            self.root.create_line(limits*i, 1, limits*i, self.width, fill="black")
        for i in range(1, 3, 1):
            self.root.create_line(1, limits*i, self.width, limits*i, fill="black")

        index = 0
        for i in range(0, 3, 1):
            for j in range(0, 3, 1):
                self.root.create_text(limits*i+ limits/2 , limits*j + 7, text=biomes[index], fill="black")
                index += 1


class Diamond_square:
    def __init__(self):
        self.heightmapWidth = 257  # 17, 33, 65, 129, 257, 513, 1025...   (best result for performance : 257)
        self.heightmap = [[0] * self.heightmapWidth for i in range(self.heightmapWidth)]
        self.rand = random.randint(45, 175)
        self.heightmap[0][0] = self.rand
        self.heightmap[self.heightmapWidth - 1][0] = self.rand
        self.heightmap[0][self.heightmapWidth - 1] = self.rand
        self.heightmap[self.heightmapWidth - 1][self.heightmapWidth - 1] = self.rand
        self.randomness = 150
        self.tileWidth = self.heightmapWidth - 1

    def create_heightMap(self):
        while self.tileWidth > 1:
            self.halfSide = math.floor(self.tileWidth / 2)

            for x in range(0, self.heightmapWidth - 1, self.tileWidth):
                for y in range(0, self.heightmapWidth - 1, self.tileWidth):
                    cornerSum = self.heightmap[x][y] + \
                                self.heightmap[x + self.tileWidth][y] + \
                                self.heightmap[x][y + self.tileWidth] + \
                                self.heightmap[x + self.tileWidth][y + self.tileWidth]

                    avg = cornerSum / 4
                    avg += random.randint(-self.randomness, self.randomness)

                    self.heightmap[x + self.halfSide][y + self.halfSide] = avg

            for x in range(0, self.heightmapWidth - 1, self.halfSide):
                for y in range((x + self.halfSide) % self.tileWidth, self.heightmapWidth - 1, self.tileWidth):
                    avg = self.heightmap[(x - self.halfSide + self.heightmapWidth - 1) % (self.heightmapWidth - 1)][y] + \
                          self.heightmap[(x + self.halfSide) % (self.heightmapWidth - 1)][y] + \
                          self.heightmap[x][(y + self.halfSide) % (self.heightmapWidth - 1)] + \
                          self.heightmap[x][(y - self.halfSide + self.heightmapWidth - 1) % (self.heightmapWidth - 1)]

                    avg /= 4.0
                    avg += random.randint(-self.randomness, self.randomness)
                    self.heightmap[x][y] = avg

                    if x == 0:
                        self.heightmap[self.heightmapWidth - 1][y] = avg
                    if y == 0:
                        self.heightmap[x][self.heightmapWidth - 1] = avg

            self.randomness = max(self.randomness // 2, 1)
            self.tileWidth //= 2


class Sub_Section_Generator():
    def __init__(self, res, heightmap):
        self.res = res                      #RESOLUTION CHOISI PAR L'UTILISATEUR
        self.originalMap = 257              #TAILLE DE LA CARTE ORIGINAL
        self.heighMap = heightmap           #HEIGHT MAP ORIGNINAL
        self.scalling = math.floor(self.originalMap * self.res)
        self.UPSCALEDMAP = [[0] * self.scalling for i in range(self.scalling)]

        self.length = math.floor(self.scalling/3)
        self.sect1 = [[0] * self.length for i in range(self.length)]
        self.sect2 = [[0] * self.length for i in range(self.length)]
        self.sect3 = [[0] * self.length for i in range(self.length)]
        self.sect4 = [[0] * self.length for i in range(self.length)]
        self.sect5 = [[0] * self.length for i in range(self.length)]
        self.sect6 = [[0] * self.length for i in range(self.length)]
        self.sect7 = [[0] * self.length for i in range(self.length)]
        self.sect8 = [[0] * self.length for i in range(self.length)]
        self.sect9 = [[0] * self.length for i in range(self.length)]

        self.ALL = [self.sect1, self.sect2, self.sect3,
                    self.sect4, self.sect5, self.sect6,
                    self.sect7, self.sect8, self.sect9]


    def create_whole_map(self):
        facteur = math.floor(self.scalling/self.originalMap)

        for i in range(self.originalMap):
            for j in range(self.originalMap):
                upsacled_i = i * facteur
                upsacled_j = j * facteur
                for x in range(facteur):
                    for y in range(facteur):
                        self.UPSCALEDMAP[upsacled_i + x][upsacled_j + y] = self.heighMap[i][j]

    def sub_divide(self):
        index = -1
        for x in range(3):
            for y in range(3):
                index += 1
                index2 = -1
                l1 = self.length * x
                l2 = self.length * y
                l3 = self.length * (x + 1)
                l4 = self.length * (y + 1)
                for i in range(l1, l3, 1):
                    index2 += 1
                    index3 = -1
                    for j in range(l2, l4, 1):
                        index3 += 1
                        self.ALL[index][index2][index3] = self.UPSCALEDMAP[i][j]

class Seed():
    def __init__(self, waterPerc):
        self.diamond_square = None
        self.mapValide = False
        self.biomeOrder = []
        self.WaterPerc = waterPerc
        self.seed = self.get_seed()
        self.biomeDict = {0: Biome.BIOMES_NAME[0], 
                          1: Biome.BIOMES_NAME[0],
                          2: Biome.BIOMES_NAME[0],
                          3: Biome.BIOMES_NAME[1],
                          4: Biome.BIOMES_NAME[1],
                          5: Biome.BIOMES_NAME[4],
                          6: Biome.BIOMES_NAME[4],
                          7: Biome.BIOMES_NAME[2],
                          8: Biome.BIOMES_NAME[2],
                          9: Biome.BIOMES_NAME[3]}

    def get_seed(self):
        random.seed(math.trunc(time.time()))
        seed = 0
        while (len(str(math.trunc(seed)))) != 10:
            seed = random.random()
            seed = seed * 10000000000
        return math.trunc(seed)

    def set_biomes(self):
        for i in range(1, 10, 1):
            x = int(str(self.seed)[i])
            self.biomeOrder.append(self.biomeDict[x])

    def check_water_percentage(self):
        total = self.diamond_square.heightmapWidth**2
        water = 0
        for i in range(0, self.diamond_square.heightmapWidth, 1):
            for j in range(0, self.diamond_square.heightmapWidth, 1):
                if(self.diamond_square.heightmap[i][j] > -1 and self.diamond_square.heightmap[i][j] < 50):
                    water += 1
        percentage = ((water/total)*100)

        if percentage < (self.WaterPerc + 5) and percentage > (self.WaterPerc - 5):
            return True
        else:
            return False

    def generate_map(self):
        self.get_seed()
        self.set_biomes()

        while(self.mapValide == False):
            self.diamond_square = Diamond_square()
            self.diamond_square.create_heightMap()
            self.mapValide = self.check_water_percentage()

        self.mapValide = False
        
