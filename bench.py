# benchmark_names.py
import re
import sys
import timeit

# Get data with:
# curl -L https://github.com/pypi-data/pypi-json-data/releases/download/latest/pypi-data.sqlite.gz | gzip -d > pypi-data.sqlite
# Or ues pre-cached files from:
# https://gist.github.com/hugovk/efdbee0620cc64df7b405b52cf0b6e42

CACHE_FILE = "/tmp/bench/names.txt"
DB_FILE = "/tmp/bench/pypi-data.sqlite"

try:
    with open(CACHE_FILE) as f:
        TEST_ALL_NAMES = [line.rstrip("\n") for line in f]
except FileNotFoundError:
    TEST_ALL_NAMES = []
    import sqlite3

    with sqlite3.connect(DB_FILE) as conn:
        with open(CACHE_FILE, "w") as cache:
            for (name,) in conn.execute("SELECT name FROM projects"):
                if name:
                    TEST_ALL_NAMES.append(name)
                    cache.write(name + "\n")


_normalize_table = str.maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ-.",
    "abcdefghijklmnopqrstuvwxyz__",
)


def normalize1(name):
    return re.sub(r"[-_.]+", "-", name).lower().replace("-", "_")


def normalize2(name):
    value = name.translate(_normalize_table)
    while "__" in value:
        value = value.replace("__", "_")
    return value


def normalize3(name):
    value = name.lower().replace("_", "-").replace(".", "-")
    while "__" in value:
        value = value.replace("__", "_")
    return value


def bench(func):
    for n in TEST_ALL_NAMES:
        func(n)


if __name__ == "__main__":
    print(sys.version)

    # print(f"Loaded {len(TEST_ALL_NAMES):,} names")
    t1 = timeit.timeit("bench(normalize1)", globals=globals(), number=1)
    print(f"Time: {t1:.4f} seconds")
    t2 = timeit.timeit("bench(normalize2)", globals=globals(), number=1)
    print(f"Time: {t2:.4f} seconds")
    t3 = timeit.timeit("bench(normalize3)", globals=globals(), number=1)
    print(f"Time: {t3:.4f} seconds")

    result = f"{sys.version.split()[0]},{t1:.4f},{t2:.4f},{t3:.4f},'{sys.version}'"
    print(result)
    with open("all.csv", "a") as f:
        f.write(result + "\n")
