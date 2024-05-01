import solve_2022_22 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "        ...#",
        "        .#..",
        "        #...",
        "        ....",
        "...#.......#",
        "........#...",
        "..#....#....",
        "..........#.",
        "        ...#....",
        "        .....#..",
        "        .#......",
        "        ......#.",
        "",
        "10R5L5R10L4R5L5"
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        (
            '        ...#    ',
            '        .#..    ',
            '        #...    ',
            '        ....    ',
            '...#.......#    ',
            '........#...    ',
            '..#....#....    ',
            '..........#.    ',
            '        ...#....',
            '        .....#..',
            '        .#......',
            '        ......#.',
        ),
        (10, -90, 5, 90, 5, -90, 10, 90, 4, -90, 5, 90, 5),
        (8,0)
    )

def test_get_password(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.get_password(data) == 6032

