import solve_2015_04 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return ["abcdef"]

@pytest.fixture
def puzzle_input2():
    return ["pqrstuv"]

def test_find_lowest_key(puzzle_input, puzzle_input2):
    assert subject.find_lowest_key(puzzle_input[0]) == 609043
    assert subject.find_lowest_key(puzzle_input2[0]) == 1048970

