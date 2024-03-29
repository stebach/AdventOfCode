import solve_2023_23 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '#.#####################',
        '#.......#########...###',
        '#######.#########.#.###',
        '###.....#.>.>.###.#.###',
        '###v#####.#v#.###.#.###',
        '###.>...#.#.#.....#...#',
        '###v###.#.#.#########.#',
        '###...#.#.#.......#...#',
        '#####.#.#.#######.#.###',
        '#.....#.#.#.......#...#',
        '#.#####.#.#.#########v#',
        '#.#...#...#...###...>.#',
        '#.#.#v#######v###.###v#',
        '#...#.>.#...>.>.#.###.#',
        '#####v#.#.###v#.#.###.#',
        '#.....#...#...#.#.#...#',
        '#.#########.###.#.#.###',
        '#...###...#...#...#.###',
        '###.###.#.###v#####v###',
        '#...#...#.#.>.>.#.>.###',
        '#.###.###.#.###.#.#v###',
        '#.....###...###...#...#',
        '#####################.#'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        (1,0),
        (21,22),
        {
            (1,0): {
                (3,5):15
            },
            (3,5):{
                (5,13): 22,
                (11,3):22
            },
            (5,13): {
                (13,19):38,
                (13,13):12
            },
            (11,3): {
                (21,11):30,
                (13,13):24
            },
            (13,19): {
                (19,19):10
            },
            (13,13): {
                (21,11):18,
                (13,19):10
            },
            (21,11):{
                (19,19):10
            },
            (19,19):{
                (21,22):5
            },
            (21,22): {}
        },
        {
            (1,0): {
                (3,5):15
            },
            (3,5):{
                (1,0): 15,
                (5,13): 22,
                (11,3): 22,
            },
            (5,13): {
                (3,5): 22,
                (13,19):38,
                (13,13):12,
            },
            (11,3): {
                (3,5): 22,
                (21,11):30,
                (13,13):24,
            },
            (13,19): {
                (5,13):38,
                (19,19):10,
                (13,13):10,
            },
            (13,13): {
                (5,13):12,
                (11,3):24,
                (13,19):10,
                (21,11):18,
            },
            (21,11):{
                (11,3):30,
                (13,13):18,
                (19,19):10
            },
            (19,19):{
                (13,19):10,
                (21,11):10,
                (21,22):5,
            },
            (21,22): {
                (19,19):5,
            }
        }
    )

def test_part1_example1(puzzle_input):
    assert subject.part1(subject.parse_lines(puzzle_input)) == 94

def test_part2_example1(puzzle_input):
    assert subject.part2(subject.parse_lines(puzzle_input)) == 154