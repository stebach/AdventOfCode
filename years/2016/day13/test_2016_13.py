import solve_2016_13 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return 10

def test_find_route(puzzle_input):
    assert subject.find_route((1,1),(7,4),puzzle_input) == 11


