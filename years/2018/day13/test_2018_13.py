import solve_2018_13 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '/->-\\        ',
        '|   |  /----\\',
        '| /-+--+-\  |',
        '| | |  | v  |',
        '\\-+-/  \-+--/',
        '  \\------/',
    ]

@pytest.fixture
def puzzle_input2():
    return [
        '/>-<\\  ',
        '|   |  ',
        '| /<+-\\',
        '| | | v',
        '\\>+</ |',
        '  |   ^',
        '  \\<->/',
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == [
        (
        '/---\\        ',
        '|   |  /----\\',
        '| /-+--+-\  |',
        '| | |  | |  |',
        '\\-+-/  \-+--/',
        '  \\------/',
        ),
        [
            [0,(2,0),(1,0),0],
            [3,(9,3),(0,1),0]
        ]
    ]

def test_part1_example1(puzzle_input):
    assert subject.part1(subject.parse_lines(puzzle_input)) == (7,3)

def test_part2_example1(puzzle_input2):
    assert subject.part2(subject.parse_lines(puzzle_input2)) == (6,4)
