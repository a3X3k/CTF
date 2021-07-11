# Wireshark Doo Dooo Do Doo...

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/Pico21/Assets/1.png?raw=true)

- Download the `PCAPNG` file.
- Analyse it using `Wireshark`.
- After following `TCP` Stream we shall find that the last line seems to be like a flag in `tcp.stream eq 5`

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/Pico21/Assets/2.png?raw=true)

```
cvpbPGS{c33xno00_1_f33_h_qrnqorrs}
```

- Its ROT13 Encrypted.
- So [decoding](https://www.dcode.fr/caesar-cipher) it will give the flag.

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/Pico21/Assets/3.png?raw=true)

```
Flag --> picoCTF{p33kab00_1_s33_u_deadbeef}
```
