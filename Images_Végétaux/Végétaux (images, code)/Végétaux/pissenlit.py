import random
from PIL import Image, ImageDraw

image = Image.new("RGBA", (400, 400), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

tronc = "gray"
rectangle = "yellow"

draw.rectangle((190, 200, 210, 400), fill=tronc)

draw.rectangle((170, 50, 230, 200), fill=rectangle)

image.save("pissenlit.png")
