import solve_2015_10 as subject
import pytest


def test_look_and_say():
    assert subject.look_and_say(1,1) == '11'
    assert subject.look_and_say(11,1) == '21'
    assert subject.look_and_say(21,1) == '1211'
    assert subject.look_and_say(1211,1) == '111221'
    assert subject.look_and_say(111221,1) == '312211'
    assert subject.look_and_say(1,5) == '312211'

