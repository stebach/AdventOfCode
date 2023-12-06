import solve_2018_05 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [1, 2, 3]


def test_reduce():
    assert subject.reduce("aA") == ""
    assert subject.reduce("abBA") == ""
    assert subject.reduce("abAB") == "abAB"
    assert subject.reduce("aabAAB") == "aabAAB"
    assert subject.reduce("dabAcCaCBAcCcaDA") == "dabCBAcaDA"

def test_part1_example1():
    assert subject.part1("dabAcCaCBAcCcaDA") == 10

def test_part2_example1():
    assert subject.part2("dabAcCaCBAcCcaDA") == 4

