import solve_2022_08 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '30373',
        '25512',
        '65332',
        '33549',
        '35390'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (3,0,3,7,3),
        (2,5,5,1,2),
        (6,5,3,3,2),
        (3,3,5,4,9),
        (3,5,3,9,0)
    )

def test_visible_trees(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.visible_trees(data) == 21

def test_scenic_score(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.scenic_score(data) == 8


