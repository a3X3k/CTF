with open('Given Hex.txt','r') as f:
	buff = f.read()

temp = ""
temp = buff.replace("20", "")
temp = temp.replace(" 0a", "")
temp = temp.replace(" ", "")

temp = bytes.fromhex(temp)
temp = temp.decode("ASCII")

f = open("Decoded Given Hex.txt", "w")
f.write(temp)
f.close()