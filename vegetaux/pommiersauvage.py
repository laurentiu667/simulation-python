# import random
# from PIL import Image, ImageDraw
#
# image = Image.new("RGBA", (400, 400), (255, 255, 255, 100))
# draw = ImageDraw.Draw(image)
#
# tronc = "saddlebrown"
# feuille = "olivedrab"
# pomme = "lemonchiffon"
#
#
# # Tronc plus haut et plus mince
# draw.rectangle((180, 200, 220, 400), fill=tronc)
#
# # Feuilles plus hautes et plus minces
# draw.rectangle((150, 100, 250, 300), fill=feuille)
#
# # Ajouter les pommes
# for _ in range(15):  # Dessiner 10 pommes
#     x = random.randint(160, 240)  # Position aléatoire en x dans le rectangle des feuilles avec marge de 10px
#     y = random.randint(110, 290)  # Position aléatoire en y dans le rectangle des feuilles avec marge de 10px
#     draw.ellipse((x, y, x + 10, y + 10), fill=pomme)  # Dessiner une pomme (cercle rouge)
#
# image.save("pommiersauvage-printemps.png")
