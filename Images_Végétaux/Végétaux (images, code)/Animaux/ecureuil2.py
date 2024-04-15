from PIL import Image, ImageDraw

# Créer une nouvelle image avec fond transparent
image = Image.new("RGBA", (100, 100), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Couleurs et caractéristiques de l'écureuil
couleur_corps_ecureuil = "saddlebrown"
couleur_ventre = "#D2B48C"  # Beige
couleur_oreille = "saddlebrown"
couleur_nez = "black"

# Dessiner le corps de l'écureuil
draw.ellipse((30, 40, 70, 80), fill=couleur_corps_ecureuil)

# Dessiner le ventre de l'écureuil (moitié inférieure du corps)
draw.ellipse((35, 60, 65, 80), fill=couleur_ventre)

# Dessiner la tête de l'écureuil
draw.ellipse((40, 30, 60, 50), fill=couleur_corps_ecureuil)

# Dessiner les oreilles de l'écureuil
draw.polygon([(40, 30), (45, 20), (50, 30)], fill=couleur_oreille)  # Oreille gauche
draw.polygon([(50, 30), (55, 20), (60, 30)], fill=couleur_oreille)  # Oreille droite

# Dessiner les yeux de l'écureuil
draw.ellipse((45, 40, 47, 42), fill=couleur_nez)  # Oeil gauche
draw.ellipse((53, 40, 55, 42), fill=couleur_nez)  # Oeil droit

# Dessiner le nez de l'écureuil
draw.ellipse((49, 45, 51, 47), fill=couleur_nez)

# Enregistrer l'image
image.save("ecureuil2.png")
