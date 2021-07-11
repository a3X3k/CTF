# Glute

![](https://github.com/a3X3k/Bi0s/blob/master/CTFs/WPI/Glute/Assets/1.png?raw=true)

- We are provided with a `PNG` image.

![](https://github.com/a3X3k/Bi0s/blob/master/CTFs/WPI/Glute/Assets/glute.png?raw=true)

- Using `foremost` we shall carve out the files.

```
foremost -i <File Name>

foremost -i glute.png
```

- We shall get [`JPG`](https://github.com/a3X3k/Bi0s/blob/master/CTFs/WPI/Glute/Assets/output/jpg/00000564.jpg?raw=true),[`PNG`](https://github.com/a3X3k/Bi0s/blob/master/CTFs/WPI/Glute/Assets/output/png/00000000.png?raw=true),[`PDF`](https://github.com/a3X3k/Bi0s/blob/master/CTFs/WPI/Glute/Assets/output/pdf/00000557.pdf) files.
- In the [`PDF`](https://github.com/a3X3k/Bi0s/blob/master/CTFs/WPI/Glute/Assets/output/pdf/00000557.pdf) we shall get the flag.

![](https://github.com/a3X3k/Bi0s/blob/master/CTFs/WPI/Glute/Assets/2.png?raw=true)

```
Flag --> WPI{P0lyGlOtz_R_koo1}
```
