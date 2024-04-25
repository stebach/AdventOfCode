import solve_2022_17 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        1,1,1,-1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,
    )

def test_get_height_after_number_of_rocks(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.get_height_after_number_of_rocks(data, 2022) == 3068
    assert subject.get_height_after_number_of_rocks(data, 1_000_000_000_000) == 1514285714288

