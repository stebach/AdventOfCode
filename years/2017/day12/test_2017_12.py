import solve_2017_12 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '0 <-> 2',
        '1 <-> 1',
        '2 <-> 0, 3, 4',
        '3 <-> 2, 4',
        '4 <-> 2, 3, 6',
        '5 <-> 6',
        '6 <-> 4, 5'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (0, (2,)),
        (1, (1,)),
        (2, (0, 3, 4)),
        (3, (2, 4)),
        (4, (2, 3, 6)),
        (5, (6,)),
        (6, (4, 5)),
    )

def test_count_connections(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.count_connections(data, 0) == 6


def test_count_groups(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.count_groups(data) == 2
