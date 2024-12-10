import solve_2024_10 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '89010123',
        '78121874',
        '87430965',
        '96549874',
        '45678903',
        '32019012',
        '01329801',
        '10456732'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (8,9,0,1,0,1,2,3),
        (7,8,1,2,1,8,7,4),
        (8,7,4,3,0,9,6,5),
        (9,6,5,4,9,8,7,4),
        (4,5,6,7,8,9,0,3),
        (3,2,0,1,9,0,1,2),
        (0,1,3,2,9,8,0,1),
        (1,0,4,5,6,7,3,2)
    )

def test_get_trailheads(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_trailheads(data) == [5, 6, 5, 3, 1, 3, 5, 3, 5]
    assert subject.get_trailheads(data, True) == [20, 24, 10, 4, 1, 4, 5, 8, 5]

def test_solve(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.solve(data) == (36, 81)
