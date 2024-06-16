import solve_2017_01 as subject
import pytest

def test_captcha():
    assert subject.captcha("1122") == 3
    assert subject.captcha("1111") == 4
    assert subject.captcha("1234") == 0
    assert subject.captcha("91212129") == 9

    assert subject.captcha("1212", True) == 6
    assert subject.captcha("1221", True) == 0
    assert subject.captcha("123425", True) == 4
    assert subject.captcha("123123", True) == 12
    assert subject.captcha("12131415", True) == 4
