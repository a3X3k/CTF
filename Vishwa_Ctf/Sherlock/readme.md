# Sherlock

![](https://github.com/a3x3k/Bi0s/blob/master/CTFs/Vishwa_Ctf/Assets/7.png?raw=true)

- Download the Image File given.

![](https://github.com/a3x3k/Bi0s/blob/master/CTFs/Vishwa_Ctf/Assets/8.jpg?raw=true)

- From the `Magic Numbers` we shall find that the given image is actually a `png` format.
- But we get it as `jpg`.
- So `change` its `format` to `png`.
- Use `zsteg` tool to extract the hidden information.

```sh
zsteg -a decode.png
```

![](https://github.com/a3x3k/Bi0s/blob/master/CTFs/Vishwa_Ctf/Assets/9.png?raw=true)

```sh
Flag --> vishwaCTF{@w3s0Me_sh3Rl0cK_H0m3s}
```
