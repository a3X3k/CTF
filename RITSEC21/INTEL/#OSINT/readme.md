# #OSINTChallenge

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/RITSEC21/Assets/14.png?raw=true)

 - From the challange we shall understand that we need to look into her [Twitter](https://twitter.com/joanne_turner_f/with_replies) account.

```
Where was she when she took the photo in her Twitter background?
```

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/RITSEC21/Assets/15.png?raw=true)

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/RITSEC21/Assets/12.png?raw=true)

- From the description we shall get some hint. 
- **Hint 1** `local`.
- Her locality is `Rochester`.
- **Hint 2** `She loves art and nature`.
- So it must be a nature park or some environment related spot.
- We shall see peace symbol in her background.
- So searching for `Peace symbol nature park in Rochester` gave the **Peace Sign Garden Durand Eastman Park**.
- Google Maps --> [Peace Sign Garden Durand Eastman Park](https://maps.google.com/?cid=5616891822005491354&entry=gps)
- I found the same photo in her background.

![bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/RITSEC21/Assets/13.png?raw=true)

- So the flag should be either `Durand_Eastman_Park` or `Peace_Sign_Garden_Durand_Eastman_Park`.

```
Flag --> RE{Durand_Eastman_Park}
```


