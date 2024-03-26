import random
from PIL import Image, ImageDraw

image = Image.new("RGBA", (400, 400), (255, 255, 255, 100))
draw = ImageDraw.Draw(image)

tronc = "saddlebrown"
feuille = "khaki"
boule = "white"

# Tronc plus haut et plus mince
draw.rectangle((180, 200, 220, 400), fill=tronc)

# Feuilles plus hautes et plus minces
draw.polygon([(150, 300), (250, 300), (200, 100)], fill=feuille)


image.save("sapinhiver_automne.png")
