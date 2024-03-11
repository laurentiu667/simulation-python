





from PIL import Image, ImageDraw

# Create a new RGBA image with a transparent background
image = Image.new("RGBA", (100, 100), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Raccoon colors and characteristics
body_color = "gray"
mask_color = "black"
eye_color = "white"
nose_color = "black"
tail_color = "gray"

# Draw the raccoon's body
draw.ellipse((20, 40, 80, 90), fill=body_color)

# Draw the raccoon's tail with stripes
draw.rectangle((70, 60, 90, 80), fill=tail_color)  # Tail base
draw.line((75, 60, 75, 80), fill="black", width=2)  # Stripe 1
draw.line((85, 60, 85, 80), fill="black", width=2)  # Stripe 2

# Draw the head
draw.ellipse((35, 20, 65, 50), fill=body_color)

# Draw the mask
draw.ellipse((40, 25, 60, 45), fill=mask_color)

# Draw the eyes
draw.ellipse((43, 30, 48, 35), fill=eye_color)  # Left eye
draw.ellipse((52, 30, 57, 35), fill=eye_color)  # Right eye

# Draw the nose
draw.ellipse((48, 40, 52, 44), fill=nose_color)




image.save("laveur.png")