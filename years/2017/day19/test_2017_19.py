import solve_2017_19 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
    '     |          ',
    '     |  +--+    ',
    '     A  |  C    ',
    ' F---|----E|--+ ',
    '     |  |  |  D ',
    '     +B-+  +--+ ',
]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '),
        (' ',' ',' ',' ',' ','|',' ',' ','+','-','-','+',' ',' ',' ',' '),
        (' ',' ',' ',' ',' ','A',' ',' ','|',' ',' ','C',' ',' ',' ',' '),
        (' ','F','-','-','-','|','-','-','-','-','E','|','-','-','+',' '),
        (' ',' ',' ',' ',' ','|',' ',' ','|',' ',' ','|',' ',' ','D',' '),
        (' ',' ',' ',' ',' ','+','B','-','+',' ',' ','+','-','-','+',' '),
    )

def test_get_letters(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_letters(data) == 'ABCDEF'
    assert subject.get_letters(data, True) == 38


