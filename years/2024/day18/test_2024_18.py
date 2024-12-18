import solve_2024_18 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '5,4',
        '4,2',
        '4,5',
        '3,0',
        '2,1',
        '6,3',
        '2,4',
        '1,5',
        '0,6',
        '3,3',
        '2,6',
        '5,1',
        '1,2',
        '5,5',
        '2,5',
        '6,5',
        '1,4',
        '0,4',
        '6,4',
        '1,1',
        '6,1',
        '1,0',
        '0,5',
        '1,6',
        '2,0'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (5, 4),
        (4, 2),
        (4, 5),
        (3, 0),
        (2, 1),
        (6, 3),
        (2, 4),
        (1, 5),
        (0, 6),
        (3, 3),
        (2, 6),
        (5, 1),
        (1, 2),
        (5, 5),
        (2, 5),
        (6, 5),
        (1, 4),
        (0, 4),
        (6, 4),
        (1, 1),
        (6, 1),
        (1, 0),
        (0, 5),
        (1, 6),
        (2, 0)
    )

def test_shortest_path(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.shortest_path(data, 6, 12) == 22

def test_find_blocking(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.find_blocking(data, 6) == (6, 1)

def test_solve(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.solve(data, 6, 12) == (22, '6,1')

