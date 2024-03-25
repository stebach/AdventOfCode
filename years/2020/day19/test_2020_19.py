import solve_2020_19 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        '0: 4 1 5',
        '1: 2 3 | 3 2',
        '2: 4 4 | 5 5',
        '3: 4 5 | 5 4',
        '4: "a"',
        '5: "b"',
        '',
        'ababbb',
        'bababa',
        'abbbab',
        'aaabbb',
        'aaaabbb'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        {
            0: [[4,1,5]],
            1: [[2,3],[3,2]],
            2: [[4,4],[5,5]],
            3: [[4,5],[5,4]],
            4: 'a',
            5: 'b'
        },
        [
            'ababbb',
            'bababa',
            'abbbab',
            'aaabbb',
            'aaaabbb'
        ]
    )

def test_create_regex(puzzle_input):
    data = subject.parse_lines(puzzle_input)
    assert subject.create_regex(data[0]) ==  'a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b'
    