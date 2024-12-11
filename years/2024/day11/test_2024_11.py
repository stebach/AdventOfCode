import solve_2024_11 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return ['125 17']

def test_parse_line(puzzle_input):
    assert list(map(subject.parse_line, puzzle_input)) == [[125, 17]]

def test_number_of_stones(puzzle_input):
    data = list(map(subject.parse_line, puzzle_input))
    assert subject.number_of_stones(data[0], 25) == 55312

def test_solve(puzzle_input):
    data = list(map(subject.parse_line, puzzle_input))
    assert subject.solve(data[0]) == (55312, 65601038650482)

