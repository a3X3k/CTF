# GIMP IT

- Download the [`xcf`](https://github.com/a3X3k/RoadMap/blob/main/Set%204/GIMP%20IT/GIMP%20It/1.xcf) file.
- Try `strings` analysis.

![](https://github.com/a3X3k/RoadMap/blob/main/Set%204/GIMP%20IT/GIMP%20It/3.png?raw=true)

- This shows that there is an `GIMP` `text` Layer.
- When you add text in [`GIMP`](https://www.quackit.com/web_graphics/gimp/tutorial/adding_text_with_gimp.cfm#:~:text=Text%20And%20Layers,other%20parts%20of%20the%20image.), a new layer is added automatically. 
- We shall see that there is `50 4b 03 04` in the `text` layer.
- This is the `Magic Number` of `ZIP` file.
- So I made a [`script`](https://github.com/a3X3k/RoadMap/blob/main/Set%204/GIMP%20IT/GIMP%20It/1.py) to `extract` the text from the `text` layer.

```
from zipfile import ZipFile

import binascii
  
with open('1.xcf','rb') as f:
	buff = f.read()

buff = buff.replace(" ","")
buff = buff.replace("\\n","")
start=buff.find('504b')
end=buff.find('0500000000')
end+=10

with open("1.zip", "wb") as g:
    g.write(buff[start:end].decode("hex"))

with ZipFile("1.zip", 'r') as zip:
	zip.extractall()
```

- This script `extracts` the [`ZIP`](https://github.com/a3X3k/RoadMap/blob/main/Set%204/GIMP%20IT/GIMP%20It/1.zip) file and `unzips` its contents.
- We shall get the [`data.txt`](https://github.com/a3X3k/RoadMap/blob/main/Set%204/GIMP%20IT/GIMP%20It/data.txt) file after `unzipping`.
- The file is filled with `0`'s and `1`'s.
- In some of the previous CTF challenges, I came to know that we shall create a `QR` code from the `0`'s and `1`'s.
- So I made a [`script`](https://github.com/a3X3k/RoadMap/blob/main/Set%204/GIMP%20IT/GIMP%20It/2.py) to convert the `0`'s and `1`'s to `QR` code.

```
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
```

- After creating the Image I saved it as [`PNG`](https://github.com/a3X3k/RoadMap/blob/main/Set%204/GIMP%20IT/GIMP%20It/2.png) image. ( Can be `JPG` or `JPEG` or `BMP` too ).
- Scanning it using `zbarimg` we shall get the `flag`.

![](https://github.com/a3X3k/RoadMap/blob/main/Set%204/GIMP%20IT/GIMP%20It/4.png?raw=true)

```
d4rk{L0t5_0f_th1ng5_t0_d0_1n_th15_chAll@ng3}c0de
```


