import solve_2015_16 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'Sue 1: cars: 2, trees: 2, pomeranians: 0',
        'Sue 2: goldfish: 1, cars: 5, children: 4',
        'Sue 3: pomeranians: 2, cars: 3, trees: 2',
        'Sue 4: akitas: 10, perfumes: 2, cats: 1',
        'Sue 5: samoyeds: 10, goldfish: 8, cats: 7',
        'Sue 6: vizslas: 2, children: 2, trees: 8',
        'Sue 7: trees: 4, vizslas: 5, pomeranians: 6',
        'Sue 8: cats: 10, perfumes: 3, pomeranians: 7',
        'Sue 9: trees: 4, cats: 6, perfumes: 8',
        'Sue 10: pomeranians: 2, akitas: 9, samoyeds: 1',
        'Sue 11: cars: 1, children: 10, samoyeds: 0',
        'Sue 12: trees: 2, pomeranians: 3, akitas: 3',
        'Sue 13: cars: 7, cats: 7, trees: 3',
        'Sue 14: goldfish: 9, cars: 5, children: 3',
        'Sue 15: akitas: 9, samoyeds: 10, children: 5',
        'Sue 16: cars: 4, children: 0, goldfish: 7',
        'Sue 17: trees: 5, children: 0, samoyeds: 2',
        'Sue 18: pomeranians: 1, akitas: 10, children: 8',
        'Sue 19: goldfish: 5, trees: 3, cars: 2',
        'Sue 20: akitas: 5, perfumes: 0, cars: 0'
    ]

def test_parse_line(puzzle_input):
    assert tuple(map(subject.parse_line, puzzle_input)) == (
        (1, {'cars':2, 'trees':2, 'pomeranians':0 }),
        (2, {'goldfish':1, 'cars':5, 'children':4 }),
        (3, {'pomeranians':2, 'cars':3, 'trees':2 }),
        (4, {'akitas':10, 'perfumes':2, 'cats':1 }),
        (5, {'samoyeds':10, 'goldfish':8, 'cats':7 }),
        (6, {'vizslas':2, 'children':2, 'trees':8 }),
        (7, {'trees':4, 'vizslas':5, 'pomeranians':6 }),
        (8, {'cats':10, 'perfumes':3, 'pomeranians':7 }),
        (9, {'trees':4, 'cats':6, 'perfumes':8 }),
        (10, {'pomeranians':2, 'akitas':9, 'samoyeds':1 }),
        (11, {'cars':1, 'children':10, 'samoyeds':0 }),
        (12, {'trees':2, 'pomeranians':3, 'akitas':3 }),
        (13, {'cars':7, 'cats':7, 'trees':3 }),
        (14, {'goldfish':9, 'cars':5, 'children':3 }),
        (15, {'akitas':9, 'samoyeds':10, 'children':5 }),
        (16, {'cars':4, 'children':0, 'goldfish':7 }),
        (17, {'trees':5, 'children':0, 'samoyeds':2 }),
        (18, {'pomeranians':1, 'akitas':10, 'children':8 }),
        (19, {'goldfish':5, 'trees':3, 'cars':2 }),
        (20, {'akitas':5, 'perfumes':0, 'cars':0 })
    )

def test_find_valid_entries(puzzle_input):
    data = tuple(map(subject.parse_line, puzzle_input))
    assert subject.find_valid_entries(data) == [19]

