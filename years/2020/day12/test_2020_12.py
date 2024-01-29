import solve_2020_12 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'F10',
        'N3',
        'F7',
        'R90',
        'F11'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('F',10),
        ('N',3),
        ('F',7),
        ('R',90),
        ('F',11)
    )

def test_get_manhattan_distance(puzzle_input):
    assert subject.get_manhattan_distance(tuple(map(subject.parse_line, puzzle_input))) == 25

def test_waypoint_movement(puzzle_input):
    assert subject.waypoint_movement(tuple(map(subject.parse_line, puzzle_input))) == 286

