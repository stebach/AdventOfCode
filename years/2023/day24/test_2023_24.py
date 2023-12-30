import solve_2023_24 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '19, 13, 30 @ -2, 1, -2',
        '18, 19, 22 @ -1, -1, -2',
        '20, 25, 34 @ -2, -2, -4',
        '12, 31, 28 @ -1, -2, -1',
        '20, 19, 15 @ 1, -5, -3',
        '20, 25, 34 @ -2, -2, -4'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ((19,13,30),(-2,1,-2)),
        ((18,19,22),(-1,-1,-2)),
        ((20,25,34),(-2,-2,-4)),
        ((12,31,28),(-1,-2,-1)),
        ((20,19,15),(1,-5,-3)),
        ((20,25,34),(-2,-2,-4))
    )

def test_part1_example1(puzzle_input):
    points = tuple(map(subject.parse_line, puzzle_input))
    assert subject.find_intersection(points[0], points[1], True) == (14 + 1/3, 15 + 1/3, points[0][0][2])
    assert subject.find_intersection(points[0], points[2], True) == (11 + 2/3, 16 + 2/3, points[0][0][2])
    assert subject.find_intersection(points[0], points[3], True) == (6.2, 19.4, points[0][0][2])
    assert subject.find_intersection(points[0], points[4], True) == None
    assert subject.find_intersection(points[1], points[5], True) == None
