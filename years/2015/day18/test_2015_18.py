import solve_2015_18 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '.#.#.#',
        '...##.',
        '#....#',
        '..#...',
        '#.#..#',
        '####..'
    ]

@pytest.fixture
def puzzle_input2():
    return [
        '##.#.#',
        '...##.',
        '#....#',
        '..#...',
        '#.#..#',
        '####.#'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (6, 6, set(
        [(1,0),(3,0),(5,0),(3,1),(4,1),(0,2),(5,2),(2,3),(0,4),(2,4),(5,4),(0,5),(1,5),(2,5),(3,5)]
    ))

def test_animate(puzzle_input, puzzle_input2):
    data = subject.parse_lines(puzzle_input)
    assert len(subject.animate(data, 4)) == 4

    data = subject.parse_lines(puzzle_input2)
    assert len(subject.animate(data, 5, True)) == 17


