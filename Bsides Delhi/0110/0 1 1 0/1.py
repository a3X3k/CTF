from PIL import Image, ImageChops
     
# creating a image1 object 
im1 = Image.open("1.png") .convert("1")
     
# creating a image2 object 
im2 = Image.open("2.png") .convert("1")
     
# applying logical_xor method 
ImageChops.logical_xor(im1, im2).save("3.png")
