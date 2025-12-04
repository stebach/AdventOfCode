import solve_2025_04 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return ['..@@.@@@@.','@@@.@.@.@@','@@@@@.@.@@','@.@@@@..@.','@@.@@@@.@@','.@@@@@@@.@','.@.@.@.@@@','@.@@@.@@@@','.@@@@@@@@.','@.@.@@@.@.']

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (0,0,1,1,0,1,1,1,1,0),
        (1,1,1,0,1,0,1,0,1,1),
        (1,1,1,1,1,0,1,0,1,1),
        (1,0,1,1,1,1,0,0,1,0),
        (1,1,0,1,1,1,1,0,1,1),
        (0,1,1,1,1,1,1,1,0,1),
        (0,1,0,1,0,1,0,1,1,1),
        (1,0,1,1,1,0,1,1,1,1),
        (0,1,1,1,1,1,1,1,1,0),
        (1,0,1,0,1,1,1,0,1,0)
    )


def test_solve(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.solve(data) == (13, 43)

