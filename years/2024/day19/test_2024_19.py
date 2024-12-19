import solve_2024_19 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'r, wr, b, g, bwu, rb, gb, br',
        '',
        'brwrr',
        'bggr',
        'gbbr',
        'rrbgbr',
        'ubwu',
        'bwurrg',
        'brgr',
        'bbrgwb'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'towels': ('r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br'),
        'designs': ('brwrr', 'bggr', 'gbbr', 'rrbgbr', 'ubwu', 'bwurrg', 'brgr', 'bbrgwb')
    }

def test_possible_designs(puzzle_input):
    data = [x for x in subject.possible_designs(subject.parse_lines(puzzle_input)) if x > 0]
    assert len(data) == 6
    assert sum(data) == 16

def test_solve(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.solve(data) == (6, 16)

