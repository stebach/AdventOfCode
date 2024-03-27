import solve_2021_07 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return ["16,1,2,0,4,2,7,1,2,14"]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        16: 1,
        1: 2,
        2: 3,
        0: 1,
        4: 1,
        7: 1,
        14: 1
    }

def test_optimal_fuel_for_alignment(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.optimal_fuel_for_alignment(data) == 37

def test_optimal_fuel_for_adjusted(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.optimal_fuel_for_alignment_adjusted(data) == 168
