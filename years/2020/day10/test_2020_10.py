import solve_2020_10 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return (
        16,
        10,
        15,
        5,
        1,
        11,
        7,
        19,
        6,
        12,
        4
    )

@pytest.fixture
def puzzle_input2():
    return (
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3
    )

def test_differences_when_all_are_used(puzzle_input, puzzle_input2):
    assert subject.differences_when_all_are_used(puzzle_input) == (7,0,5)
    assert subject.differences_when_all_are_used(puzzle_input2) == (22,0,10)

def test_number_of_arrangements(puzzle_input, puzzle_input2):
    assert subject.number_of_arrangements(puzzle_input) == 8
    assert subject.number_of_arrangements(puzzle_input2) == 19208


