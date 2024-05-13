import solve_2015_17 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return (20, 15, 10, 5, 5)

def test_get_combinations(puzzle_input):
    assert subject.get_combinations(puzzle_input, 25) == [[20,5], [20,5], [15, 10], [15, 5, 5]]
