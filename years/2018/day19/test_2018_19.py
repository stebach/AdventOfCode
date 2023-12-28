import solve_2018_19 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
    '#ip 0',
    'seti 5 0 1',
    'seti 6 0 2',
    'addi 0 1 0',
    'addr 1 2 3',
    'setr 1 0 0',
    'seti 8 0 4',
    'seti 9 0 5'
]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (subject.OPCODE_IP, 0, 0, 0),
        (subject.OPCODE_SETI, 5, 0, 1),
        (subject.OPCODE_SETI, 6, 0, 2),
        (subject.OPCODE_ADDI, 0, 1, 0),
        (subject.OPCODE_ADDR, 1, 2, 3),
        (subject.OPCODE_SETR, 1, 0, 0),
        (subject.OPCODE_SETI, 8, 0, 4),
        (subject.OPCODE_SETI, 9, 0, 5),
    )

def test_part1_example1(puzzle_input):
    assert subject.part1(tuple(map(subject.parse_line, puzzle_input))) == 7

