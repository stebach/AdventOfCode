import solve_2024_22 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return (
        1,
        10,
        100,
        2024
    )

@pytest.fixture
def puzzle_input2():
    return (
        1,
        2,
        3,
        2024
    )

def test_secret_number(puzzle_input):
    assert subject.secret_number(puzzle_input[0], 2000) == 8685429
    assert subject.secret_number(puzzle_input[1], 2000) == 4700978
    assert subject.secret_number(puzzle_input[2], 2000) == 15273692
    assert subject.secret_number(puzzle_input[3], 2000) == 8667524
    assert sum([subject.secret_number(x, 2000) for x in puzzle_input]) == 37327623

def test_get_most_bananas_by_sequence(puzzle_input2):
    assert subject.get_most_bananas_by_sequence(puzzle_input2) == 23


