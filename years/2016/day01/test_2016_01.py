import solve_2016_01 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "R2, L3"
    ]

@pytest.fixture
def puzzle_input2():
    return [
        "R5, L5, R5, R3"
    ]

@pytest.fixture
def puzzle_input3():
    return [
        "R8, R4, R4, R8"
    ]



def test_parse_lines(puzzle_input, puzzle_input2):
    assert subject.parse_lines(puzzle_input) == ("R", 2, "L", 3)
    assert subject.parse_lines(puzzle_input2) == ("R", 5, "L", 5, "R", 5, "R", 3)

def test_distance(puzzle_input, puzzle_input2, puzzle_input3):
    data = subject.parse_lines(puzzle_input)
    assert subject.distance(data) == 5
    data = subject.parse_lines(puzzle_input2)
    assert subject.distance(data) == 12
    data = subject.parse_lines(puzzle_input3)
    assert subject.distance(data, True) == 4

