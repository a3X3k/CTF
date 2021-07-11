# Parcel

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/RITSEC21/Assets/8.png?raw=true)

- `File format` is not known.
- So lets see the file type with `file` command.
- We shall see that the file format is `gzip`.

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/RITSEC21/Assets/11.png?raw=true)

- So lets rename the file to `.gzip`.
- Now if we extract it we shall see that there is an file inside with unknown format.
- Just changing the file format to `txt` will open it.

[Txt](https://github.com/a3X3k/Bi0s/blob/master/CTFs/RITSEC21/Assets/Parcel.txt)
[GZ File](https://github.com/a3X3k/Bi0s/blob/master/CTFs/RITSEC21/Assets/Parcel.gz)

- In txt file we shall see the Base64 encoded texts.
- [Decoding](https://www.base64decode.org/) it will give the `PNG` Image header.
- So decoding all texts will give multiple images.
- Use [Online Tool](https://base64.guru/converter/decode/image/png) to extract the images directly. 
- Concatenating all images will yeild the flage.

```
Flag --> RS{Im_doing_a_v1rtual_puzzl3}
```


