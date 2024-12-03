import solve_2024_03 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'

def test_add_up_mul(puzzle_input):
    assert subject.add_up_mul(puzzle_input) == 161
    assert subject.add_up_mul(puzzle_input, True) == 48

def test_solve(puzzle_input):
    assert subject.solve(puzzle_input) == (161,48)

