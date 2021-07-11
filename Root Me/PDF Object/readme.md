# PDF Object

- Download the [`PDF`](https://github.com/a3X3k/RoadMap/blob/main/Set%203/Rootme/PDF%20Object/1.pdf) given.
- Analyse using `Peepdf`.
- [`Reference 1`](https://eternal-todo.com/tools/peepdf-pdf-analysis-tool) [`Reference 2`](https://singhgurjot.wordpress.com/2015/04/15/how-to-use-peepdf-suspecious-pdf-in-kali-linux/)



![](https://github.com/a3X3k/RoadMap/blob/main/Set%203/Rootme/PDF%20Object/1.png?raw=true)

![](https://github.com/a3X3k/RoadMap/blob/main/Set%203/Rootme/PDF%20Object/2.png?raw=true)

- We shall see that there are `78 Objects` and `25 Streams`.
- We shall see there is an `embedded file` in the `PDF`.
- So now we need to extract the `embedded file` using the `stream` command.
- Totally there are `25 streams`.

![](https://github.com/a3X3k/RoadMap/blob/main/Set%203/Rootme/PDF%20Object/3.png?raw=true)

- After `analysing` all only the `stream 77` seemed to have some `suspicious` data.

![](https://github.com/a3X3k/RoadMap/blob/main/Set%203/Rootme/PDF%20Object/4.png?raw=true)

- Lets redirect the output to the [`TXT`](https://github.com/a3X3k/RoadMap/blob/main/Set%203/Rootme/PDF%20Object/1.txt) file and see what's that.

```
PPDF> stream 77 > 1.txt
```

- It seems to look like a `Base 64` encoded text.
- So let's try to `decode` it.

![](https://github.com/a3X3k/RoadMap/blob/main/Set%203/Rootme/PDF%20Object/5.png?raw=true)
![](https://github.com/a3X3k/RoadMap/blob/main/Set%203/Rootme/PDF%20Object/6.png?raw=true)

- We shall see that its an `JPEG` Image after decoding the Base64 Encoded.
- Now lets redirect the output to the `JPEG` file.

```
PPDF> decode file 1.txt base64 > 1.jpeg
```

- Now we got a [`Image`](https://github.com/a3X3k/RoadMap/blob/main/Set%203/Rootme/PDF%20Object/1.jpeg) which has the `Flag`.

```
Hidden_embedded_Fil3
```

