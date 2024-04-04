import datetime

try:
    y = datetime.datetime.fromisoformat("0000W25")
    print(y)
except ValueError as e:
    assert str(e) == "month must be in 1..12"
