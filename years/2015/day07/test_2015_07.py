import solve_2015_07 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '123 -> x',
        '456 -> y',
        'x AND y -> d',
        'x OR y -> e',
        'x LSHIFT 2 -> f',
        'y RSHIFT 2 -> g',
        'NOT x -> h',
        'NOT y -> i'
    ]

def test_parse_line(puzzle_input):
    assert dict(map(subject.parse_line, puzzle_input)) == {
        'x': ('123',),
        'y': ('456',),
        'd': ('AND','x','y'),
        'e': ('OR','x','y'),
        'f': ('LSHIFT','x',2),
        'g': ('RSHIFT','y',2),
        'h': ('NOT','x'),
        'i': ('NOT','y'),
    }

def test_get_signals(puzzle_input):
    data = dict(map(subject.parse_line, puzzle_input))
    assert subject.get_signals(data) == {
        'd': 72,
        'e': 507,
        'f': 492,
        'g': 114,
        'h': 65412,
        'i': 65079,
        'x': 123,
        'y': 456,
    }

