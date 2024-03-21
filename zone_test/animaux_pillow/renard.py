from PIL import Image, ImageDraw

# Create a new RGBA image with a transparent background
image = Image.new("RGBA", (100, 100), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

lynx_color = "saddlebrown"
ear_inner_color = "lightgrey"
eye_nose_color = "black"

draw.ellipse((30, 20, 70, 60), fill=lynx_color)

# Decreased the Y coordinates to lower the ears
draw.polygon([(25, 20), (32, 10), (40, 20)], fill=lynx_color)
draw.polygon([(60, 20), (67, 10), (75, 20)], fill=lynx_color)

draw.ellipse((40, 35, 45, 40), fill=eye_nose_color)
draw.ellipse((55, 35, 60, 40), fill=eye_nose_color)

draw.ellipse((47, 45, 53, 51), fill=eye_nose_color)

draw.line((50, 60, 50, 65), fill=lynx_color, width=4)

image.save("renard.png")
