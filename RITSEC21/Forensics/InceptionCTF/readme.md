# Inception CTF

#### Dream 1

- Extract the Zip.
- `InceptionCTF` contains `Reality.7z` .
- Extract it to get `Reality` folder.
- Two files will be extracted.
- Suspicious.txt and `Vanchaze.7z`.
- Suspicious.txt contains reversed file.
- Reversing the contents will give the flag.

```
InceptionCTF --> Reality --> Suspicious.txt

Flag --> RITSEC{Dreamland}
```

#### Dream 2

- Extracting `Vanchase.7z` will give `kidnap.txt`.
- It contains Hex code and decoding it will give the flag.

```
InceptionCTF --> Reality --> Vanchase --> kidnap.txt

Hex code : "52 49 54 53 45 43 7b 57 61 74 65 72 55 6e 64 65 72 54 68 65 42 72 69 64 67 65 7d".

Flag --> RITSEC{WaterUnderTheBridge} 
``` 

#### Dream 3

- Extracting `TheHotel.7z` will give `ThePointman.txt`.
- It contains `Base64` encoded text and decoding it will give the flag.

```
InceptionCTF --> Reality --> Vanchase --> THEHotel --> ThePointman.txt 
 
 Flag --> RITSEC{F@!!ingElev@tor}
```

#### Dream 4

- Extracting `Snowfortress.7z` will give `Passwordpath.exe`.

```
InceptionCTF  --> Reality --> Vanchase --> THEHotel --> Snowfortress --> Passwordpath.exe
```

- Now `cat` the Passwordpath.exe and we shall see the `Java Script code`.
- Decoding the `JS` gives `Morsecode`.
- Decoding the `Morse code` gives the flag.

```
Flag --> RITSEC{DIVERSION}
```

#### Dream 5

- Extracting `Limbo.7z` will give `Inception.jpg`.

```
 --> Reality --> Vanchase --> THEHotel --> Snowfortress --> Limbo --> Inception.jpg
```

- Doing `strings` in `Inception.jpg` gives Base64 encoded text `UklUU0VDezUyODQ5MX0g`.
- Decode it to get the flag.

```
Flag --> RITSEC{528491}
```

