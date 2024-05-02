import solve_2015_02 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '2x3x4',
        '1x1x10',
        '4x3x2',
        '1x10x1',
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (2,3,4),
        (1,1,10),
        (2,3,4),
        (1,1,10),
    )

def test_square_feet_wrapping_paper(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.square_feet_wrapping_paper(data) == 202

def test_feet_ribbon(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.feet_ribbon(data) == 96