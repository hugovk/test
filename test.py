#!/usr/bin/env python
import mimetypes
import sys

from tqdm import tqdm

print(123)

print(sys.version)
print(sys.platform)

for i in tqdm(range(1000)):
    pass

print("My PIN is 1234")

print(mimetypes.guess_file_type("my.xml"))
