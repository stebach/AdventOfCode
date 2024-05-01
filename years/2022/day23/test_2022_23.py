import solve_2022_23 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "....#..",
        "..###.#",
        "#...#.#",
        ".#...##",
        "#.###..",
        "##.#.##",
        ".#..#.."
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        (4,0),
        (2,1),
        (3,1),
        (4,1),
        (6,1),
        (0,2),
        (4,2),
        (6,2),
        (1,3),
        (5,3),
        (6,3),
        (0,4),
        (2,4),
        (3,4),
        (4,4),
        (0,5),
        (1,5),
        (3,5),
        (5,5),
        (6,5),
        (1,6),
        (4,6),
    )

def test_move_elfs(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.move_elfs(data, 10)[0] == 110
    assert subject.move_elfs(data)[1] == 20

