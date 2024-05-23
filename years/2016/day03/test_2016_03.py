import solve_2016_03 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '  100  120  200',
        '  300  200  100',
        '   50  100  250',
        '  100  120  200',
        '  300  200  100',
        '   50  100  250',
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (100,120,200),
        (300,200,100),
        (50,100,250),
        (100,120,200),
        (300,200,100),
        (50,100,250),
    )

def test_count_valid_triangles(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.count_valid_triangles(data) == 2

def test_count_valid_triangles_vertical(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.count_valid_triangles_vertical(data) == 4

