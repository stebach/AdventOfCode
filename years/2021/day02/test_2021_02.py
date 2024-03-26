import solve_2021_02 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2"
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ("forward",  5),
        ("down",  5),
        ("forward",  8),
        ("up",  3),
        ("down",  8),
        ("forward",  2)
    )

def test_get_horizontal_position(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_horizontal_position(data) == 150

def test_get_horizontal_position_using_aim(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_horizontal_position_using_aim(data) == 900



