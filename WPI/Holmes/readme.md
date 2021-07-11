# Holmes

![](https://github.com/a3X3k/Bi0s/blob/master/CTFs/WPI/Holmes/1.png?raw=true)

- We are given with Base64 encoded text.
- So we shall [`Decode`](https://www.base64decode.org/) it.

```
Z29vZCB0aG91Z2h0LCBidXQgbm8u

good thought, but no.
```

- Its a `rabbit hole`.
- So there is no file with this challenge - it's more of an OSINT challenge
- The challenge name is a good hint - `sherlock Holmes`.
- Since its given in `Forensics` I have gone through out the internet and finally ended up in the [`Sherlock - Project`](https://github.com/sherlock-project/sherlock).
- This is a tool to `Hunt down social media accounts by username across social networks`.
- Clone the repo and try with the text given.

### Installation

```
# clone the repo
$ git clone https://github.com/sherlock-project/sherlock.git

# change the working directory to sherlock
$ cd sherlock

# install the requirements
$ python3 -m pip install -r requirements.txt
```

### Usage

```
python3 sherlock <User Name>

python3 sherlock Z29vZCB0aG91Z2h0LCBidXQgbm8u
```

![](https://github.com/a3X3k/Bi0s/blob/master/CTFs/WPI/Holmes/2.png?raw=true)

```
[*] Checking username Z29vZCB0aG91Z2h0LCBidXQgbm8u on:
[+] Cent: https://beta.cent.co/@Z29vZCB0aG91Z2h0LCBidXQgbm8u
[+] Chess: https://www.chess.com/member/Z29vZCB0aG91Z2h0LCBidXQgbm8u
[+] GitHub: https://www.github.com/Z29vZCB0aG91Z2h0LCBidXQgbm8u
[+] NameMC (Minecraft.net skins): https://namemc.com/profile/Z29vZCB0aG91Z2h0LCBidXQgbm8u
[+] ProductHunt: https://www.producthunt.com/@Z29vZCB0aG91Z2h0LCBidXQgbm8u
[+] Steamid: https://steamid.uk/profile/Z29vZCB0aG91Z2h0LCBidXQgbm8u
[+] Twitter: https://mobile.twitter.com/Z29vZCB0aG91Z2h0LCBidXQgbm8u
```

- We shall get all the social handles with same username.
- In this [`Git Repo`](https://www.github.com/Z29vZCB0aG91Z2h0LCBidXQgbm8u) with the same username has the flag.

[`Git Repo --> Flag`](https://github.com/Z29vZCB0aG91Z2h0LCBidXQgbm8u/flag)

```
Flag  --> WPI{sh3rlock_holmes_w0uld_be_pr0ud}
```

