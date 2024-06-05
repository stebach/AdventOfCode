import solve_2016_15 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'Disc #1 has 5 positions; at time=0, it is at position 4.',
        'Disc #2 has 2 positions; at time=0, it is at position 1.'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (5, 4),
        (2, 1),
    )

def test_find_time(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.find_time(data) == 5


