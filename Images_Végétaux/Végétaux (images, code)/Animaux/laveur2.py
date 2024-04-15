from PIL import Image, ImageDraw

# Créer une nouvelle image avec fond transparent
image = Image.new("RGBA", (100, 100), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Couleurs pour le raton-laveur
couleur_corps = "gray"
couleur_ventre = "#a5a5a5"  # Gris clair
couleur_oreilles = "#222222"
couleur_yeux = "white"
couleur_nez = "#ff9999"  # Rouge lavé
couleur_queue = "gray"
couleur_pupille = "black"

# Dessiner le corps du raton-laveur
draw.ellipse((20, 40, 80, 90), fill=couleur_corps)

# Dessiner une tache grise sur le ventre
draw.ellipse((30, 70, 70, 90), fill=couleur_ventre)

# Dessiner la queue du raton-laveur avec des rayures
draw.ellipse((70, 60, 90, 80), fill=couleur_queue)  # Base de la queue
draw.line((75, 60, 75, 80), fill="black", width=2)  # Rayure 1
draw.line((85, 62, 85, 78), fill="black", width=2)  # Rayure 2

# Dessiner la tête
draw.ellipse((35, 20, 65, 50), fill=couleur_corps)

# Dessiner le masque
draw.ellipse((40, 25, 60, 45), fill="black")

# Dessiner les yeux
draw.ellipse((43, 30, 48, 35), fill=couleur_yeux)  # Oeil gauche
draw.ellipse((52, 30, 57, 35), fill=couleur_yeux)  # Oeil droit

# Dessiner les pupilles
draw.ellipse((45, 32, 46, 33), fill=couleur_pupille)  # Pupille gauche
draw.ellipse((54, 32, 55, 33), fill=couleur_pupille)  # Pupille droite

# Dessiner le nez
draw.ellipse((48, 37, 52, 41), fill=couleur_nez)

# Dessiner les oreilles
draw.ellipse((33, 10, 47, 25), fill=couleur_oreilles)  # Oreille gauche
draw.ellipse((53, 10, 67, 25), fill=couleur_oreilles)  # Oreille droite

# Enregistrer l'image
image.save("laveur2.png")
