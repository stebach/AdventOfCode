import solve_2017_24 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '0/2',
        '2/2',
        '2/3',
        '3/4',
        '3/5',
        '0/1',
        '10/1',
        '9/10'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (0,2),
        (2,2),
        (2,3),
        (3,4),
        (3,5),
        (0,1),
        (10,1),
        (9,10)
    )

def test_get_strongest(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_strongest(data) == 31
    assert subject.get_strongest(data, True) == 19

