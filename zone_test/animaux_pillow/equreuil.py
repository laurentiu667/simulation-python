from PIL import Image, ImageDraw

# Create a new RGBA image with a transparent background
image = Image.new("RGBA", (100, 100), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Squirrel colors and characteristics
squirrel_body_color = "saddlebrown"
tail_color = "sienna"  # A lighter brown for the fluffy tail
eye_color = "black"

# Draw the squirrel's body
draw.ellipse((30, 40, 70, 80), fill=squirrel_body_color)


# Draw the head
draw.ellipse((40, 30, 60, 50), fill=squirrel_body_color)

# Draw the ears
draw.polygon([(40, 30), (45, 20), (50, 30)], fill=squirrel_body_color)  # Left ear
draw.polygon([(50, 30), (55, 20), (60, 30)], fill=squirrel_body_color)  # Right ear

# Draw the eyes
draw.ellipse((45, 40, 47, 42), fill=eye_color)  # Left eye
draw.ellipse((53, 40, 55, 42), fill=eye_color)  # Right eye

# Draw the nose
draw.ellipse((49, 45, 51, 47), fill=eye_color)


image.save("ecureuil.png")