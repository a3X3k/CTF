from scapy.all import *
a=rdpcap("/home/sai/Downloads/capture.pcapng")
z=""
for i in a:
	b=""
	for j in i:
		b=b+str(j)
	if(len(b)==46 or len(b)==282):
		z=z+b[-2]
print(z)
		
