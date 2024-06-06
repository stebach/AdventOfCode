import solve_2016_20 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '5-8',
        '0-2',
        '4-7'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (5,8),
        (0,2),
        (4,7),
    )

def test_get_lowset(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_lowest(data) == 3

def test_count_allowed(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.count_allowed(data, 9) == 2


