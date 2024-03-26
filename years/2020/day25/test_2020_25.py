import solve_2020_25 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        5764801,
        17807724
    ]

def test_get_loopsizes(puzzle_input):
    assert subject.get_loopsizes(puzzle_input) == [8,11]

def test_run_loop():
    assert subject.run_loop(1, 7, 8) == 5764801
    assert subject.run_loop(1, 7, 11) == 17807724
    assert subject.run_loop(1, 5764801, 11) == 14897079
    assert subject.run_loop(1, 17807724, 8) == 14897079

def test_get_encryption_key(puzzle_input):
    assert subject.get_encryption_key(puzzle_input) == 14897079

