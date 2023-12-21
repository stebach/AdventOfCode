import solve_2023_21 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '...........',
        '.....###.#.',
        '.###.##..#.',
        '..#.#...#..',
        '....#.#....',
        '.##..S####.',
        '.##..#...#.',
        '.......##..',
        '.##.#.####.',
        '.##..##.##.',
        '...........'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        (5,5),
        (11,11),
        ((5,1),(6,1),(7,1),(9,1),(1,2),(2,2),(3,2),(5,2),(6,2),(9,2),(2,3),(4,3),(8,3),(4,4),(6,4),(1,5),(2,5),(6,5),(7,5),(8,5),(9,5),(1,6),(2,6),(5,6),(9,6),(7,7),(8,7),(1,8),(2,8),(4,8),(6,8),(7,8),(8,8),(9,8),(1,9),(2,9),(5,9),(6,9),(8,9),(9,9))
    )

def test_part1_example1(puzzle_input):
    assert subject.part1(subject.parse_lines(puzzle_input), 1) == 2
    assert subject.part1(subject.parse_lines(puzzle_input), 2) == 4
    assert subject.part1(subject.parse_lines(puzzle_input), 3) == 6
    assert subject.part1(subject.parse_lines(puzzle_input), 6) == 16

