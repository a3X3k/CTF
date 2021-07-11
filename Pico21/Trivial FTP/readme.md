# Trivial Flag Transfer Protocol

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/Pico21/Assets/4.png?raw=true)

- While Downloading the `PCAPNG` file itself we shall understand that large amount of data is being transmitted by seeing the file size `49.7 MB`.
- So first lets export the objects and the challenge name gives the hint as `TFTP`.
- So lets export the 'TFTP' objects.
- We shall see that several files are being transmitted.

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/Pico21/Assets/5.png?raw=true)

- The files were `instructions.txt`, `plan`, `program.deb`, `picture1.bmp`, `picture2.bmp`, and `picture3.bmp`.
- Lets analze each file.

### Instructions.txt

```
GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA
```

- Its ROT13 encrypted.
- Lets [decode](https://www.dcode.fr/caesar-cipher) it.

```
TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN
```

- Adding space inbetween gives,

```
TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN
```

- So as mentioned lets check the `Plan` file.

### Plan

```
VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF
```

- Its ROT13 encrypted.
- Lets [decode](https://www.dcode.fr/caesar-cipher) it.

```
IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS
```

- Adding space inbetween gives,

```
I USED THE PROGRAM AND HID IT WITH - DUEDILIGENCE. CHECK OUT THE PHOTOS
```

### Program.deb

- After extracting `program.deb` we shall find that it has the files related to `steghide`.
- So now let's use `steghide` to `analyse` the `bmp` files.
- There are `three` bmp images - `picture1.bmp` `picture2.bmp` `picture3.bmp`.
- We need a password to exctract the file if anything is hidden inside.
- In the previous file we got a hint that `I USED THE PROGRAM AND HID IT WITH-DUE DILIGENCE`.
- So `DUEDILIGENCE` is the password.
- After trying the steghide command in all three images, the flag.txt was found in the image `picture3.bmp`.  

```
steghide extract -sf picture3.bmp
```

```
Flag --> picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
```




