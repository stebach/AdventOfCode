import solve_2015_01 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '(())',
        '()()',
        '(((',
        '(()(()(',
        '))(((((',
        '())',
        '))(',
        ')))',
        ')())())'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        [1,1,-1,-1,],
        [1,-1,1,-1,],
        [1,1,1,],
        [1,1,-1,1,1,-1,1,],
        [-1,-1,1,1,1,1,1,],
        [1,-1,-1,],
        [-1,-1,1,],
        [-1,-1,-1,],
        [-1,1,-1,-1,1,-1,-1,],
    )

def test_get_floor(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_floor(data[0]) == 0
    assert subject.get_floor(data[1]) == 0
    assert subject.get_floor(data[2]) == 3
    assert subject.get_floor(data[3]) == 3
    assert subject.get_floor(data[4]) == 3
    assert subject.get_floor(data[5]) == -1
    assert subject.get_floor(data[6]) == -1
    assert subject.get_floor(data[7]) == -3
    assert subject.get_floor(data[8]) == -3

def test_get_first_pos_for_basement():
    assert subject.get_first_pos_for_basement([-1]) == 1
    assert subject.get_first_pos_for_basement([1,-1,1,-1,-1]) == 5