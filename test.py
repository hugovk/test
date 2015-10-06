#!/usr/bin/env python

from django.core.files.images import ImageFile
path = 'test-placeholder.png'
im = ImageFile(open(path, 'rb'))
print(im.height)
assert(im.height == 22)

