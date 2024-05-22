import solve_2015_23 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'inc a',
        'jio a, +2',
        'tpl a',
        'inc a'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('inc','a'),
        ('jio','a', 2),
        ('tpl','a'),
        ('inc','a'),
    )

def test_run(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.run(data)['a'] == 2


