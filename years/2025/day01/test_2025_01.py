import solve_2025_01 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (-1,68), (-1,30), (1,48), (-1,5), (1,60), (-1,55), (-1,1), (-1,99), (1,14), (-1,82)
    )

def test_solve(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.solve(data) == (3,6)

