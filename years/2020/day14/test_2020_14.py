import solve_2020_14 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
        'mem[8] = 11',
        'mem[7] = 101',
        'mem[8] = 0'
    ]

@pytest.fixture
def puzzle_input2():
    return [
        'mask = 000000000000000000000000000000X1001X',
        'mem[42] = 100',
        'mask = 00000000000000000000000000000000X0XX',
        'mem[26] = 1'
    ]


def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('mask','XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'),
        ('mem',8,11),
        ('mem',7,101),
        ('mem',8,0),
    )

def test_initialize(puzzle_input):
    assert subject.initialize(tuple(map(subject.parse_line, puzzle_input))) == 165

def test_initialize2(puzzle_input2):
    assert subject.initialize2(tuple(map(subject.parse_line, puzzle_input2))) == 208


