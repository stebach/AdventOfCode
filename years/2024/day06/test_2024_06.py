import solve_2024_06 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '....#.....',
        '.........#',
        '..........',
        '..#.......',
        '.......#..',
        '..........',
        '.#..^.....',
        '........#.',
        '#.........',
        '......#...'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == {
        'w': 10,
        'h': 10,
        'guard': {
            'pos': (4,6),
            'direction': (0,-1)
        },
        'obstacles': set(((4,0),(9,1),(2,3),(7,4),(1,6),(8,7),(0,8),(6,9)))
    }

def test_count_visited(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.count_visited(data) == 41

def test_find_loop_possibilities(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.find_loop_possibilities(data) == 6

def test_solve(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.solve(data) == (41,6)

