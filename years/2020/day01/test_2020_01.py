import solve_2020_01 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        1721,
        979,
        366,
        299,
        675,
        1456
    ]

def test_find_sum(puzzle_input):
    assert subject.find_sum(puzzle_input, 2020) == (1721, 299)
    assert subject.find_sum(puzzle_input, 2020, True)  == (979, 366, 675)

