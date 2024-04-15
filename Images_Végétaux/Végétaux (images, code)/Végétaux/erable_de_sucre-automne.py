import random
from PIL import Image, ImageDraw

image = Image.new("RGBA", (400, 400), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

tronc = "#9f7563"
feuille = "#797856"

# Tronc plus haut et plus mince
tronc_x1, tronc_y1 = 180, 200
tronc_x2, tronc_y2 = 220, 400
draw.rectangle((tronc_x1, tronc_y1, tronc_x2, tronc_y2), fill=tronc)

# Feuilles plus hautes et plus minces
draw.rectangle((150, 100, 250, 300), fill=feuille)

image.save("erable_de_sucre-automne.png")
