import solve_2016_12 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'cpy 41 a',
        'inc a',
        'inc a',
        'dec a',
        'jnz a 2',
        'dec a'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('cpy', 41, 0),
        ('inc', 0),
        ('inc', 0),
        ('dec', 0),
        ('jnz', 0, 2),
        ('dec', 0),
    )

def test_run(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.run(data)[0] == 42

