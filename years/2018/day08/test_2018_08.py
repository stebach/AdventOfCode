import solve_2018_08 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

def test_parse_line(puzzle_input):
    assert subject.parse_line(puzzle_input)[1] == [
        [
            [
                [],
                [10,11,12]
            ],
            [
                [
                    [
                        [],
                        [99]
                    ]
                ],
                [2]
            ],
        ],
        [1,1,2]
    ]

def test_part1_example1(puzzle_input):
    assert subject.part1(subject.parse_line(puzzle_input)[1]) == 138

def test_part2_example1(puzzle_input):
    assert subject.part2(subject.parse_line(puzzle_input)[1]) == 66

