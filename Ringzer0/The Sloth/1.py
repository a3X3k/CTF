with open('1.png','rb') as f:
	buff = f.read()

temp = ""

for i in range(0,len(buff)):
	if buff[i] == 'I' and buff[i+1] == 'D' and buff[i+2] == 'A' and buff[i+3] == 'T':		 
		temp += buff[i-1]

print(temp)