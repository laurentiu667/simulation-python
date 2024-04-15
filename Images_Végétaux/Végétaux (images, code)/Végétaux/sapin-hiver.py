from PIL import Image, ImageDraw
import random

# Créer une nouvelle image avec fond transparent
image = Image.new("RGBA", (400, 400), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Couleur du tronc et du sapin
tronc = "#9f7563"
sapin = "#9bba9e"
neige = "white"  # Couleur des boules de neige

# Coordonnées du tronc
tronc_x1, tronc_y1 = 180, 300
tronc_x2, tronc_y2 = 220, 400

# Coordonnées du triangle pour le sapin
sapin_x1, sapin_y1 = 150, 300
sapin_x2, sapin_y2 = 200, 100
sapin_x3, sapin_y3 = 250, 300

# Dessiner le tronc
draw.rectangle((tronc_x1, tronc_y1, tronc_x2, tronc_y2), fill=tronc)

# Dessiner le triangle pour le sapin
draw.polygon([(sapin_x1, sapin_y1), (sapin_x2, sapin_y2), (sapin_x3, sapin_y3)], fill=sapin)

# Coordonnées des boules de neige (au hasard sur la surface du sapin)
random.seed(42)  # Pour obtenir des résultats reproductibles
for _ in range(20):  # Ajouter 20 boules de neige
    x = random.randint(sapin_x1, sapin_x3)
    y = random.randint(sapin_y2, sapin_y1)  # Sur la partie supérieure du sapin
    # Vérifier si les coordonnées de la boule de neige sont à l'intérieur du triangle
    if (sapin_x2 - sapin_x1) * (y - sapin_y1) >= (sapin_y2 - sapin_y1) * (x - sapin_x1) and \
       (sapin_x3 - sapin_x2) * (y - sapin_y2) >= (sapin_y3 - sapin_y2) * (x - sapin_x2) and \
       (sapin_x1 - sapin_x3) * (y - sapin_y3) >= (sapin_y1 - sapin_y3) * (x - sapin_x3):
        draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=neige)  # Dessiner une boule de neige

# Enregistrer l'image
image.save("sapin-hiver.png")
