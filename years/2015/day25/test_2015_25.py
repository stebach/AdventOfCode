import solve_2015_25 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'To continue, please consult the code grid in the manual.  Enter the code at row 6, column 5.'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (5,6)

def test_get_code(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.get_code(data) == 1534922

