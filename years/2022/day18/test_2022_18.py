import solve_2022_18 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '2,2,2',
        '1,2,2',
        '3,2,2',
        '2,1,2',
        '2,3,2',
        '2,2,1',
        '2,2,3',
        '2,2,4',
        '2,2,6',
        '1,2,5',
        '3,2,5',
        '2,1,5',
        '2,3,5',
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (2,2,2),
        (1,2,2),
        (3,2,2),
        (2,1,2),
        (2,3,2),
        (2,2,1),
        (2,2,3),
        (2,2,4),
        (2,2,6),
        (1,2,5),
        (3,2,5),
        (2,1,5),
        (2,3,5),
    )

def test_get_surface(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_surface(data) == 64

def test_get_exterior_surface(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_exterior_surface(data) == 58


