from PIL import Image, ImageDraw


image = Image.new("RGBA", (100, 100), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)


bear_color = "brown"
ear_inner_color = "lightgrey"
eye_nose_color = "black"


# Draw the bear's head
draw.ellipse((30, 20, 70, 60), fill=bear_color)

# Draw the ears
draw.ellipse((25, 10, 40, 25), fill=bear_color)
draw.ellipse((60, 10, 75, 25), fill=bear_color)
draw.ellipse((30, 15, 35, 20), fill=ear_inner_color)
draw.ellipse((65, 15, 70, 20), fill=ear_inner_color)

# Draw the eyes
draw.ellipse((40, 35, 45, 40), fill=eye_nose_color)
draw.ellipse((55, 35, 60, 40), fill=eye_nose_color)

# Draw the nose
draw.ellipse((47, 45, 53, 51), fill=eye_nose_color)


image.save("bear.png")