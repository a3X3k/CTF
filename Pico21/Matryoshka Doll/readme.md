# Matryoshka Doll

![](https://github.com/a3X3k/Bi0s/blob/master/CTFs/Pico21/Assets/22.png?raw=true)

- Download the file given.

![](https://github.com/a3X3k/Bi0s/blob/master/CTFs/Pico21/Assets/21.jpg?raw=true)

- Trying `binwalk` carves out many files.
- But it `recursively` gives images and each time we have to `carve` it out seperately.
- So we shall use the `binwalk` `recursive` `carving` command.

```
binwalk -e -M <filename> # ( -M = Recursive )

binwalk -e -M dolls.jpg
```

![](https://github.com/a3X3k/Bi0s/blob/master/CTFs/Pico21/Assets/19.png?raw=true)

![](https://github.com/a3X3k/Bi0s/blob/master/CTFs/Pico21/Assets/20.png?raw=true)

- It gives `_dolls.jpg.extracted\base_images\_2_c.jpg.extracted\base_images\_3_c.jpg.extracted\base_images\_4_c.jpg.extracted` these directories.
- In the final directory we shall find the `flag.txt` which contains the `flag`.

```
Flag --> picoCTF{96fac089316e094d41ea046900197662}
```
