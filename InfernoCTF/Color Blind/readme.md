# Color Blind

## Approach 1

- Download the [`PNG Image`](https://github.com/a3X3k/RoadMap/blob/main/Set%204/Color%20Blind/1.png).
- Try analysing using `zsteg`.
- Lets analyse using `zsteg -a <File Name>` which gives all hidden information.

![](https://github.com/a3X3k/RoadMap/blob/main/Set%204/Color%20Blind/2.png?raw=true)

- Here we get the `flag` directly.

## Approach 2

- Using `PIL` `Library` we shall extract the `RGB` values.
- I wrote a [`script`](https://github.com/a3X3k/RoadMap/blob/main/Set%204/Color%20Blind/1.py) to `extract` the data.

```
from PIL import Image

image = Image.open('1.png')

height = image.height
width = image.width 

for i in range(width):
	for j in range(height):
		r, g, b = image.getpixel((i, j))
		print("{}{}{}".format(chr(r),chr(g),chr(b)),end="")
```

## Output

```
blahblahblah_hello_how_are_you_today_i_hope_you_are_not_doing_this_manually_infernoCTF{h3y_100k_y0u_4r3_n07_h3x_bl1nD_:O}_doing_this_manually_would_be_a_bad_idea_you_shouldnt_do_it_manually_ok
```

```
infernoCTF{h3y_100k_y0u_4r3_n07_h3x_bl1nD_:O}
```

