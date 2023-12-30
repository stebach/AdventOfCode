import solve_2018_22 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'depth: 510',
        'target: 10,10'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (510,10,10)

def test_part1_example1(puzzle_input):
    assert subject.part1(subject.parse_lines(puzzle_input)) == 114

def test_part2_example1(puzzle_input):
    assert subject.part2(subject.parse_lines(puzzle_input)) == 45
