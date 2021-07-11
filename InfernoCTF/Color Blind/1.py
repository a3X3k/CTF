from PIL import Image

image = Image.open('1.png') # Opening image using Image module 

height = image.height
width = image.width 

for i in range(width):
	for j in range(height):
		r, g, b = image.getpixel((i, j))
		print("{}{}{}".format(chr(r),chr(g),chr(b)),end="")