# Elizabeth is Missing

- We are provided with the [`PDF`](https://github.com/a3X3k/Bi0s/blob/master/CTFs/TAMU/Assets/eowens%20flyer.pdf).

![](https://github.com/a3X3k/Bi0s/blob/master/CTFs/TAMU/Assets/1.png?raw=true)

- Here we can see deci mal.
- [`Decode`](https://convert.town/ascii-to-text) it to ASCII.

```
72 101 121 33 32 73 39 109 32 104 111 115 116 105 110 103 32 97 32 114 101 116 114 101 97 
116 32 102 111 114 32 109 121 32 99 108 105 101 110 116 115 32 115 111 32 73 39 108 108 32 
98 101 32 111 102 102 32 116 104 101 32 103 114 105 100 32 102 111 114 32 97 119 104 105 
108 101 32 45 32 73 32 103 111 116 32 97 32 110 101 119 32 112 104 111 110 101 32 110 117 
109 98 101 114 44 32 115 111 32 99 97 108 108 32 109 101 32 105 102 32 121 111 117 32 110 
101 101 100 32 97 110 121 116 104 105 110 103 32 40 57 55 57 41 52 50 57 45 50 49 55 54 46

Hey! I'm hosting a retreat for my clients so I'll be off the grid for awhile - I got a new phone number, so call me if you need anything (979)429-2176.
```

- We are provided with Mobile Number.
- I spent more than 5 hours in tracing out in different Police FIR's and tried to OSINT with the name `ELIZABETH OWENS`.
- My last hope was to call the number.
- Since its a international dialing, I have used [`Free Calls - International Phone Calling App`](https://play.google.com/store/apps/details?id=com.whatsphone.messenger.im) for free dialing.
- You get 10 credits depending on App. 
- I understood that its a voice mail. 
- So I called again with recording on. 
- Then I played the audio thrice to understand.
- Thats basically the `https` link [`Eowensphotography`](eowensphotography.weebly.com).
- Paste it in URL bar and OSINT the site. 
- You will see the section `Where Am I?`. 
- There you will get the flag.

```
Flag --> gigem{3_0W3N5}
```
