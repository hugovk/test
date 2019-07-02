#!/usr/bin/env python
import pytest

print(123)

def test_ok():
    assert True

@pytest.mark.skip(reason="skip it")
def test_skip():
    assert False
