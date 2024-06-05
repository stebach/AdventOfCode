import solve_2016_14 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return "abc"

def test_find_keys(puzzle_input):
    assert subject.find_keys(puzzle_input)[63][0] == 22728
    assert subject.find_keys(puzzle_input, True)[63][0] == 22551


