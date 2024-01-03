import solve_2019_01 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        12,
        14,
        1969,
        100756
    ]

def test_part1(puzzle_input):
    assert subject.part1(puzzle_input) == 34241

def test_part2(puzzle_input):
    assert subject.part2(puzzle_input) == 51316

