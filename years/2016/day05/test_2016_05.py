import solve_2016_05 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return 'abc'

def test_find_password(puzzle_input):
    assert subject.find_password(puzzle_input) == ('18f47a30','05ace8e3') 
