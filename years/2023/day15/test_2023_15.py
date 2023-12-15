import solve_2023_15 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

def test_hash():
    assert subject.hash("HASH") == 52

def test_parse_line(puzzle_input):
    assert subject.parse_line(puzzle_input) == [
        'rn=1',
        'cm-',
        'qp=3',
        'cm=2',
        'qp-',
        'pc=4',
        'ot=9',
        'ab=5',
        'pc-',
        'pc=6',
        'ot=7'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(subject.parse_line(puzzle_input)) == [
        ['rn','=',1],
        ['cm','-'],
        ['qp','=',3],
        ['cm','=',2],
        ['qp','-'],
        ['pc','=',4],
        ['ot','=',9],
        ['ab','=',5],
        ['pc','-'],
        ['pc','=',6],
        ['ot','=',7]

    ]

def test_part1_example1(puzzle_input):
    assert subject.part1(subject.parse_line(puzzle_input)) == 1320

def test_part2_example1(puzzle_input):
    assert subject.part2(subject.parse_line(puzzle_input)) == 145

