import random
from PIL import Image, ImageDraw

image = Image.new("RGBA", (400, 400), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

tronc = "#bbbbbb"
feuille = "#94c25a"
égratignure = "black"

# Tronc plus haut et plus mince
tronc_x1, tronc_y1 = 180, 200
tronc_x2, tronc_y2 = 220, 400
draw.rectangle((tronc_x1, tronc_y1, tronc_x2, tronc_y2), fill=tronc)

# Ajouter des égratignures aléatoires sur le tronc
for _ in range(5):  # Ajouter 5 égratignures
    x = random.randint(tronc_x1, tronc_x2)  # Coordonnée x aléatoire à l'intérieur du tronc
    y1 = random.randint(tronc_y1, tronc_y2 - 10)  # Coordonnée y1 aléatoire à l'intérieur du tronc
    y2 = random.randint(y1 + 10, tronc_y2)  # Coordonnée y2 aléatoire à l'intérieur du tronc
    draw.line((x, y1, x, y2), fill=égratignure, width=2)  # Dessiner une ligne verticale pour représenter une égratignure

# Feuilles plus hautes et plus minces
draw.rectangle((150, 100, 250, 300), fill=feuille)

image.save("bouleaujaune.png")
