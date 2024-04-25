import solve_2022_20 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return (
        1,2,-3,3,-2,0,4
    )

def test_decrypt(puzzle_input):
    assert subject.decrypt(puzzle_input) == 3
    assert subject.decrypt(puzzle_input, 811589153, 10) == 1623178306


