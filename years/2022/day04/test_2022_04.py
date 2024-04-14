import solve_2022_04 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8"
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ((2,4),(6,8)),
        ((2,3),(4,5)),
        ((5,7),(7,9)),
        ((2,8),(3,7)),
        ((6,6),(4,6)),
        ((2,6),(4,8)),
    )

def test_find_fully_contained(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.find_fully_contained(data) == 2

def test_find_overlapping(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.find_overlapping(data) == 4
