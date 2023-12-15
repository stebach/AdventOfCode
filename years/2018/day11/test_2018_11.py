import solve_2018_11 as subject
import pytest

def test_power_level():
    assert subject.power_level(3,5,8) == 4
    assert subject.power_level(122,79,57) == -5
    assert subject.power_level(217,196,39) == 0
    assert subject.power_level(101,153,71) == 4

def test_part1_example1():
    assert subject.part1(18) == (33,45)
    assert subject.part1(42) == (21,61)


