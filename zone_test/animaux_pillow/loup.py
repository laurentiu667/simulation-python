from PIL import Image, ImageDraw


image = Image.new("RGBA", (100, 100), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)


wolf_color = "grey"
ear_inner_color = "lightgrey"
eye_nose_color = "black"


draw.ellipse((30, 20, 70, 60), fill=wolf_color)

draw.polygon([(25, 10), (32, 2), (40, 10)], fill=wolf_color)
draw.polygon([(60, 10), (68, 2), (75, 10)], fill=wolf_color)


draw.ellipse((30, 15, 35, 20), fill=ear_inner_color)
draw.ellipse((65, 15, 70, 20), fill=ear_inner_color)

draw.ellipse((40, 35, 45, 40), fill=eye_nose_color)
draw.ellipse((55, 35, 60, 40), fill=eye_nose_color)


draw.ellipse((47, 45, 53, 51), fill=eye_nose_color)

image.save("loup.png")