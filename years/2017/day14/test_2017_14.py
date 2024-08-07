import solve_2017_14 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return "flqrgnkx"

def test_count_used(puzzle_input):
    assert subject.count_used(puzzle_input) == 8108

def test_count_regions(puzzle_input):
    assert subject.count_regions(puzzle_input) == 1242

