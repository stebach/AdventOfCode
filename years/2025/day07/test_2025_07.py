import solve_2025_07 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return ['.......S.......',
    '...............',
    '.......^.......',
    '...............',
    '......^.^......',
    '...............',
    '.....^.^.^.....',
    '...............',
    '....^.^...^....',
    '...............',
    '...^.^...^.^...',
    '...............',
    '..^...^.....^..',
    '...............',
    '.^.^.^.^.^...^.',
    '...............']

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'start': (7, 0),
        'splitters': (
            (7, 2),
            (6, 4),
            (8, 4),
            (5, 6),
            (7, 6),
            (9, 6),
            (4, 8),
            (6, 8),
            (10, 8),
            (3, 10),
            (5, 10),
            (9, 10),
            (11, 10),
            (2, 12),
            (6, 12),
            (12, 12),
            (1, 14),
            (3, 14),
            (5, 14),
            (7, 14),
            (9, 14),
            (13, 14)
        ),
        'height': 16,
    }

def test_solve(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.solve(data) == (21,40)

