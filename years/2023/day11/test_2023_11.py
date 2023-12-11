import solve_2023_11 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#....."
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == [
        [0, 3],
        [1, 7],
        [2, 0],
        [4, 6],
        [5, 1],
        [6, 9],
        [8, 7],
        [9, 0],
        [9, 4]
    ]

def test_part1_example1(puzzle_input):
    assert subject.part1(subject.parse_lines(puzzle_input)) == 374

def test_part2_example1(puzzle_input):
    assert subject.part2(subject.parse_lines(puzzle_input), 10) == 1030

