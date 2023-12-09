import solve_2023_09 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return tuple(map(subject.parse_line, [
        "0 3 6 9 12 15",
        "1 3 6 10 15 21",
        "10 13 16 21 30 45"
    ]))

def test_part1_example1(puzzle_input):
    assert subject.part1(puzzle_input) == 114

def test_part2_example1(puzzle_input):
    assert subject.part2(puzzle_input) == 2

