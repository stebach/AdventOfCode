import solve_2016_21 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'swap position 4 with position 0',
        'swap letter d with letter b',
        'reverse positions 0 through 4',
        'rotate left 1 step',
        'move position 1 to position 4',
        'move position 3 to position 0',
        'rotate based on position of letter b',
        'rotate based on position of letter d',
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('swap position', 4, 0),
        ('swap letter', 'd', 'b'),
        ('reverse positions', 0, 4),
        ('rotate', 'left', 1),
        ('move position', 1, 4),
        ('move position', 3, 0),
        ('rotate based on position', 'b'),
        ('rotate based on position', 'd'),
    )

def test_scramble(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.scramble('abcde', data[0:1]) == 'ebcda'
    assert subject.scramble('abcde', data[0:2]) == 'edcba'
    assert subject.scramble('abcde', data[0:3]) == 'abcde'
    assert subject.scramble('abcde', data[0:4]) == 'bcdea'
    assert subject.scramble('abcde', data[0:5]) == 'bdeac'
    assert subject.scramble('abcde', data[0:6]) == 'abdec'
    assert subject.scramble('abcde', data[0:7]) == 'ecabd'
    assert subject.scramble('abcde', data[0:8]) == 'decab'

    assert subject.scramble('abcdefg', [('rotate based on position', 'a')]) == 'gabcdef'
    assert subject.scramble('abcdefg', [('rotate based on position', 'b')]) == 'fgabcde'
    assert subject.scramble('abcdefg', [('rotate based on position', 'c')]) == 'efgabcd'
    assert subject.scramble('abcdefg', [('rotate based on position', 'd')]) == 'defgabc'
    assert subject.scramble('abcdefg', [('rotate based on position', 'e')]) == 'bcdefga'

    assert subject.scramble('gabcdef', [('rotate based on position', 'a')], True) == 'abcdefg'
    assert subject.scramble('fgabcde', [('rotate based on position', 'b')], True) == 'abcdefg'
    assert subject.scramble('efgabcd', [('rotate based on position', 'c')], True) == 'abcdefg'

    assert subject.scramble('ebcda', data[0:1], True) == 'abcde'
    assert subject.scramble('edcba', data[0:2], True) == 'abcde'
    assert subject.scramble('abcde', data[0:3], True) == 'abcde'
    assert subject.scramble('bcdea', data[0:4], True) == 'abcde'
    assert subject.scramble('bdeac', data[0:5], True) == 'abcde'
    assert subject.scramble('abdec', data[0:6], True) == 'abcde'


