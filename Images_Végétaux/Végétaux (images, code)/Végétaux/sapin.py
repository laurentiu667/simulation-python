from PIL import Image, ImageDraw
# Créer une nouvelle image avec fond transparent
image = Image.new("RGBA", (400, 400), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Couleur du tronc et du sapin
tronc = "#663e2d"
sapin = "#15561b"

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

# Enregistrer l'image
image.save("sapin.png")



