import solve_2018_23 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'pos=<0,0,0>, r=4',
        'pos=<1,0,0>, r=1',
        'pos=<4,0,0>, r=3',
        'pos=<0,2,0>, r=1',
        'pos=<0,5,0>, r=3',
        'pos=<0,0,3>, r=1',
        'pos=<1,1,1>, r=1',
        'pos=<1,1,2>, r=1',
        'pos=<1,3,1>, r=1'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (0,0,0,4),
        (1,0,0,1),
        (4,0,0,3),
        (0,2,0,1),
        (0,5,0,3),
        (0,0,3,1),
        (1,1,1,1),
        (1,1,2,1),
        (1,3,1,1)
    )

def test_part1_example1(puzzle_input):
    assert subject.part1(tuple(map(subject.parse_line, puzzle_input))) == 7

def test_part2_example1(puzzle_input):
    assert subject.part2(
        (
            (10,12,12,2),
            (12,14,12,2),
            (16,12,12,4),
            (14,14,14,6),
            (50,50,50,200),
            (10,10,10,5),
        )
    ) == 36
