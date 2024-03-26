import solve_2021_01 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263
    ]

def test_get_increases(puzzle_input):
    assert subject.get_increases(puzzle_input) == 7
    assert subject.get_increases(puzzle_input, 3) == 5
