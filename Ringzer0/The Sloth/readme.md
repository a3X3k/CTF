# The Sloth

- We are provided with the [`PNG`](https://github.com/a3X3k/RoadMap/blob/main/Set%201/RingZer0/The%20Sloth/1.png) Image.
- While going through the `Hex Dump`, I found out this is a `Pattern Tracing Challenge`.
- I found suspicious `IDAT` chunk in the file.
- Further Looking all `Hex Dumps` gives the idea how the challenge is made.
- Author of the Challenge, `concatenated` each letter of the `flag` to the each `IDAT` chunk.
- So I made a [`script`](https://github.com/a3X3k/RoadMap/blob/main/Set%201/RingZer0/The%20Sloth/1.py) to extract the `flag`.

```
with open('1.png','rb') as f:
	buff = f.read()

temp = ""

for i in range(0,len(buff)):
	if buff[i] == 'I' and buff[i+1] == 'D' and buff[i+2] == 'A' and buff[i+3] == 'T':		 
		temp += buff[i-1]

print(temp)
```

- This will print out the `flag`.

```
FLAG-g77miF1E1awTS8t9TkY2hEMw2sqeXGt
```
