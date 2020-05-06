import sys

print(sys.version)
import ujson

print(ujson.__version__)
print(ujson.dumps([{"key": "value"}, 81, True]))