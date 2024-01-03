import solve_2019_06 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'COM)B',
        'B)C',
        'C)D',
        'D)E',
        'E)F',
        'B)G',
        'G)H',
        'D)I',
        'E)J',
        'J)K',
        'K)L'
    ]

@pytest.fixture
def puzzle_input2():
    return [
        'COM)B',
        'B)C',
        'C)D',
        'D)E',
        'E)F',
        'B)G',
        'G)H',
        'D)I',
        'E)J',
        'J)K',
        'K)L',
        'K)YOU',
        'I)SAN'
    ]


def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        ('COM','B'),
        ('B','C'),
        ('C','D'),
        ('D','E'),
        ('E','F'),
        ('B','G'),
        ('G','H'),
        ('D','I'),
        ('E','J'),
        ('J','K'),
        ('K','L')
    )

def test_part1(puzzle_input):
    assert subject.part1(tuple(map(subject.parse_line, puzzle_input))) == 42

def test_part2(puzzle_input2):
    assert subject.part2(tuple(map(subject.parse_line, puzzle_input2))) == 4

