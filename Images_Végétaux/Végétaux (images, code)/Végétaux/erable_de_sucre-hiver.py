import random
from PIL import Image, ImageDraw

image = Image.new("RGBA", (400, 400), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

tronc = "#a27663"
feuille = "#d0ca2b"
neige = "white"

# Tronc plus haut et plus mince
tronc_x1, tronc_y1 = 180, 200
tronc_x2, tronc_y2 = 220, 400
draw.rectangle((tronc_x1, tronc_y1, tronc_x2, tronc_y2), fill=tronc)

# Feuilles plus hautes et plus minces
draw.rectangle((150, 100, 250, 300), fill=feuille)

# Nombre de lignes et de colonnes dans la grille
rows = 5
cols = 5

# Taille de chaque grille
grid_width = (250 - 150) // cols
grid_height = (300 - 100) // rows

# Coordonnées des boules de neige réparties uniformément sur la surface des feuilles
random.seed(42)  # Pour obtenir des résultats reproductibles
for i in range(rows):
    for j in range(cols):
        # Coordonnées du coin supérieur gauche de la grille actuelle
        grid_x = 150 + j * grid_width
        grid_y = 100 + i * grid_height
        # Coordonnées aléatoires à l'intérieur de la grille
        x = random.randint(grid_x, grid_x + grid_width)
        y = random.randint(grid_y, grid_y + grid_height)
        draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=neige)  # Dessiner une boule de neige

image.save("erable_de_sucre-hiver.png")
