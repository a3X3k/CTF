# Lost at Sea

![](https://github.com/a3X3k/Bi0s/blob/master/CTFs/WPI/Suspicious%20Traffic/1.png?raw=true)

- Download the [`PCAPNG`](https://github.com/a3X3k/Bi0s/blob/master/CTFs/WPI/Suspicious%20Traffic/capture.pcapng) file.
- Using Wireshark analyze it.
- After follow `HTTP` requests we shall understand that the `Flag` is present `Byte` by `Byte`.
- So I have made a [`Scapy`](https://github.com/a3X3k/Bi0s/blob/master/CTFs/WPI/Suspicious%20Traffic/1.py) script for extracting them.

```
from scapy.all import *
a=rdpcap("capture.pcapng")
z=""
for i in a:
	b=""
	for j in i:
		b=b+str(j)
	if(len(b)==46 or len(b)==282):
		z=z+b[-2]
print(z)
```

```
Flag --> WPI{su3p1ci0uS_htTp}
```
