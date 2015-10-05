#!/usr/bin/env python
print(123)

from django.core.files.images import ImageFile
path = 'test-placeholder.png'
im = ImageFile(open(path, 'rb'))
print(im.height)

print(123)
