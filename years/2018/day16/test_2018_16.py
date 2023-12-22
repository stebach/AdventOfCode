import solve_2018_16 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'Before: [3, 2, 1, 1]',
        '9 2 1 2',
        'After:  [3, 2, 2, 1]',
        '',
        'Before: [2, 1, 0, 2]',
        '6 1 3 3',
        'After:  [2, 1, 0, 0]',
        '',
        '',
        '',
        '2 2 3 2',
        '15 1 0 1',
        '10 1 0 1'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        (
            (
                (3,2,1,1),
                (9,2,1,2),
                (3,2,2,1)
            ),
            (
                (2,1,0,2),
                (6,1,3,3),
                (2,1,0,0)
            ),
        ),
        (
            (2,2,3,2),
            (15,1,0,1),
            (10,1,0,1),
        )
    )

def test_part1_example1(puzzle_input):
    assert subject.possible_opcodes(
        subject.parse_lines(puzzle_input)[0][0]
    ) == 3

