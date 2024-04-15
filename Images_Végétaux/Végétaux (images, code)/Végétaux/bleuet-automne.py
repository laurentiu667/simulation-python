import random
from PIL import Image, ImageDraw

# Créer une nouvelle image avec fond transparent
image = Image.new("RGBA", (400, 400), (255, 255, 255, 0))

# Initialiser l'objet ImageDraw pour dessiner sur l'image
draw = ImageDraw.Draw(image)

feuille = "#46753a"

# Définir les coordonnées du carré (coin supérieur gauche et coin inférieur droit)
x1, y1 = 100, 100
x2, y2 = 300, 300

# Dessiner le carré rempli en vert
draw.rectangle((x1, y1, x2, y2), fill=feuille)

# Enregistrer l'image
image.save("bleuet-automne.png")
