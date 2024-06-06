import solve_2016_19 as subject
import pytest

def test_while_elephant_circle():
    assert subject.white_elephant_circle(5) == 3
    assert subject.white_elephant_circle(5, True) == 2

