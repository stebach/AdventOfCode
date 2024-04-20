import solve_2022_13 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        "[1,1,3,1,1]",
        "[1,1,5,1,1]",
        "",
        "[[1],[2,3,4]]",
        "[[1],4]",
        "",
        "[9]",
        "[[8,7,6]]",
        "",
        "[[4,4],4,4]",
        "[[4,4],4,4,4]",
        "",
        "[7,7,7,7]",
        "[7,7,7]",
        "",
        "[]",
        "[3]",
        "",
        "[[[]]]",
        "[[]]",
        "",
        "[1,[2,[3,[4,[5,6,7]]]],8,9]",
        "[1,[2,[3,[4,[5,6,0]]]],8,9]"
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == [
        [
            [1,1,3,1,1],
            [1,1,5,1,1],
        ],
        [
            [[1],[2,3,4]],
            [[1],4],
        ],
        [
            [9],
            [[8,7,6]],
        ],
        [
            [[4,4],4,4],
            [[4,4],4,4,4],
        ],
        [
            [7,7,7,7],
            [7,7,7],
        ],
        [
            [],
            [3],
        ],
        [
            [[[]]],
            [[]],
        ],
        [
            [1,[2,[3,[4,[5,6,7]]]],8,9],
            [1,[2,[3,[4,[5,6,0]]]],8,9]
        ]
    ]

def test_right_order(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert sum(subject.right_order(data)) == 13

def test_decoder_key(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.decoder_key(data) == 140
