from PIL import Image
im = Image.open('test2.gif')
im.save('testfile.png', 'PNG')
im2 = Image.open('testfile.png')
print im2.info
# {'transparency': 255}
im3 = im2.convert('RGBA')
print im3
# <PIL.Image.Image image mode=RGBA size=10x9 at 0x10C014B00>
print im3.info
# {'transparency': 255}
