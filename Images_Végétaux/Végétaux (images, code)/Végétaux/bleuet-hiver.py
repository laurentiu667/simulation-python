import random
from PIL import Image, ImageDraw

# Créer une nouvelle image avec fond transparent
image = Image.new("RGBA", (400, 400), (255, 255, 255, 0))

# Initialiser l'objet ImageDraw pour dessiner sur l'image
draw = ImageDraw.Draw(image)

feuille = "#46753a"
neige = "white"

# Définir les coordonnées du carré (coin supérieur gauche et coin inférieur droit)
x1, y1 = 100, 100
x2, y2 = 300, 300

# Dessiner le carré rempli en vert
draw.rectangle((x1, y1, x2, y2), fill=feuille)

# Définir la taille des boules de neige
taille_boule = 5

# Dessiner des boules de neige aléatoirement dans le carré
for _ in range(25):  # Dessiner 25 boules de neige
    # Générer des coordonnées aléatoires à l'intérieur du carré (en excluant une petite marge)
    neige_x = random.randint(x1 + taille_boule, x2 - taille_boule)
    neige_y = random.randint(y1 + taille_boule, y2 - taille_boule)
    # Dessiner un cercle bleu pour représenter un bleuet
    draw.ellipse((neige_x - taille_boule, neige_y - taille_boule, neige_x + taille_boule, neige_y + taille_boule), fill=neige)

# Enregistrer l'image
image.save("bleuet-hiver.png")
