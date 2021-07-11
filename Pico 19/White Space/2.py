from pwn import *

with open("whitepages.txt", "rb") as bin_file:
    data = bytearray(bin_file.read()) 
    data = data.replace(b'\xe2\x80\x83', b'0')
    data = data.replace(b'\x20', b'1')
    data = data.decode("ascii")
    print(unbits(data))
