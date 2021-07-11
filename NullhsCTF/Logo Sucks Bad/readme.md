# Logo Sucks Bad

- Download the [`PNG Image`](https://github.com/a3X3k/RoadMap/blob/main/Set%202/Logo%20Sucks%20Bad/logo.png)
- Try analysing using `zsteg`.

![](https://github.com/a3X3k/RoadMap/blob/main/Set%202/Logo%20Sucks%20Bad/2.png?raw=true)

- We shall see the `Lorum Ipsum` text there in the `b1,rgb,lsb,xy` payload.
- Let's extract the entire `LSB payload` from the Image.

```
zsteg -E <PayLoad> <File Name>

zsteg -E b1,rgb,lsb,xy logo.png
```

![](https://github.com/a3X3k/RoadMap/blob/main/Set%202/Logo%20Sucks%20Bad/3.png?raw=true)

- We shall see the `flag` in between the text.

```
nullhsctf{th4_l3est_s3gnific3nt_bbbbbbbbbbbbb}
```

