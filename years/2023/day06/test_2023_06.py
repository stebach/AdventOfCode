import solve_2023_06 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "Time:      7  15   30",
        "Distance:  9  40  200"
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == [
        [7,9],[15,40],[30,200]
    ]

def test_part1_example1(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.part1(data) == 288

def test_part2_example1(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.part2(data) == 71503
