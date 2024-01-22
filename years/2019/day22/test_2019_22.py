import solve_2019_22 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "deal with increment 7",
        "deal into new stack",
        "deal into new stack"
    ]

@pytest.fixture
def puzzle_input2():
    return [
        "cut 6",
        "deal with increment 7",
        "deal into new stack"
    ]

@pytest.fixture
def puzzle_input3():
    return [
        "deal with increment 7",
        "deal with increment 9",
        "cut -2"
    ]

@pytest.fixture
def puzzle_input4():
    return [
        "deal into new stack",
        "cut -2",
        "deal with increment 7",
        "cut 8",
        "cut -4",
        "deal with increment 7",
        "cut 3",
        "deal with increment 9",
        "deal with increment 3",
        "cut -1"
    ]

def test_parse_line(puzzle_input, puzzle_input2, puzzle_input3, puzzle_input4):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ("increment", 7),
        ("deal",),
        ("deal",)
    )
    assert tuple(map(subject.parse_line, puzzle_input2)) == (
        ("cut", 6),
        ("increment", 7),
        ("deal",)
    )
    assert tuple(map(subject.parse_line, puzzle_input3)) == (
        ("increment", 7),
        ("increment", 9),
        ("cut", -2)
    )
    assert tuple(map(subject.parse_line, puzzle_input4)) == (
        ("deal",),
        ("cut", -2),
        ("increment", 7),
        ("cut", 8),
        ("cut", -4),
        ("increment", 7),
        ("cut", 3),
        ("increment", 9),
        ("increment", 3),
        ("cut", -1)
    )

def test_solve(puzzle_input, puzzle_input2, puzzle_input3, puzzle_input4):
    assert subject.find_position(10,9,1,tuple(map(subject.parse_line, puzzle_input))) == 3
    assert subject.find_position(10,4,1,tuple(map(subject.parse_line, puzzle_input2))) == 3
    assert subject.find_position(10,7,1,tuple(map(subject.parse_line, puzzle_input3))) == 3
    assert subject.find_position(10,8,1,tuple(map(subject.parse_line, puzzle_input4))) == 3

