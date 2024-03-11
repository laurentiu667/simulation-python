from PIL import Image, ImageDraw

# Create a new RGBA image with a transparent background
image = Image.new("RGBA", (100, 100), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Beaver colors and characteristics
beaver_color = "darkgoldenrod"
tail_color = "burlywood"  # For the distinctive flat tail
eye_color = "black"

# Draw the beaver's body
draw.ellipse((30, 40, 70, 60), fill=beaver_color)

# Draw the head
draw.ellipse((40, 30, 60, 50), fill=beaver_color)

# Draw the ears
draw.ellipse((40, 25, 45, 30), fill=beaver_color)  # Left ear
draw.ellipse((55, 25, 60, 30), fill=beaver_color)  # Right ear

# Draw the eyes
draw.ellipse((43, 35, 47, 39), fill=eye_color)  # Left eye
draw.ellipse((53, 35, 57, 39), fill=eye_color)  # Right eye

# Draw the nose
draw.ellipse((48, 40, 52, 44), fill=eye_color)

image.save("castord.png")