# Peace

![](https://github.com/a3x3k/Bi0s/blob/master/CTFs/Vishwa_Ctf/Assets/5.png?raw=true)

- Download the `rar` file given.
- Crack the `rar password` using `rar2john`.

```
rar2john morse.rar > ki.txt
```

- `unrar` the `rar` file using password `india`

![](https://github.com/a3x3k/Bi0s/blob/master/CTFs/Vishwa_Ctf/Assets/6.png?raw=true)

- We will get a `morse encrypted audio` file.
- Use `morse decoder` to `decode` the content.

```sh
76 69 73 68 77 61 63 74 66 7B 37 68 33 79 5F 34 72 45 5F 46 30 72 33 66 65 37 31 6E 67 7D
```

- We will get the `hexadecimal` values.
- Decode it to get the `ASCII` text.

```sh
Flag --> vishwactf{7h3y_4rE_F0r3fe71ng}
```
