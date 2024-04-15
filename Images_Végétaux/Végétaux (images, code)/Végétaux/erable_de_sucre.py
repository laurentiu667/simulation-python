import random
from PIL import Image, ImageDraw

image = Image.new("RGBA", (400, 400), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

tronc = "#633a28"
feuille = "#cfc931"
égratignure = "#ff8800"

# Tronc plus haut et plus mince
tronc_x1, tronc_y1 = 180, 200
tronc_x2, tronc_y2 = 220, 400
draw.rectangle((tronc_x1, tronc_y1, tronc_x2, tronc_y2), fill=tronc)

# Feuilles plus hautes et plus minces
feuilles_x1, feuilles_y1 = 150, 100
feuilles_x2, feuilles_y2 = 250, 300
draw.rectangle((feuilles_x1, feuilles_y1, feuilles_x2, feuilles_y2), fill=feuille)

# Ajouter des égratignures aléatoires sur les feuilles
for _ in range(10):  # Ajouter 5 égratignures
    x = random.randint(feuilles_x1, feuilles_x2)  # Coordonnée x aléatoire à l'intérieur des feuilles
    y1 = random.randint(feuilles_y1, feuilles_y2 - 10)  # Coordonnée y1 aléatoire à l'intérieur des feuilles
    y2 = random.randint(y1 + 10, feuilles_y2)  # Coordonnée y2 aléatoire à l'intérieur des feuilles
    draw.line((x, y1, x, y2), fill=égratignure, width=2)  # Dessiner une ligne verticale pour représenter une égratignure

image.save("erable_de_sucre.png")
