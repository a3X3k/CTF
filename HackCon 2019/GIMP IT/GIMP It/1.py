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



