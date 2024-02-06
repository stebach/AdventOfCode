import solve_2020_15 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [1, 3, 2]

@pytest.fixture
def puzzle_input2():
    return [2, 1, 3]

@pytest.fixture
def puzzle_input3():
    return [1, 2, 3]

@pytest.fixture
def puzzle_input4():
    return [2, 3, 1]

@pytest.fixture
def puzzle_input5():
    return [3, 2, 1]

@pytest.fixture
def puzzle_input6():
    return [3, 1, 2]


def test_nth_number(puzzle_input, puzzle_input2, puzzle_input3, puzzle_input4, puzzle_input5, puzzle_input6):
    assert subject.nth_number(puzzle_input, 2020) == 1
    assert subject.nth_number(puzzle_input2, 2020) == 10
    assert subject.nth_number(puzzle_input3, 2020) == 27
    assert subject.nth_number(puzzle_input4, 2020) == 78
    assert subject.nth_number(puzzle_input5, 2020) == 438
    assert subject.nth_number(puzzle_input6, 2020) == 1836


