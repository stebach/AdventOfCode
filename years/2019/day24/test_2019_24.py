import solve_2019_24 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return ['....#',
    '#..#.',
    '#..##',
    '..#..',
    '#....']

def test_parse_line(puzzle_input):
    assert list(map(subject.parse_line, puzzle_input)) == [
        ['.','.','.','.','#'],
        ['#','.','.','#','.'],
        ['#','.','.','#','#'],
        ['.','.','#','.','.'],
        ['#','.','.','.','.']
    ]

def test_run_minutes(puzzle_input):
    assert subject.run_minutes(list(map(subject.parse_line, puzzle_input)), 1) == [
        ['#','.','.','#','.'],
        ['#','#','#','#','.'],
        ['#','#','#','.','#'],
        ['#','#','.','#','#'],
        ['.','#','#','.','.']
    ]
    assert subject.run_minutes(list(map(subject.parse_line, puzzle_input)), 2) == [
        ['#','#','#','#','#'],
        ['.','.','.','.','#'],
        ['.','.','.','.','#'],
        ['.','.','.','#','.'],
        ['#','.','#','#','#']
    ]
    assert subject.run_minutes(list(map(subject.parse_line, puzzle_input)), 3) == [
        ['#','.','.','.','.'],
        ['#','#','#','#','.'],
        ['.','.','.','#','#'],
        ['#','.','#','#','.'],
        ['.','#','#','.','#']
    ]
    assert subject.run_minutes(list(map(subject.parse_line, puzzle_input)), 4) == [
        ['#','#','#','#','.'],
        ['.','.','.','.','#'],
        ['#','#','.','.','#'],
        ['.','.','.','.','.'],
        ['#','#','.','.','.']
    ]

def test_first_double(puzzle_input):
    assert subject.run_minutes(list(map(subject.parse_line, puzzle_input)), until_first_double=True) == [
        ['.','.','.','.','.'],
        ['.','.','.','.','.'],
        ['.','.','.','.','.'],
        ['#','.','.','.','.'],
        ['.','#','.','.','.']
    ]

def test_biodiversity_rating():
    assert subject.biodiversity_rating([
        ['.','.','.','.','.'],
        ['.','.','.','.','.'],
        ['.','.','.','.','.'],
        ['#','.','.','.','.'],
        ['.','#','.','.','.']
    ]) == 2129920

def test_run_minutes_multilayer(puzzle_input):
    assert subject.run_minutes_multilayer([list(map(subject.parse_line, puzzle_input))], 10) == [
        [
            ['.','.','#','.','.'],
            ['.','#','.','#','.'],
            ['.','.','.','.','#'],
            ['.','#','.','#','.'],
            ['.','.','#','.','.']
        ],
        [
            ['.','.','.','#','.'],
            ['.','.','.','#','#'],
            ['.','.','.','.','.'],
            ['.','.','.','#','#'],
            ['.','.','.','#','.']
        ],
        [
            ['#','.','#','.','.'],
            ['.','#','.','.','.'],
            ['.','.','.','.','.'],
            ['.','#','.','.','.'],
            ['#','.','#','.','.']
        ],
        [
            ['.','#','.','#','#'],
            ['.','.','.','.','#'],
            ['.','.','.','.','#'],
            ['.','.','.','#','#'],
            ['.','#','#','#','.']
        ],
        [
            ['#','.','.','#','#'],
            ['.','.','.','#','#'],
            ['.','.','.','.','.'],
            ['.','.','.','#','.'],
            ['.','#','#','#','#']
        ],
        [
            ['.','#','.','.','.'],
            ['.','#','.','#','#'],
            ['.','#','.','.','.'],
            ['.','.','.','.','.'],
            ['.','.','.','.','.']
        ],
        [
            ['.','#','#','.','.'],
            ['#','.','.','#','#'],
            ['.','.','.','.','#'],
            ['#','#','.','#','#'],
            ['#','#','#','#','#']
        ],
        [
            ['#','#','#','.','.'],
            ['#','#','.','#','.'],
            ['#','.','.','.','.'],
            ['.','#','.','#','#'],
            ['#','.','#','.','.']
        ],
        [
            ['.','.','#','#','#'],
            ['.','.','.','.','.'],
            ['#','.','.','.','.'],
            ['#','.','.','.','.'],
            ['#','.','.','.','#']
        ],
        [
            ['.','#','#','#','.'],
            ['#','.','.','#','.'],
            ['#','.','.','.','.'],
            ['#','#','.','#','.'],
            ['.','.','.','.','.']
        ],
        [
            ['#','#','#','#','.'],
            ['#','.','.','#','.'],
            ['#','.','.','#','.'],
            ['#','#','#','#','.'],
            ['.','.','.','.','.']
        ]
    ]

