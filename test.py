#!/usr/bin/env python
import locale
import mimetypes
import os
import sys

from tqdm import tqdm

print(123)

print(sys.version)
print(sys.platform)

for i in tqdm(range(1000)):
    pass

print("My PIN is 1234")


print(mimetypes.guess_type("filename.rtf", strict=False))
print(mimetypes.guess_type("filename.rtf", strict=True))

print(f"{os.getpid()=}")

os.environ["monty"] = "python"
print("MONTY" in os.environ)
print("monty" in os.environ)

print(locale.getlocale())
print(locale.getdefaultlocale())

locale.setlocale(locale.LC_CTYPE)
print(locale.getlocale())
print(locale.getdefaultlocale())
