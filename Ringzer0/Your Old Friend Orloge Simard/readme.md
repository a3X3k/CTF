# Your Old friend Orloge Simard

- We are provided with the [`Audio`](https://github.com/a3X3k/RoadMap/blob/main/Set%201/RingZer0/Your%20Old%20Friend%20Orloge%20Simard/1.mp3) file.
- Analysing it through `Sonic Visualiser` and `Audacity` shows something suspicious.

![Image](https://github.com/a3X3k/RoadMap/blob/main/Set%201/RingZer0/Your%20Old%20Friend%20Orloge%20Simard/1.png?raw=true)

- On getting close to it, I understood that its a `Morse Code`.

- I `trimmed` the required portion and tried to [`decode`](https://morsecode.world/international/decoder/audio-decoder-adaptive.html) the `Morse mp3`.
- But I got only some random texts.
- Then I `manually decoded` it. 
- Morse Code --> [`Reference`](https://www.artofmanliness.com/articles/morse-code/)

![Image](https://github.com/a3X3k/RoadMap/blob/main/Set%201/RingZer0/Your%20Old%20Friend%20Orloge%20Simard/Ref.png?raw=true)

### Left to Right Analysis

![Image](https://github.com/a3X3k/RoadMap/blob/main/Set%201/RingZer0/Your%20Old%20Friend%20Orloge%20Simard/Morse.png?raw=true)

- Initially Decoding the first `four` characters gives `EVMN`.
- The `fifth` Character `---.` is not in the Morse Code. 
- But we have the reverse of it `.---` which corresponds to `J` in Morse Code.
- So Now I tried to decode the Morse Code in Reverse.

###  Right to Left Analysis

![Image](https://github.com/a3X3k/RoadMap/blob/main/Set%201/RingZer0/Your%20Old%20Friend%20Orloge%20Simard/Original%20Morse.png)

- This Analysis gives us the `flag`.

```
FLAGDONNEMOITAJAMBE
```
