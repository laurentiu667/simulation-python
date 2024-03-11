from PIL import Image, ImageDraw

# Create a new RGBA image with a transparent background
image = Image.new("RGBA", (100, 100), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Rabbit colors and characteristics
rabbit_color = "lightgray"
ear_color = "pink"
eye_color = "black"

# Draw the rabbit's body
draw.ellipse((40, 30, 60, 60), fill=rabbit_color)

# Draw the head
draw.ellipse((40, 30, 60, 50), fill=rabbit_color)

# Draw curved ears
draw.ellipse((30, 20, 40, 40), fill=rabbit_color)  # Left ear base
draw.ellipse((60, 20, 70, 40), fill=rabbit_color)  # Right ear base


# Add pink inner ear
draw.ellipse((35, 20, 38, 30), fill=ear_color)  # Left inner ear
draw.ellipse((62, 20, 65, 30), fill=ear_color)  # Right inner ear

# Draw the eyes
draw.ellipse((43, 35, 47, 39), fill=eye_color)  # Left eye
draw.ellipse((53, 35, 57, 39), fill=eye_color)  # Right eye

# Draw the nose
draw.ellipse((48, 40, 52, 44), fill=eye_color)

image.save("lapin.png")