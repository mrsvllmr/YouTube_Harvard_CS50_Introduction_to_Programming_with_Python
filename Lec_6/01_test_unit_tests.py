from Lec_6.unittests import square
import pytest


def main():
    test_square()


def test_square():
    assert square(3) == 9
    assert square(2) == 4
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0


# divide them into separate functions to get better feedback
def test_positive():
    assert square(3) == 9
    assert square(2) == 4


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")


if __name__ == "__main__":
    main()


# call it via "pytest filename.py"
# pytest itself takes care of try..except etc. - just define assertions
# make sure your functions return values - only they can be tested (no prints)