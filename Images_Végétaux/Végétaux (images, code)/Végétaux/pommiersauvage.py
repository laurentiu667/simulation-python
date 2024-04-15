import random
from PIL import Image, ImageDraw

image = Image.new("RGBA", (400, 400), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

tronc = "#663e2d"
feuille = "#348e58"
pomme = "#e93d3d"

# Tronc plus haut et plus mince
draw.rectangle((180, 200, 220, 400), fill=tronc)

# Feuilles plus hautes et plus minces
draw.rectangle((150, 100, 250, 300), fill=feuille)

# Nombre de lignes et de colonnes dans la grille
rows = 5
cols = 5

# Taille de chaque grille
grid_width = (250 - 150) // cols
grid_height = (300 - 100) // rows

# Coordonnées des pommes réparties uniformément sur la surface des feuilles
random.seed(42)  # Pour obtenir des résultats reproductibles
for i in range(rows):
    for j in range(cols):
        # Coordonnées du coin supérieur gauche de la grille actuelle
        grid_x = 150 + j * grid_width
        grid_y = 100 + i * grid_height
        # Coordonnées aléatoires à l'intérieur de la grille
        x = random.randint(grid_x, grid_x + grid_width)
        y = random.randint(grid_y, grid_y + grid_height)
        draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=pomme)  # Dessiner une pomme

image.save("pommiersauvage.png")
