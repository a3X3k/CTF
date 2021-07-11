# Information

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/Pico21/Assets/11.png?raw=true)

 - Download the File.

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/Pico21/Assets/12.jpg?raw=true)

- Try `exiftool` to view the details of the file since its mentioned as `hint`.

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/Pico21/Assets/13.png?raw=true)

- It contains the `Base64` encoded text.
- So [decoding](https://www.base64decode.org/) it will give the flag.

```
cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
```

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/Pico21/Assets/14.png?raw=true)

```
Flag --> picoCTF{the_m3tadata_1s_modified}
```


