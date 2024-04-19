import solve_2022_12 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "Sabqponm",
        "abcryxxl",
        "accszExk",
        "acctuvwj",
        "abdefghi"
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        [
            [0,0,1,16,15,14,13,12],
            [0,1,2,17,24,23,23,11],
            [0,2,2,18,25,25,23,10],
            [0,2,2,19,20,21,22,9],
            [0,1,3,4,5,6,7,8]
        ],
        (0,0),
        (5,2)
    )

def test_steps(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.steps(data) == 31
    assert subject.steps(data, True) == 29
