import solve_2017_16 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return ['s1,x3/4,pe/b']

def test_parse_line(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        ('s',1),
        ('x',3,4),
        ('p','e','b'),
    )

def test_dance(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.dance(data, 5) == 'baedc'
    assert subject.dance_repeat(data, 5, 2) == 'ceadb'
