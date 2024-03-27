import solve_2021_06 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "3,4,3,1,2"
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        3: 2,
        4: 1,
        1: 1,
        2: 1
    }

def test_grow(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.grow(data, 18) == 26
    assert subject.grow(data, 80) == 5934
    assert subject.grow(data, 256) == 26984457539

