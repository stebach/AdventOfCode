import solve_2017_06 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "0	2	7	0"
    ]

def test_parse_line(puzzle_input):
    assert list(map(subject.parse_line, puzzle_input))[0] == [0,2,7,0]

def test_loop_size(puzzle_input):
    data = list(map(subject.parse_line, puzzle_input))[0]
    assert subject.loop_size(data) == 5
    assert subject.loop_size(data, True) == 4
