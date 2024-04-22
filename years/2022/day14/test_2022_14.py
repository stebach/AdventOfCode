import solve_2022_14 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "498,4 -> 498,6 -> 496,6",
        "503,4 -> 502,4 -> 502,9 -> 494,9"
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == set([
        (498,4),
        (498,5),
        (498,6),
        (497,6),
        (496,6),
        (503,4),
        (502,4),
        (502,5),
        (502,6),
        (502,7),
        (502,8),
        (502,9),
        (501,9),
        (500,9),
        (499,9),
        (498,9),
        (497,9),
        (496,9),
        (495,9),
        (494,9),
    ])

def test_run_sand(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    result = subject.run_sand(data)
    assert result[0] == 24
    assert result[1] == 93
