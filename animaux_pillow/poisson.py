from PIL import Image, ImageDraw

# Create a new RGBA image with a transparent background
image = Image.new("RGBA", (100, 100), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Fish colors and characteristics
fish_body_color = "firebrick"
eye_color = "white"
eye_pupil_color = "black"

# Draw the fish body
draw.ellipse((20, 30, 80, 70), fill=fish_body_color)

# Draw the fish tail
draw.polygon([(80, 50), (100, 40), (100, 60)], fill=fish_body_color)

# Draw the fish eye
draw.ellipse((30, 45, 40, 55), fill=eye_color)
draw.ellipse((35, 50, 37, 52), fill=eye_pupil_color)

image.save("poisson.png")