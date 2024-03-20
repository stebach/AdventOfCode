import solve_2020_18 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '1 + 2 * 3 + 4 * 5 + 6',
        '2 * 3 + (4 * 5)',
        '5 + (8 * 3 + 9 + 3 * 4 * 3)', 
        '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
        '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        [1, '+', 2, '*', 3, '+', 4, '*', 5, '+', 6],
        [2, '*', 3, '+', [4, '*', 5]],
        [5, '+', [8, '*', 3, '+', 9, '+', 3, '*', 4, '*', 3]], 
        [5, '*', 9, '*', [7, '*', 3, '*', 3, '+', 9, '*', 3, '+', [8, '+', 6, '*', 4]]],
        [[[2, '+', 4, '*', 9], '*', [6, '+', 9, '*', 8, '+', 6], '+', 6], '+', 2, '+', 4, '*', 2]
    )

def test_calc():
    assert subject.calc(subject.parse_line('1 + 2 * 3 + 4 * 5 + 6')) == 71
    assert subject.calc(subject.parse_line('1 + (2 * 3) + (4 * (5 + 6))')) == 51
    assert subject.calc(subject.parse_line('2 * 3 + (4 * 5)')) == 26
    assert subject.calc(subject.parse_line('5 + (8 * 3 + 9 + 3 * 4 * 3)')) == 437
    assert subject.calc(subject.parse_line('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')) == 12240
    assert subject.calc(subject.parse_line('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')) == 13632
    assert subject.calc(subject.parse_line('1 + 2 * 3 + 4 * 5 + 6'), True) == 231
    assert subject.calc(subject.parse_line('1 + (2 * 3) + (4 * (5 + 6))'), True) == 51
    assert subject.calc(subject.parse_line('2 * 3 + (4 * 5)'), True) == 46    
    assert subject.calc(subject.parse_line('5 + (8 * 3 + 9 + 3 * 4 * 3)'), True) == 1445
    assert subject.calc(subject.parse_line('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'), True) == 669060
    assert subject.calc(subject.parse_line('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'), True) == 23340


