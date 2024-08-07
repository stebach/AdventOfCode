import solve_2017_15 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'Generator A starts with 65',
        'Generator B starts with 8921'
    ]

def test_parse_line(puzzle_input):
    assert list(map(subject.parse_line, puzzle_input)) == [65,8921]

def test_get_count(puzzle_input):
    data = list(map(subject.parse_line, puzzle_input))
    assert subject.get_count(data) == 588
    assert subject.get_count(data, 5_000_000, True) == 309


