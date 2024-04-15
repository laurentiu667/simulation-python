import random
from PIL import Image, ImageDraw

# Créer une nouvelle image avec fond transparent
image = Image.new("RGBA", (400, 400), (255, 255, 255, 0))

# Initialiser l'objet ImageDraw pour dessiner sur l'image
draw = ImageDraw.Draw(image)

feuille = "#46753a"
bleuet = "#1844e4"

# Définir les coordonnées du carré (coin supérieur gauche et coin inférieur droit)
x1, y1 = 100, 100
x2, y2 = 300, 300

# Dessiner le carré rempli en vert
draw.rectangle((x1, y1, x2, y2), fill=feuille)

# Définir la taille des bleuets
taille_bleuet = 5

# Dessiner des bleuets bleus aléatoirement dans le carré
for _ in range(25):  # Dessiner 25 bleuets
    # Générer des coordonnées aléatoires à l'intérieur du carré (en excluant une petite marge)
    bleuet_x = random.randint(x1 + taille_bleuet, x2 - taille_bleuet)
    bleuet_y = random.randint(y1 + taille_bleuet, y2 - taille_bleuet)
    # Dessiner un cercle bleu pour représenter un bleuet
    draw.ellipse((bleuet_x - taille_bleuet, bleuet_y - taille_bleuet, bleuet_x + taille_bleuet, bleuet_y + taille_bleuet), fill=bleuet)

# Enregistrer l'image
image.save("bleuet.png")
