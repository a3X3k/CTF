# Weird File

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/Pico21/Assets/15.jpeg?raw=true)

- Download the `docm` file.
- `oletools` is a package of python tools to analyze Microsoft OLE2 files.
- Using this we shall try to analyze the file.

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/Pico21/Assets/16.jpeg?raw=true)

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/Pico21/Assets/17.jpeg?raw=true)

- It contains the `Base64` encoded text.
- So [decoding](https://www.base64decode.org/) it will give the flag.

```
cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9
```

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/Pico21/Assets/18.jpeg?raw=true)

```
Flag --> picoCTF{m4cr0s_r_d4ng3r0us}
```
