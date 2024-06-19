import solve_2017_05 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "0",
        "3",
        "0",
        "1",
        "-3"
    ]

def test_parse_line(puzzle_input):
    assert list(map(subject.parse_line, puzzle_input)) == [0, 3, 0, 1, -3]

def test_get_jumps(puzzle_input):
    data = list(map(subject.parse_line, puzzle_input))
    assert subject.get_jumps(data) == 5
    assert subject.get_jumps(data, True) == 10
