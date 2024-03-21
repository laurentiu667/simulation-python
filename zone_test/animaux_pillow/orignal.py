from PIL import Image, ImageDraw

image = Image.new("RGBA", (100, 100), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)


moose_color = "saddlebrown"
ear_color = "peru"
eye_nose_color = "black"


draw.ellipse((20, 30, 80, 90), fill=moose_color)


draw.ellipse((15, 40, 35, 60), fill=ear_color)  # Left ear
draw.ellipse((65, 40, 85, 60), fill=ear_color)  # Right ear


draw.line((25, 35, 10, 10), fill="grey", width=3)
draw.line((25, 35, 5, 25), fill="grey", width=3)  # Left antler bottom
draw.line((75, 35, 90, 10), fill="grey", width=3)  # Right antler top
draw.line((75, 35, 95, 25), fill="grey", width=3)  # Right antler bottom

# Draw the eyes
draw.ellipse((40, 60, 45, 65), fill=eye_nose_color)  # Left eye
draw.ellipse((55, 60, 60, 65), fill=eye_nose_color)  # Right eye

# Draw the nose
draw.ellipse((47, 75, 53, 81), fill=eye_nose_color)

image.save("orignal.png")