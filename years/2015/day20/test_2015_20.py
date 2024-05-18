import solve_2015_20 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [70]

def test_get_delivered_gifts():
    assert subject.get_delivered_gifts(1) == 10
    assert subject.get_delivered_gifts(2) == 30
    assert subject.get_delivered_gifts(3) == 40
    assert subject.get_delivered_gifts(4) == 70
    assert subject.get_delivered_gifts(5) == 60
    assert subject.get_delivered_gifts(6) == 120
    assert subject.get_delivered_gifts(7) == 80
    assert subject.get_delivered_gifts(8) == 150
    assert subject.get_delivered_gifts(9) == 130
    
def test_get_lowest_house(puzzle_input):
    assert subject.get_lowest_house(puzzle_input[0], False, 2) == 4


