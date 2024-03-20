import solve_2020_17 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '.#.',
        '..#',
        '###'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        (1,0,0,0),
        (2,1,0,0),
        (0,2,0,0),
        (1,2,0,0),
        (2,2,0,0),
    )

def test_run_cycles(puzzle_input):
    assert subject.run_cycles(subject.parse_lines(puzzle_input), 1) == 11
    assert subject.run_cycles(subject.parse_lines(puzzle_input), 2) == 21
    assert subject.run_cycles(subject.parse_lines(puzzle_input), 3) == 38
    assert subject.run_cycles(subject.parse_lines(puzzle_input), 6) == 112
    assert subject.run_cycles(subject.parse_lines(puzzle_input), 1, True) == 29
    assert subject.run_cycles(subject.parse_lines(puzzle_input), 2, True) == 60
    assert subject.run_cycles(subject.parse_lines(puzzle_input), 6, True) == 848
