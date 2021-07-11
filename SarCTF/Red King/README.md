# Red King

- Download the [`PNG Image`](https://github.com/a3X3k/RoadMap/blob/main/Set%202/Red%20King/1.png)
- Try analysing using `zsteg`.

![](https://github.com/a3X3k/RoadMap/blob/main/Set%202/Red%20King/2.png?raw=true)

- Intial analysis using `zsteg <File Name>` didn't give any much data.
- So lets analyse using `zsteg -a <File Name>` which gives all hidden information.

![](https://github.com/a3X3k/RoadMap/blob/main/Set%202/Red%20King/3.png?raw=true)

- We shall see the `In 1989, Moriarty Murdered...` text there in the `b1,r,lsb,yx` payload.
- Let's extract the entire `LSB payload` from the Image.

```
zsteg -E <PayLoad> <File Name>

zsteg -E b1,r,lsb,yx 1.png
```

![](https://github.com/a3X3k/RoadMap/blob/main/Set%202/Red%20King/4.png?raw=true)

- We shall see the `flag` in between the text.

```
FLAG{who_is_moriarty}
```
