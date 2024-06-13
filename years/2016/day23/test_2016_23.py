import solve_2016_23 as subject
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

def test_run(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.run(data)[0] == 3


