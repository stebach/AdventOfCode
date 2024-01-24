import solve_2020_09 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576
    ]

def test_find_first_invalid(puzzle_input):
    assert subject.find_first_invalid(puzzle_input, 5) == 127

def test_find_continous(puzzle_input):
    assert subject.find_continous(puzzle_input, 127) == [15,25,47,40]


