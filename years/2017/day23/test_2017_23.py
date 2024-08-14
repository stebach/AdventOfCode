import solve_2017_23 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'set a 1',
        'add a 2',
        'mul a a',
        'mod a 5',
        'snd a',
        'set a 0',
        'rcv a',
        'jgz a -1',
        'set a 1',
        'jgz a -2'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('set','a','n',1),
        ('add','a','n',2),
        ('mul','a','r','a'),
        ('mod','a','n',5),
        ('snd','a'),
        ('set','a','n',0),
        ('rcv','a'),
        ('jgz','a','n',-1),
        ('set','a','n',1),
        ('jgz','a','n',-2),
    )

