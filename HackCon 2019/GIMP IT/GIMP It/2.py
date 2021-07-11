from PIL import Image

with open('data.txt','r') as f:
	buff = f.read()

rgb=[]
for i in range(len(buff)):
	if buff[i]=='0':
		rgb.append((255,255,255))
	else:
		rgb.append((0,0,0))

image = Image.new(mode="RGBA", size=(370,370))
image.putdata(rgb)
image.save("2.png")


