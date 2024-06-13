import solve_2016_25 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'cpy 2 a',
        'tgl a',
        'tgl a',
        'tgl a',
        'cpy 1 a',
        'dec a',
        'dec a'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('cpy','2','a'),
        ('tgl','a'),
        ('tgl','a'),
        ('tgl','a'),
        ('cpy','1','a'),
        ('dec','a'),
        ('dec','a'),
    )