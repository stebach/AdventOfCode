import solve_2017_20 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>',
        'p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>'
    ]

@pytest.fixture
def puzzle_input2():
    return [
        'p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>',
        'p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>',
        'p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>',
        'p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>',
    ]


def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (3,0,0,2,0,0,-1,0,0),
        (4,0,0,0,0,0,-2,0,0),
    )

def test_closest_long_term(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.closest_long_term(data) == 0

def test_remove_collisions(puzzle_input2):
    data = tuple(map(subject.parse_line, puzzle_input2))
    assert subject.remove_collisions(data) == 1

