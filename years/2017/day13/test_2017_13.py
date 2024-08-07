import solve_2017_13 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '0: 3',
        '1: 2',
        '4: 4',
        '6: 4'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        [0, 3],
        [1, 2],
        [4, 4],
        [6, 4],
    )

def test_get_severity(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_severity(data) == 24

def test_get_fewest_wait_without_getting_caught(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_fewest_wait_without_getting_caught(data) == 10


