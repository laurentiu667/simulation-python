from PIL import *

# Créer une nouvelle image blanche de taille 400x400 pixels
image = Image.new("RGB", (400, 400), "white")

# Initialiser l'objet pour dessiner sur l'image
draw = ImageDraw.Draw(image)

# Dessiner le corps du loup (un cercle)
draw.ellipse((100, 100, 300, 300), fill="gray")

# Dessiner la tête du loup (un cercle)
draw.ellipse((150, 50, 250, 150), fill="gray")

# Dessiner les oreilles du loup (deux ellipses)
draw.ellipse((160, 30, 190, 70), fill="gray")
draw.ellipse((210, 30, 240, 70), fill="gray")

# Dessiner les yeux du loup (deux cercles)
draw.ellipse((180, 80, 200, 100), fill="white")
draw.ellipse((220, 80, 240, 100), fill="white")

# Dessiner les pupilles du loup (deux cercles noirs)
draw.ellipse((190, 90, 195, 95), fill="black")
draw.ellipse((230, 90, 235, 95), fill="black")

# Dessiner le nez du loup (un triangle)
draw.polygon([(205, 110), (215, 110), (210, 120)], fill="black")

# Dessiner la bouche du loup (un arc de cercle)
draw.arc((200, 120, 220, 140), start=0, end=180, fill="black")

# Enregistrer l'image
image.save("loup.png")

# Afficher l'image
image.show()
