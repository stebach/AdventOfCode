import solve_2020_13 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '939',
        '7,13,x,x,59,x,31,19'
    ]

@pytest.fixture
def puzzle_input2():
    return [
        '0',
        '17,x,13,19'
    ]

@pytest.fixture
def puzzle_input3():
    return [
        '0',
        '67,7,59,61'
    ]

@pytest.fixture
def puzzle_input4():
    return [
        '0',
        '67,x,7,59,61'
    ]

@pytest.fixture
def puzzle_input5():
    return [
        '0',
        '67,7,x,59,61'
    ]

@pytest.fixture
def puzzle_input6():
    return [
        '0',
        '1789,37,47,1889'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        939,
        [7,13,-1,-1,59,-1,31,19]
    )

def test_get_earliest(puzzle_input):
    assert subject.get_earliest(subject.parse_lines(puzzle_input)) == 295

def test_get_earliest_with_offsets(puzzle_input, puzzle_input2, puzzle_input3, puzzle_input4, puzzle_input5, puzzle_input6):
    assert subject.get_earliest_with_offsets(subject.parse_lines(puzzle_input)) == 1068781
    assert subject.get_earliest_with_offsets(subject.parse_lines(puzzle_input2)) == 3417
    assert subject.get_earliest_with_offsets(subject.parse_lines(puzzle_input3)) == 754018
    assert subject.get_earliest_with_offsets(subject.parse_lines(puzzle_input4)) == 779210
    assert subject.get_earliest_with_offsets(subject.parse_lines(puzzle_input5)) == 1261476
    assert subject.get_earliest_with_offsets(subject.parse_lines(puzzle_input6)) == 1202161486


