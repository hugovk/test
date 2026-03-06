#!/usr/bin/env python3
"""Standalone script to run test_bz2 testDecompressorChunksMaxsize."""

import bz2
import os
import unittest
from bz2 import BZ2Decompressor


# Build BIG_TEXT / BIG_DATA the same way the test suite does:
# gather ~128KB of .py files from a directory as raw bytes, then compress.
def _build_big_data():
    import glob

    # Use this script's directory (or stdlib Lib/ if available)
    # to find .py files
    search_dirs = [
        os.path.dirname(os.path.abspath(__file__)),
        os.path.dirname(os.__file__),  # stdlib location
    ]
    buf = bytearray(128 * 1024)
    size = 0
    for d in search_dirs:
        for fname in glob.glob(os.path.join(glob.escape(d), "*.py")):
            with open(fname, "rb") as fh:
                size += fh.readinto(memoryview(buf)[size:])
            if size >= 128 * 1024:
                break
        if size >= 128 * 1024:
            break
    if size == 0:
        # Fallback: generate synthetic data
        buf = os.urandom(128 * 1024)
        size = len(buf)
    big_text = bytes(buf[:size])
    big_data = bz2.compress(big_text, compresslevel=1)
    return big_text, big_data


BIG_TEXT, BIG_DATA = _build_big_data()


class TestDecompressorChunksMaxsize(unittest.TestCase):

    def test_decompressor_chunks_maxsize(self):
        bzd = BZ2Decompressor()
        max_length = 100
        out = []

        # Feed some input
        len_ = len(BIG_DATA) - 64
        out.append(bzd.decompress(BIG_DATA[:len_], max_length=max_length))
        self.assertFalse(bzd.needs_input)
        self.assertEqual(len(out[-1]), max_length)

        # Retrieve more data without providing more input
        out.append(bzd.decompress(b"", max_length=max_length))
        self.assertFalse(bzd.needs_input)
        self.assertEqual(len(out[-1]), max_length)

        # Retrieve more data while providing more input
        out.append(bzd.decompress(BIG_DATA[len_:], max_length=max_length))
        self.assertLessEqual(len(out[-1]), max_length)

        # Retrieve remaining uncompressed data
        while not bzd.eof:
            out.append(bzd.decompress(b"", max_length=max_length))
            self.assertLessEqual(len(out[-1]), max_length)

        out = b"".join(out)
        self.assertEqual(out, BIG_TEXT)
        self.assertEqual(bzd.unused_data, b"")


if __name__ == "__main__":
    unittest.main(verbosity=2)
