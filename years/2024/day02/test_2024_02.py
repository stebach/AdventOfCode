import solve_2024_02 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9"
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (7, 6, 4, 2, 1),
        (1, 2, 7, 8, 9),
        (9, 7, 6, 2, 1),
        (1, 3, 2, 4, 5),
        (8, 6, 4, 4, 1),
        (1, 3, 6, 7, 9)
    )

def test_is_safe(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.is_safe(data[0]) == True
    assert subject.is_safe(data[1]) == False
    assert subject.is_safe(data[2]) == False
    assert subject.is_safe(data[3]) == False
    assert subject.is_safe(data[4]) == False
    assert subject.is_safe(data[5]) == True
    assert [subject.is_safe(x) for x in data].count(True) == 2

    assert subject.is_safe(data[0], True) == True
    assert subject.is_safe(data[1], True) == False
    assert subject.is_safe(data[2], True) == False
    assert subject.is_safe(data[3], True) == True
    assert subject.is_safe(data[4], True) == True
    assert subject.is_safe(data[5], True) == True
    assert [subject.is_safe(x, True) for x in data].count(True) == 4

def test_solve(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.solve(data) == (2,4)

