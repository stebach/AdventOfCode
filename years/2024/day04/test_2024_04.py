import solve_2024_04 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'MMMSXXMASM',
        'MSAMXMSMSA',
        'AMXSXMAAMM',
        'MSAMASMSMX',
        'XMASAMXAMM',
        'XXAMMXXAMA',
        'SMSMSASXSS',
        'SAXAMASAAA',
        'MAMMMXMMMM',
        'MXMXAXMASX'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('M','M','M','S','X','X','M','A','S','M'),
        ('M','S','A','M','X','M','S','M','S','A'),
        ('A','M','X','S','X','M','A','A','M','M'),
        ('M','S','A','M','A','S','M','S','M','X'),
        ('X','M','A','S','A','M','X','A','M','M'),
        ('X','X','A','M','M','X','X','A','M','A'),
        ('S','M','S','M','S','A','S','X','S','S'),
        ('S','A','X','A','M','A','S','A','A','A'),
        ('M','A','M','M','M','X','M','M','M','M'),
        ('M','X','M','X','A','X','M','A','S','X')
    )

def test_search_word(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.search_word(data, 'xmas') == 18

def test_search_crossed_3letter_word(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.search_crossed_3letter_word(data, 'mas') == 9

def test_solve(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.solve(data) == (18, 9)

