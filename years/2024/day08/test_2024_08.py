import solve_2024_08 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '............',
        '........0...',
        '.....0......',
        '.......0....',
        '....0.......',
        '......A.....',
        '............',
        '............',
        '........A...',
        '.........A..',
        '............',
        '............'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'h': 12,
        'w': 12,
        'antennas': {
            '0': [(8, 1), (5, 2), (7, 3), (4, 4)],
            'A': [(6, 5), (8, 8), (9, 9)]
        }
    }

def test_unique_antinodes(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert len(subject.unique_antinodes(data)) == 14
    assert len(subject.unique_antinodes(data, True)) == 34

def test_solve(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.solve(data) == (14,34)

