#!/usr/bin/env python

from PIL import Image

im = Image.open("lena.ppm").convert("I")

im.point(list(range(256))*256, 'L')
