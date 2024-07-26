import solve_2017_11 as subject
import pytest

def test_parse_lines():
    assert subject.parse_lines('se,sw,se,sw,sw') == ['se','sw','se','sw','sw']

def test_get_distance():
    assert subject.get_distance(['ne','ne','ne']) == 3
    assert subject.get_distance(['ne','ne','sw','sw']) == 0
    assert subject.get_distance(['ne','ne','s','s']) == 2
    assert subject.get_distance(['se','sw','se','sw','sw']) == 3

