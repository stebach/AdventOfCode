import solve_2019_04 as subject
import pytest


def test_check_password():
    assert subject.check_password(111111) == True
    assert subject.check_password(223450) == False
    assert subject.check_password(123789) == False

    assert subject.check_password(112233,True) == True
    assert subject.check_password(123444,True) == False
    assert subject.check_password(111122,True) == True


