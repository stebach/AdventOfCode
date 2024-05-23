import solve_2016_02 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'ULL',
        'RRDDD',
        'LURDL',
        'UUUUD'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('U','L','L'),
        ('R','R','D','D','D'),
        ('L','U','R','D','L'),
        ('U','U','U','U','D')
    )

def test_get_code(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_code(data) == 1985
    
def test_get_code_two(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.get_code_two(data) == '5DB3'
    
