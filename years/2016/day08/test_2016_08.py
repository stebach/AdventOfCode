import solve_2016_08 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'rect 3x2',
        'rotate column x=1 by 1',
        'rotate row y=0 by 4',
        'rotate column x=1 by 1'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('rect',3,2),
        ('rotate',1,1,1),
        ('rotate',0,0,4),
        ('rotate',1,1,1)
    )

def test_count_lit(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.count_lit(data) == 6

def test_draw(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.draw(data, 7, 3) == ' █  █ █\n█ █    \n █     '
