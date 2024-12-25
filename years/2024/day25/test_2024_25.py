import solve_2024_25 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '#####',
        '.####',
        '.####',
        '.####',
        '.#.#.',
        '.#...',
        '.....',
        '',
        '#####',
        '##.##',
        '.#.##',
        '...##',
        '...#.',
        '...#.',
        '.....',
        '',
        '.....',
        '#....',
        '#....',
        '#...#',
        '#.#.#',
        '#.###',
        '#####',
        '',
        '.....',
        '.....',
        '#.#..',
        '###..',
        '###.#',
        '###.#',
        '#####',
        '',
        '.....',
        '.....',
        '.....',
        '#....',
        '#.#..',
        '#.#.#',
        '#####'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'locks': (
            (0, 5, 3, 4, 3),
            (1, 2, 0, 5, 3)
        ),
        'keys': (
            (5, 0, 2, 1, 3),
            (4, 3, 4, 0, 2),
            (3, 0, 2, 0, 1)
        )
    }

def test_get_fitting_pair_count(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.get_fitting_pair_count(data) == 3

def test_solve(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.solve(data) == (3, None)

