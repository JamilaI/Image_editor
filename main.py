import imageio.v2
from rembg import remove
from PIL import Image,ImageFilter, ImageDraw, ImageFont, ImageEnhance, ImageOps
#ImageDraw= allows drawing shapes, texts in image , ImageEnhance= for  brightness, contrast, color balance, and sharpness, ImageOps= (grayscale) and 'RGB'

#Remove background and save it as new picture

input_path = 'angelina.jpg'
output_path = 'angelina2.png'

inp = Image.open(input_path)
output = remove(inp)

output.save(output_path)
Image.open(output_path)

 #make the background blury rather than deleting the bg
"""blurry_background = inp.filter(ImageFilter.GaussianBlur(15))
image =Image.composite(output, blurry_background, output.split()[-1])"""


#write text on the picture

image = Image.open(output_path)
user_text = input("Enter the text:  ")

draw = ImageDraw.Draw(image)

try:
    font = ImageFont.truetype("arial.ttf", 50) #font type and size

except:
    font = ImageFont.load_default()

width, height = image.size

# Position text roughly at bottom-center
bbox = draw.textbbox((0, 0), user_text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
x = (width - text_width) / 2
y = height - text_height - 30  # 30px from bottom


# Draw text (white with black outline)
for dx in (-2, 2):
    for dy in (-2, 2):
        draw.text((x + dx, y + dy), user_text, font=font, fill="black")
draw.text((x, y), user_text, font=font, fill="white")

#add different filters on the image
print("Select filter: ")
print("1 Black and White")
print("2 Cool")
print("3 warm")
print("4 Dramatic")
print("5 Sepia")
print("6 none")

choice = input("Select a number:  ")

if choice == "1":
    image = ImageOps.grayscale(image)

elif choice == "2":
    r, g, b, *rest = image.split() + [None] * (4 - len(image.split()))
    r = r.point(lambda i: i * 1.1)
    b = b.point(lambda i: i * 0.9)
    image = Image.merge("RGB", (r, g, b))

elif choice == "3":  # Cool filter (enhance blues)
    r, g, b, *rest = image.split() + [None] * (4 - len(image.split()))
    r = r.point(lambda i: i * 0.9)
    b = b.point(lambda i: i * 1.1)
    image = Image.merge("RGB", (r, g, b))

elif choice == "4":  # Dramatic (increase contrast)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.8)

elif choice == "5":  # Sepia tone
    sepia = ImageOps.colorize(ImageOps.grayscale(image), "#704214", "#C0A080")
    image = sepia

else:
    print("No filter applied!")
# Step 6: Save new image
image.save(output_path)
print(f"Text and filter added successfully! Saved as {output_path}")



