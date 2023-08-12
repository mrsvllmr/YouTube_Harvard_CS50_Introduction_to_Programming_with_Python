from Lec_1 import functions
import pytest


def test_default():
    assert functions.sayhello() == "Hello, world"


def test_argument():
    assert functions.sayhello("Marius") == "Hello, Marius"

# this file has to be named 'test_*.py' or '*_test.py', as this is what pytest looks for
# otherwise running tests on the whole folder will not work