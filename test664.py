from PIL import Image
im = Image.open('test2.gif')
im.save('somefile.png', 'PNG')
im.thumbnail((10, 10))

im2 = Image.open('somefile.png')
im2.thumbnail((10, 10))
im2.save('somefile2.png', 'PNG')
