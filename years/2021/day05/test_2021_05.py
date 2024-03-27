import solve_2021_05 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2"
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ((0, 9), (5, 9)),
        ((8, 0), (0, 8)),
        ((9, 4), (3, 4)),
        ((2, 2), (2, 1)),
        ((7, 0), (7, 4)),
        ((6, 4), (2, 0)),
        ((0, 9), (2, 9)),
        ((3, 4), (1, 4)),
        ((0, 0), (8, 8)),
        ((5, 5), (8, 2))
    )

def test_get_overlaps(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_overlaps(data, 2) == 5
    assert subject.get_overlaps(data, 2, True) == 12

