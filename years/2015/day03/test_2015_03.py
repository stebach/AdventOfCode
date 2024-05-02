import solve_2015_03 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return ['^>v<']

@pytest.fixture
def puzzle_input2():
    return ['^v^v^v^v^v']

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input))[0] == [
        (0,-1),
        (1,0),
        (0,1),
        (-1,0),
    ]


def test_number_of_houses(puzzle_input, puzzle_input2):
    data = tuple(map(subject.parse_line, puzzle_input))
    data2 = tuple(map(subject.parse_line, puzzle_input2))
    assert subject.number_of_houses(data[0]) == 4
    assert subject.number_of_houses(data2[0]) == 2
    assert subject.number_of_houses(data[0], True) == 3
    assert subject.number_of_houses(data2[0], True) == 11

