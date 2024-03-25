import solve_2020_23 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return ["389125467"]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == [3,8,9,1,2,5,4,6,7]

def test_do_moves(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    result = subject.do_moves(data, 100)
    assert result == [6,7,3,8,4,5,2,9]


