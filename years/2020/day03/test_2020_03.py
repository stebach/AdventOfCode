import solve_2020_03 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '..##.......',
        '#...#...#..',
        '.#....#..#.',
        '..#.#...#.#',
        '.#...##..#.',
        '..#.##.....',
        '.#.#.#....#',
        '.#........#',
        '#.##...#...',
        '#...##....#',
        '.#..#...#.#'
    ]

def test_count_trees(puzzle_input):
    assert subject.count_trees(puzzle_input, 3, 1) == 7
    assert subject.count_trees(puzzle_input, 1, 1) == 2
    assert subject.count_trees(puzzle_input, 5, 1) == 3
    assert subject.count_trees(puzzle_input, 7, 1) == 4
    assert subject.count_trees(puzzle_input, 1, 2) == 2


