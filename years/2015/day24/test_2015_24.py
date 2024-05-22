import solve_2015_24 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return (
        1,2,3,4,5,7,8,9,10,11
    )

def test_get_lowest_quantum_entanglement(puzzle_input):
    assert subject.get_lowest_quantum_entanglement(puzzle_input) == 99
    assert subject.get_lowest_quantum_entanglement(puzzle_input, 4) == 44

