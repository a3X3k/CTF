# 0110

## Approach 1

- Download the [`PNG 1`](https://github.com/a3X3k/RoadMap/blob/main/Set%204/0110/0%201%201%200/1.png) and [`PNG 2`](https://github.com/a3X3k/RoadMap/blob/main/Set%204/0110/0%201%201%200/2.png)
- When `PNG 1` is scanned we get `-------------Sorry, No flag!!!!!!!-------------` as the output.
- When `PNG 2` is scanned we don't get any data.
- Now if we notice the `PNG 1` carefully we shall see that some portion of the `QR` code is not completely filled.
- So I got an idea to `XOR` the Image to combine them both to get a single `QR` code.
- So I made a [`script`](https://github.com/a3X3k/RoadMap/blob/main/Set%204/0110/0%201%201%200/1.py) to `XOR` the Image.

```
from PIL import Image, ImageChops

im1 = Image.open("1.png") .convert("1")

im2 = Image.open("2.png") .convert("1")
     
# applying logical_xor method 
ImageChops.logical_xor(im1, im2).save("3.png")
```

- Now we get the [`XOR`ed](https://github.com/a3X3k/RoadMap/blob/main/Set%204/0110/0%201%201%200/3.png) Image.

![](https://github.com/a3X3k/RoadMap/blob/main/Set%204/0110/0%201%201%200/3.png?raw=true)

- Scanning it using `zbarimg` we shall get the `flag`.

![](https://github.com/a3X3k/RoadMap/blob/main/Set%204/0110/0%201%201%200/4.png?raw=true)

## Approach 2

- Use `Image Combiner` option from `Stegsolve` to `XOR` the Image.
- Scanning the `XOR`ed Image using `zbarimg` we shall get the `flag`.

```
bsides_delhi{X0r1ng_tw0_f1l3s_g1v3s_7h3_r3sul7}
```




