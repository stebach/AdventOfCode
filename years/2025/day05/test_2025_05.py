import solve_2025_05 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return ['3-5', '10-14', '16-20', '12-18', '', '1', '5', '8', '11', '17', '32']

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'ranges': [(3, 5), (10, 14), (16, 20), (12, 18)],
        'ingredients': [1, 5, 8, 11, 17, 32]
    }

def test_solve(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.solve(data) == (3,14)

