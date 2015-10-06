#!/usr/bin/env python

from PIL import ImageFile as PillowImageFile

print(PillowImageFile.LOAD_TRUNCATED_IMAGES)
PillowImageFile.LOAD_TRUNCATED_IMAGES = True
print(PillowImageFile.LOAD_TRUNCATED_IMAGES)

import zlib

def get_image_dimensions(file_or_path, close=False):
    p = PillowImageFile.Parser()

    if hasattr(file_or_path, 'read'):
        file = file_or_path
        file_pos = file.tell()
        file.seek(0)
    else:
        file = open(file_or_path, 'rb')
        close = True
    try:
        # Most of the time Pillow only needs a small chunk to parse the image
        # and get the dimensions, but with some TIFF files Pillow needs to
        # parse the whole file.
        chunk_size = 1024
        while 1:
            data = file.read(chunk_size)
            if not data:
                break
            try:
                p.feed(data)
            except zlib.error as e:
                # ignore zlib complaining on truncated stream, just feed more
                # data to parser (ticket #19457).
                if e.args[0].startswith("Error -5"):
                    pass
                else:
                    raise
            if p.image:
                return p.image.size
            chunk_size *= 2
        return None
    finally:
        if close:
            file.close()
        else:
            file.seek(file_pos)

size = get_image_dimensions('test-placeholder.png')
print(size)
assert(size == (23, 22))


