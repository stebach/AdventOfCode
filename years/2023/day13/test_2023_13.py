import solve_2023_13 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == [
        [
            "#.##..##.",
            "..#.##.#.",
            "##......#",
            "##......#",
            "..#.##.#.",
            "..##..##.",
            "#.#.##.#.",
        ],[
            "#...##..#",
            "#....#..#",
            "..##..###",
            "#####.##.",
            "#####.##.",
            "..##..###",
            "#....#..#"
        ]
    ]

def test_start_of_reflection(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.start_of_reflection(data[0]) == -1
    assert subject.start_of_reflection(data[0], rotate=True) == 4
    assert subject.start_of_reflection(data[1]) == 3

    assert subject.start_of_reflection(data[0], smudge=True) == 2
    assert subject.start_of_reflection(data[0], rotate=True, smudge=True) == -1
    assert subject.start_of_reflection(data[1], smudge=True) == 0

def test_part1_example1(puzzle_input):
    assert subject.part1(subject.parse_lines(puzzle_input)) == 405

def test_part2_example1(puzzle_input):
    assert subject.part2(subject.parse_lines(puzzle_input)) == 400
