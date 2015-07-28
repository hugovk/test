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
            doc["username"] = os.environ['PYLAST_USERNAME'].strip()
        except KeyError:
            print("username")
        try:
            doc["password_hash"] = os.environ['PYLAST_PASSWORD_HASH'].strip()
        except KeyError:
            print("hash")
        try:
            doc["api_key"] = os.environ['PYLAST_API_KEY'].strip()
        except KeyError:
            print("key")
        try:
            doc["api_secret"] = os.environ['PYLAST_API_SECRET'].strip()
        except KeyError:
            print("secret")
        try:
            doc["username"] = os.environ['PYLAST_USERNAME'].strip()
            doc["password_hash"] = os.environ['PYLAST_PASSWORD_HASH'].strip()
            doc["api_key"] = os.environ['PYLAST_API_KEY'].strip()
            doc["api_secret"] = os.environ['PYLAST_API_SECRET'].strip()
        except KeyError:
            pytest.skip("Missing environment variables: PYLAST_USERNAME etc.")
    return doc


# @flaky(max_runs=5, min_passes=1)
class TestPyLast(unittest.TestCase):

    secrets = None

    def unix_timestamp(self):
        return int(time.time())

    def setUp(self):
        if self.__class__.secrets is None:
            self.__class__.secrets = load_secrets()

        self.username = self.__class__.secrets["username"]
        password_hash = self.__class__.secrets["password_hash"]

        API_KEY = self.__class__.secrets["api_key"]
        API_SECRET = self.__class__.secrets["api_secret"]

#         self.network = pylast.LastFMNetwork(
#             api_key=API_KEY, api_secret=API_SECRET,
#             username=self.username, password_hash=password_hash)

    def test_pass(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main(failfast=True)
