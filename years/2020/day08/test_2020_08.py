import solve_2020_08 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'nop +0',
        'acc +1',
        'jmp +4',
        'acc +3',
        'jmp -3',
        'acc -99',
        'acc +1',
        'jmp -4',
        'acc +6'
    ]

def test_parse_line(puzzle_input):  
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('nop', 0),
        ('acc', 1),
        ('jmp', 4),
        ('acc', 3),
        ('jmp', -3),
        ('acc', -99),
        ('acc', 1),
        ('jmp', -4),
        ('acc', 6),
    )

def test_find_loop(puzzle_input):
    assert subject.run_app(tuple(map(subject.parse_line, puzzle_input))) == (5, True)

def test_fix_app(puzzle_input):
    assert subject.fix_app(tuple(map(subject.parse_line, puzzle_input))) == 8

