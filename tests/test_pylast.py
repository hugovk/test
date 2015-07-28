#!/usr/bin/env python
"""
Integration (not unit) tests for pylast.py
"""
# from flaky import flaky
import os
import pytest
# from random import choice
# import time
import unittest

# import pylast


def load_secrets():
    secrets_file = "test_pylast.yaml"
    if os.path.isfile(secrets_file):
        import yaml  # pip install pyyaml
        with open(secrets_file, "r") as f:  # see example_test_pylast.yaml
            doc = yaml.load(f)
    else:
        doc = {}
        try:
            doc["my_var"] = os.environ['MY_VAR'].strip()
        except KeyError:
            print("my_var")
            pytest.skip("Missing environment variables: MY_VAR etc.")
    return doc


# @flaky(max_runs=5, min_passes=1)
class TestPyLast(unittest.TestCase):

    secrets = None

    def unix_timestamp(self):
        return int(time.time())

    def setUp(self):
        if self.__class__.secrets is None:
            self.__class__.secrets = load_secrets()

        MY_VAR = self.__class__.secrets["my_var"]

    def test_pass(self):
        print(MY_VAR)
        self.assertEqual(1, 1)
        self.assertEqual(MY_VAR, "this_is_my_var")


if __name__ == '__main__':
    unittest.main(failfast=True)
