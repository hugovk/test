from PIL import Image
Image.open('test2.gif').save('somefile.png', 'PNG')

im2 = Image.open('somefile.png')
im2.thumbnail((10, 10))