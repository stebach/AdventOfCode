import solve_2018_06 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "1, 1",
        "1, 6",
        "8, 3",
        "3, 4",
        "5, 5",
        "8, 9"
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == tuple([[1, 1], [1, 6], [8, 3], [3, 4], [5, 5], [8, 9]])

def test_part1_example1(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.part1(data) == 17

def test_part2_example1(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.part2(data, 32) == 16

