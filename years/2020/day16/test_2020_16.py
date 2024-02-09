import solve_2020_16 as subject
import pytest

@pytest.fixture
def puzzle_input():
    return [
        'class: 1-3 or 5-7',
        'row: 6-11 or 33-44',
        'seat: 13-40 or 45-50',
        '',
        'your ticket:',
        '7,1,14',
        '',
        'nearby tickets:',
        '7,3,47',
        '40,4,50',
        '55,2,20',
        '38,6,12'
    ]

def test_parse_lines(puzzle_input):
    assert subject.parse_lines(puzzle_input) == (
        {
            "class":(
                (1,3),(5,7)
            ),
            "row":(
                (6,11),(33,44)
            ),
            "seat":(
                (13,40),(45,50)
            ),
        },
        (7,1,14),
        (
            (7,3,47),
            (40,4,50),
            (55,2,20),
            (38,6,12)
        )
    )

def test_check1(puzzle_input):
    assert subject.check1(subject.parse_lines(puzzle_input)) == 71

