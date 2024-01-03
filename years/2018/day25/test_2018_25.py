import solve_2018_25 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '0,0,0,0',
        '3,0,0,0',
        '0,3,0,0',
        '0,0,3,0',
        '0,0,0,3',
        '0,0,0,6',
        '9,0,0,0',
        '12,0,0,0'
    ]

@pytest.fixture
def puzzle_input2():
    return [
        '-1,2,2,0',
        '0,0,2,-2',
        '0,0,0,-2',
        '-1,2,0,0',
        '-2,-2,-2,2',
        '3,0,2,-1',
        '-1,3,2,2',
        '-1,0,-1,0',
        '0,2,1,-2',
        '3,0,0,0'
    ]

@pytest.fixture
def puzzle_input3():
    return [
        '1,-1,0,1',
        '2,0,-1,0',
        '3,2,-1,0',
        '0,0,3,1',
        '0,0,-1,-1',
        '2,3,-2,0',
        '-2,2,0,0',
        '2,-2,0,-1',
        '1,-1,0,-1',
        '3,2,0,2'
    ]

@pytest.fixture
def puzzle_input4():
    return [
        '1,-1,-1,-2',
        '-2,-2,0,1',
        '0,2,1,3',
        '-2,3,-2,1',
        '0,2,3,-2',
        '-1,-1,1,-2',
        '0,-2,-1,0',
        '-2,2,3,-1',
        '1,2,2,0',
        '-1,-2,0,-2'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (0,0,0,0),
        (3,0,0,0),
        (0,3,0,0),
        (0,0,3,0),
        (0,0,0,3),
        (0,0,0,6),
        (9,0,0,0),
        (12,0,0,0)

    )

def test_part1_example1(puzzle_input, puzzle_input2, puzzle_input3, puzzle_input4):
    assert subject.part1(tuple(map(subject.parse_line, puzzle_input))) == 2
    assert subject.part1(tuple(map(subject.parse_line, puzzle_input2))) == 4
    assert subject.part1(tuple(map(subject.parse_line, puzzle_input3))) == 3
    assert subject.part1(tuple(map(subject.parse_line, puzzle_input4))) == 8

