
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

font_path = "Tests/fonts/FreeMono.ttf"
font_size=20

ttf = ImageFont.truetype(font_path, font_size)

txt = "Hello World!"
w, h = ttf.getsize(txt)
print(w, h)

img = Image.new("RGB", (256, 64), "white")
d = ImageDraw.Draw(img)
d.text((10, 10), txt, font=ttf, fill='black')

img.show()
img.save('font.png')

