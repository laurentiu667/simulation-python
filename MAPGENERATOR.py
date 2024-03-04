import random
import math
import tkinter as tk
import time

class Vue():
    def __init__(self, res, root):
        self.root = root
        self.width = res  #Resolution
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.width)

    def generate_square(self, size, array):
        square_size = self.width / size
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

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
                x1 += square_size
                x2 += square_size
                limit = round(size * square_size)
                if round(x1, 0) == limit:
                    y1 += square_size
                    y2 += square_size
                    x2 = square_size
                    x1 = 0

        self.canvas.pack()
        self.draw_biome_limitaion()

    def draw_biome_limitaion(self):
        limits = (self.width/3)
        for i in range(1, 3, 1):
            self.canvas.create_line(limits*i, 1, limits*i, self.width, fill="black")
        for i in range(1, 3, 1):
            self.canvas.create_line(1, limits*i, self.width, limits*i, fill="black")

        index = 0
        for i in range(0, 4, 1):
            for j in range(0, 4, 1):
                self.canvas.create_text(limits*i, limits*j, text="text", fill="white")
                index += 1

class Diamond_square:
    def __init__(self):
        self.heightmapWidth = 513  # 17, 33, 65, 129, 257, 513, 1025...   (best result for performance : 257)
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

class Seed():
    def __init__(self):
        self.diamond_square = None
        self.mapValide = False
        self.time = math.trunc(time.time())
        self.biomeOrder = []
        self.seed = self.get_seed()
        self.biomeDict = {1: "ForetFeuillu",
                          2: "ForetFeuillu",
                          3: "ForetBoreale",
                          4: "ForetBoreale",
                          5: "Prairies",
                          6: "Prairies",
                          7: "Marais",
                          8: "Marais",
                          9: "Toundra",
                          0: "Toundra"}

    def get_seed(self):
        random.seed(self.time)
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
        percentage = 0
        for i in range(0, self.diamond_square.heightmapWidth, 1):
            for j in range(0, self.diamond_square.heightmapWidth, 1):
                if(self.diamond_square.heightmap[i][j] > -1 and self.diamond_square.heightmap[i][j] < 50):
                    water += 1
        percentage = (water/total)*100

        if(percentage > 20 and percentage < 30):
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